'''Given sample metadata, compare the lineages found in different collecting orgs'''
import csv
from lineagereports.LineagesMetadata import LineagesMetadata
from lineagereports.FilterSamples import FilterSamples
from lineagereports.CollectingOrgLineages import CollectingOrgLineages

class CollectingOrgReport:
    
    def __init__(self, lineages_sample_filename, extended_sample_filename, sequencing_centre, country = "UK"):
        self.lineages_sample_filename = lineages_sample_filename
        self.extended_sample_filename = extended_sample_filename
        self.sequencing_centre = sequencing_centre
        self.country = country
        
    def create_collecting_org_report(self):
        samples = LineagesMetadata(self.lineages_sample_filename, self.extended_sample_filename ).create_samples()
        
        # Filter the samples by the criteria passed in.
        filtering_criteria = self.create_filtering_criteria(  ) 
        filtered_samples = samples
        if filtering_criteria:
            fs = FilterSamples(samples)     
            filtered_samples = fs.filter_by_dict_of_attributes( filtering_criteria)
            
        col = CollectingOrgLineages(filtered_samples, 'uk_lineage')
        output_array = col.create_shared_lineage_matrix()
        
        for row in output_array:
            print("\t".join([str(c) for c in row]))
        
    def create_filtering_criteria(self):
        filtering_criteria  = {}
        if self.country is not None and self.country != "":
            filtering_criteria['country'] = self.country
            
        if self.sequencing_centre is not None and self.sequencing_centre != "":
            filtering_criteria['sequencing_org_code'] = self.sequencing_centre
        return filtering_criteria
        
        
        
