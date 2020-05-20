import unittest
import os
import shutil
from lineagereports.Sample  import Sample

class TestSample(unittest.TestCase):
   
    def test_initialise_empty(self):
        s = Sample('ABC', {})
        self.assertEqual(s.lineage, None)

    def test_valid_sample(self):
        s = Sample('NORW-1234', {
                'sequence_name': 'England/NORW-1234/2020',
                'sample_date': '2020-01-01',
                'epi_week': '15',
                'country': 'UK',
                'adm2': 'NORFOLK',
                'lineage': 'B1.2.3.4',
                'uk_lineage': 'UK1234',
                'acc_lineage': 'B.1_23'
            })
        self.assertEqual(s.central_sample_id, 'NORW-1234')
        self.assertEqual(s.sequence_name, 'England/NORW-1234/2020')
        self.assertEqual(s.sample_date, '2020-01-01')
        self.assertEqual(s.epi_week, '15')
        self.assertEqual(s.country, 'UK')
        self.assertEqual(s.adm2, 'NORFOLK')
        self.assertEqual(s.lineage, 'B1.2.3.4')
        self.assertEqual(s.uk_lineage, 'UK1234')
        self.assertEqual(s.acc_lineage, 'B.1_23')
        
    def test_valid_parital_sample(self):
        s = Sample('NORW-1234', {
                'sequence_name': 'England/NORW-1234/2020',
                'lineage': 'B1.2.3.4',
                'uk_lineage': 'UK1234',
            })
        self.assertEqual(s.central_sample_id, 'NORW-1234')
        self.assertEqual(s.sequence_name, 'England/NORW-1234/2020')
        self.assertEqual(s.sample_date, None)
        self.assertEqual(s.epi_week, None)
        self.assertEqual(s.country, None)
        self.assertEqual(s.adm2, None)
        self.assertEqual(s.lineage, 'B1.2.3.4')
        self.assertEqual(s.uk_lineage, 'UK1234')
        self.assertEqual(s.acc_lineage, None)
        
    def test_add_extended_metadata_to_empty(self):
        s = Sample('NORW-1234', {})
        s.add_extended_metadata({            
            'source_age': '50',
            'source_sex': 'M',
            'collecting_org': 'ABC',
            'sequencing_org_code': 'NORW'
        })
        self.assertEqual(s.central_sample_id, 'NORW-1234')
        self.assertEqual(s.source_age, '50')
        self.assertEqual(s.source_sex, 'M')
        self.assertEqual(s.collecting_org, 'ABC')
        self.assertEqual(s.sequencing_org_code, 'NORW')
        
    def test_add_extended_metadata_to_full(self):
        s = Sample('NORW-1234', {
                'sequence_name': 'England/NORW-1234/2020',
                'sample_date': '2020-01-01',
                'epi_week': '15',
                'country': 'UK',
                'adm2': 'NORFOLK',
                'lineage': 'B1.2.3.4',
                'uk_lineage': 'UK1234',
                'acc_lineage': 'B.1_23'
            })
        s.add_extended_metadata({            
            'source_age': '50',
            'source_sex': 'M',
            'collecting_org': 'ABC',
            'sequencing_org_code': 'NORW'
        })
        self.assertEqual(s.central_sample_id, 'NORW-1234')
        self.assertEqual(s.sequence_name, 'England/NORW-1234/2020')
        self.assertEqual(s.sample_date, '2020-01-01')
        self.assertEqual(s.epi_week, '15')
        self.assertEqual(s.country, 'UK')
        self.assertEqual(s.adm2, 'NORFOLK')
        self.assertEqual(s.lineage, 'B1.2.3.4')
        self.assertEqual(s.uk_lineage, 'UK1234')
        self.assertEqual(s.acc_lineage, 'B.1_23')
        self.assertEqual(s.source_age, '50')
        self.assertEqual(s.source_sex, 'M')
        self.assertEqual(s.collecting_org, 'ABC')
        self.assertEqual(s.sequencing_org_code, 'NORW')

