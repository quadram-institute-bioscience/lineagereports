import unittest
import os
import shutil
from lineagereports.LineagesMetadata  import LineagesMetadata

test_modules_dir = os.path.dirname(os.path.realpath(__file__))
data_dir = os.path.join(test_modules_dir, 'data','lineages_metadata')

class TestLineagesMetadata(unittest.TestCase):
   
    def test_initialise_one_sample(self):
        l = LineagesMetadata(os.path.join(data_dir,'one_sample_lineages.csv'), os.path.join(data_dir,'one_sample_extended.csv'))
        samples = l.create_samples()
        self.assertEqual(samples['NORW-1234'].central_sample_id, 'NORW-1234')
        self.assertEqual(samples['NORW-1234'].sequence_name, 'England/NORW-1234/2020')
        self.assertEqual(samples['NORW-1234'].sample_date, '2020-01-01')
        self.assertEqual(samples['NORW-1234'].epi_week, '19.0')
        self.assertEqual(samples['NORW-1234'].country, 'UK')
        self.assertEqual(samples['NORW-1234'].adm2, 'NORFOLK')
        self.assertEqual(samples['NORW-1234'].lineage, 'B.1.2')
        self.assertEqual(samples['NORW-1234'].uk_lineage, 'UK1234')
        self.assertEqual(samples['NORW-1234'].acc_lineage, 'B.1_234')
        self.assertEqual(samples['NORW-1234'].source_age, '1.0')
        self.assertEqual(samples['NORW-1234'].source_sex, 'M')
        self.assertEqual(samples['NORW-1234'].sequencing_org_code, 'NORW')
        self.assertEqual(samples['NORW-1234'].collecting_org, None)
        
    # additional metadata (sequencing_org_code)
    def test_initialise_one_sample_local(self):
        l = LineagesMetadata(os.path.join(data_dir,'one_sample_lineages.csv'), os.path.join(data_dir,'one_sample_extended_local.csv'))
        samples = l.create_samples()
        self.assertEqual(samples['NORW-1234'].central_sample_id, 'NORW-1234')
        self.assertEqual(samples['NORW-1234'].sequence_name, 'England/NORW-1234/2020')
        self.assertEqual(samples['NORW-1234'].sample_date, '2020-01-01')
        self.assertEqual(samples['NORW-1234'].epi_week, '19.0')
        self.assertEqual(samples['NORW-1234'].country, 'UK')
        self.assertEqual(samples['NORW-1234'].adm2, 'NORFOLK')
        self.assertEqual(samples['NORW-1234'].lineage, 'B.1.2')
        self.assertEqual(samples['NORW-1234'].uk_lineage, 'UK1234')
        self.assertEqual(samples['NORW-1234'].acc_lineage, 'B.1_234')
        self.assertEqual(samples['NORW-1234'].source_age, '1.0')
        self.assertEqual(samples['NORW-1234'].source_sex, 'M')
        self.assertEqual(samples['NORW-1234'].sequencing_org_code, None)
        self.assertEqual(samples['NORW-1234'].collecting_org, 'ABC')
        