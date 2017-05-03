import pandas as pd 
     
import matplotlib

# Force matplotlib to not use any Xwindows backend.
matplotlib.use('Agg')

import matplotlib.pyplot as plt

 
     
print 'reading data...'
df = pd.read_csv("ganglia-metrics.csv", index_col=0, parse_dates=['Timestamp'])
     
print 'analysing data...'
dfm = df.groupby(pd.TimeGrouper(freq='M')).sum()
     
print dfm.head()
     
dfm.plot()
print 'saving global graph'
plt.savefig("result_graph.pdf")
     
     
dfm.hist()
print 'saving histogram graph'
plt.savefig("hist_graph.pdf"
