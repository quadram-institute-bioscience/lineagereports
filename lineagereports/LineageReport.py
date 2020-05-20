'''Given a single lineage and metadata files and filtration criteria, produce a report'''
import csv
from lineagereports.LineagesMetadata import LineagesMetadata
from lineagereports.FilterSamples import FilterSamples
from lineagereports.Timeline import Timeline

class LineageReport:
    
    def __init__(self, lineages_sample_filename, extended_sample_filename, sequencing_centre,  country = "UK"):
        self.lineages_sample_filename = lineages_sample_filename
        self.extended_sample_filename = extended_sample_filename
        self.sequencing_centre = sequencing_centre
        self.country = country
        
    def create_uk_lineage_report(self, uk_lineage):
        samples = LineagesMetadata(self.lineages_sample_filename, self.extended_sample_filename ).create_samples()
        fs = FilterSamples(samples)
        filtered_samples = fs.filter_by_dict_of_attributes({
            'country': self.country,  
            #'sequencing_org_code': self.sequencing_centre, 
            'uk_lineage': uk_lineage})
            
        tl = Timeline(filtered_samples, uk_lineage)
        tl.make_timeline()
        
