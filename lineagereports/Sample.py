'''Object to represent a sample, populated from various metadata spreadsheets'''

class Sample:
     def __init__(self, central_sample_id, sample_metadata):
         self.central_sample_id = central_sample_id
         
         # setup a select number of attributes
         for md_field in [
             'sequence_name', 
             'sample_date',
             'epi_week', 
             'country', 
             'adm2', 
             'lineage', 
             'uk_lineage', 
             'acc_lineage'
         ]:
             if md_field in sample_metadata:
                 setattr(self, md_field, sample_metadata[md_field])
             else:
                 setattr(self, md_field, None)
                 
     def add_extended_metadata(self, sample_metadata):
         for md_field in [
             'source_age',	
             'source_sex',
             'collecting_org',
             'sequencing_org_code'
         ]:
             if md_field in sample_metadata:
                 setattr(self, md_field, sample_metadata[md_field])
             else:
                 setattr(self, md_field, None)
         return self
                 