'''Given a set of samples, create a table of the number of lineages in common between collecting orgs
'''

class CollectingOrg:
    def __init__(self, collecting_org_name):
        self.collecting_org_name = collecting_org_name
        self.lineages_to_num_samples = {}

class CollectingOrgLineages:
    def __init__(self, samples, lineage_attribute):
        self.samples = samples
        self.lineage_attribute = lineage_attribute
        
    def create_shared_lineage_matrix(self):
        org_to_lineage = self.collecting_org_lineage_freq() 
        output_array = self.pairwise_lineage_output(org_to_lineage)
        return output_array
        
    def pairwise_lineage_output(self, org_to_lineage):
        output_array = []
        organisations = sorted(org_to_lineage.keys())
        # header for array
        output_array.append([""] + organisations)
        
        for source_org in organisations:
            row_output = [source_org]
            for target_org in organisations:
                # get the intersection in the lineage names between organisations
                num_lineages_in_common = list(set(org_to_lineage[source_org].lineages_to_num_samples) & set(org_to_lineage[target_org].lineages_to_num_samples))
                row_output.append(len(num_lineages_in_common))
            output_array.append(row_output)
        return output_array
        
    
    def collecting_org_lineage_freq(self):
        org_names = {}

        for s in self.samples:
            lineage = getattr(self.samples[s], self.lineage_attribute)
            collecting_org = self.samples[s].collecting_org 
            
            if collecting_org is not None \
               and collecting_org != "" \
               and collecting_org != "-" \
               and lineage is not None \
               and lineage != "" \
               and lineage != '-':
                if collecting_org not in org_names:
                    org_names[collecting_org] = CollectingOrg(collecting_org)
                    
                if lineage in org_names[collecting_org].lineages_to_num_samples:
                    org_names[collecting_org].lineages_to_num_samples[lineage] += 1
                else:
                     org_names[collecting_org].lineages_to_num_samples[lineage] = 1
                    
        return org_names
            
            
              
        