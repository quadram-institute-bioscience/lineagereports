'''Take in some samples and apply various filtration criteria'''

class FilterSamples:
    def __init__(self, samples):
        self.samples = samples
         
    # filter by an attribute creating a copy so we can reuse
    def filter_by_attribute(self, input_samples, attribute_name, attribute_value):
        filtered_samples = {}
        for s in input_samples:
            if getattr(input_samples[s], attribute_name) == attribute_value:
                filtered_samples[s] = input_samples[s]
        return filtered_samples
         
    # takes in a dictionary of attributes and filters on them, applying sequentially
    # {'country': 'UK', 'sequencing_org_code': 'NORW', 'uk_lineage': 'UK1234' }
    def filter_by_dict_of_attributes(self, filter_attributes):
        input_samples = self.samples
        for attribute_name, attribute_value in filter_attributes.items():
            filtered_samples = self.filter_by_attribute(input_samples, attribute_name, attribute_value)
            input_samples = filtered_samples
        return input_samples
        

    