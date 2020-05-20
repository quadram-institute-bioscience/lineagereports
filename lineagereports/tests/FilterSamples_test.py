import unittest
import os
import shutil
from lineagereports.FilterSamples  import FilterSamples
from lineagereports.Sample import Sample

class TestFilterSamples(unittest.TestCase):
   
    #def test_filter_by_country(self):
    #    samples = {'NORW-1111': Sample('NORW-1111', {'country': 'UK'}), 'NORW-2222': Sample('NORW-2222', {'country': 'UK'}), 'NORW-3333': Sample('NORW-3333', {'country': 'USA'})}
    #    fs = FilterSamples(samples)
    #    self.assertEqual(len(fs.filter_by_dict_of_attributes({'country': 'UK'})), 2)
    #    self.assertEqual(len(fs.filter_by_dict_of_attributes({'country': 'USA'})), 1)
        
    def test_filter_by_multiple_criteria(self):
        samples = {
            'NORW-1111': Sample('NORW-1111', {'country': 'UK',  'uk_lineage':'UK1'}).add_extended_metadata({'sequencing_org_code': 'CAMB'}), 
            'NORW-2222': Sample('NORW-2222', {'country': 'UK',  'uk_lineage':'UK1'}).add_extended_metadata({'sequencing_org_code': 'NORW'}), 
            'NORW-3333': Sample('NORW-3333', {'country': 'UK', 'sequencing_org_code': 'NORW', 'uk_lineage':'UK2'}).add_extended_metadata({'sequencing_org_code': 'NORW'}),
    'NORW-4444': Sample('NORW-4444', {'country': 'UK', 'sequencing_org_code': 'NORW', 'uk_lineage':'UK1'}).add_extended_metadata({'sequencing_org_code': 'NORW'}), 
    'NORW-5555': Sample('NORW-5555', {'country': 'USA', 'sequencing_org_code': 'CAMB', 'uk_lineage':'UK1'}).add_extended_metadata({'sequencing_org_code': 'NORW'}), 
    'NORW-6666': Sample('NORW-6666', {'country': 'UK', 'sequencing_org_code': 'NORW', 'uk_lineage':'UK1'}).add_extended_metadata({'sequencing_org_code': 'NORW'})
    
    }
        fs = FilterSamples(samples)
        self.assertEqual(len(fs.filter_by_dict_of_attributes({
            'country': 'UK'})), 5)
        self.assertEqual(len(fs.filter_by_dict_of_attributes({
            'country': 'UK',  
            'sequencing_org_code': 'NORW'})), 4)
        self.assertEqual(len(fs.filter_by_dict_of_attributes({
            'country': 'UK',  
            'sequencing_org_code': 'NORW', 
            'uk_lineage': 'UK1'})), 3)
       

