'''Read the metadata from multiple files and create objects for each sample'''
import csv

class LineagesMetadata:
    
    def __init__(self, lineages_sample_filename, extended_sample_filename):
        self.lineages_sample_filename = lineages_sample_filename
        self.extended_sample_filename = extended_sample_filename
        
    def run(self):
        samples = self.create_lineages_samples_from_file()
        self.add_extended_metadata_to_samples(samples)

    '''Take in the short lineages metadata file and create basic sample objects, with a dictionary key of the central_sample_id NORW-E1234'''
    def create_lineages_samples_from_file(self):
        samples = {}
        with open(self.lineages_sample_filename, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                central_sample_id = sequence["sequence_name"].split("/")[1]
                sample = Sample(central_sample_id, row)
                samples[central_sample_id] = sample
        return samples
        
    '''Take in a set of sample objects and add on extended metadata'''
    def add_extended_metadata_to_samples(self, samples):
        with open(self.extended_sample_filename, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row['central_sample_id'] in samples:
                    samples[row['central_sample_id']].add_extended_metadata(row)
        return samples
                
