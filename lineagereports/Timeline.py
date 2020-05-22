'''Given some sample metadata, create a timeline
Based on code from https://github.com/COG-UK/phylo-reports
All samples passed in go on the same timeline
'''
import matplotlib.pyplot as plt


class Timeline:
    def __init__(self, samples, lineage):
        self.samples = samples
        self.lineage = lineage
        
        
    def oldest_date(self):
        return min([self.samples[s].sample_date for s in self.samples])
        
    def newest_date(self):
        return max([self.samples[s].sample_date for s in self.samples])
        
    def all_dates(self):
        return  sorted(list(set([self.samples[s].sample_date for s in self.samples])))
        
    def num_samples_on_date(self, target_date):
        return len([self.samples[s].sample_date for s in self.samples if self.samples[s].sample_date == target_date])
        

    def make_timeline(self, plot_width = 12, plot_height = 5):
            
        fig,ax = plt.subplots(figsize=(plot_width, plot_height))
        
        point_oldest = self.oldest_date()
        point_newest = self.newest_date()
        x = [point_oldest, point_newest]
        y = [2, 2]
        
        
        # These are the points on the line
        x2 = list(self.all_dates())
        y2 = []
        sizes2 = []
        
        for target_date in x2:
            
            sizes2.append((self.num_samples_on_date(target_date))*40)
            y2.append(2)
        
            height = [2]
            ytick_list = [self.lineage]
        
        plt.scatter(x2,y2, zorder=2, s=sizes2)
        plt.plot(x,y, color='black', zorder=1)

            
        plt.yticks(height, ytick_list, size=10)
        plt.ylim(1, 3)
        plt.xticks(rotation=45)
        plt.show()
        