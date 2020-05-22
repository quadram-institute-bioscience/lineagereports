'''Given a single lineage and metadata files and filtration criteria, produce a report'''
import csv
from lineagereports.LineagesMetadata import LineagesMetadata
from lineagereports.FilterSamples import FilterSamples
from lineagereports.Timeline import Timeline

class LineageReport:
    
    def __init__(self, lineages_sample_filename, extended_sample_filename, sequencing_centre, collecting_org, country = "UK"):
        self.lineages_sample_filename = lineages_sample_filename
        self.extended_sample_filename = extended_sample_filename
        self.sequencing_centre = sequencing_centre
        self.collecting_org = collecting_org
        self.country = country
        
    def create_uk_lineage_report(self, uk_lineage):
        samples = LineagesMetadata(self.lineages_sample_filename, self.extended_sample_filename ).create_samples()
        fs = FilterSamples(samples)     
        filtered_samples = fs.filter_by_dict_of_attributes( self.create_filtering_criteria( uk_lineage ) )
            
        tl = Timeline(filtered_samples, uk_lineage)
        tl.make_timeline()
        
    def create_filtering_criteria(self, uk_lineage):
        filtering_criteria  = {'uk_lineage': uk_lineage}
        if self.collecting_org is not None and self.collecting_org != "":
            filtering_criteria['collecting_org'] = self.collecting_org
            
        if self.country is not None and self.country != "":
            filtering_criteria['country'] = self.country
            
        if self.sequencing_centre is not None and self.sequencing_centre != "":
            filtering_criteria['sequencing_org_code'] = self.sequencing_centre
        return filtering_criteria
        
        
        
