import pandas as pd
import matplotlib.pyplot as plt

from pysankey import sankey

df = pd.read_csv(
    'C:/Users/sulahmed/source/repos/data viz/needs-assistance.csv', sep=',',
    names=['id', 'needs', 'assistance', 'weight']
)
weight = df['weight'].values[1:].astype(float)

ax = sankey(
      left=df['needs'].values[1:], right=df['assistance'].values[1:],
      rightWeight=weight, leftWeight=weight, aspect=12, fontsize=8
)

plt.show() # to display
plt.savefig('needs-assistance.png', bbox_inches='tight') # to savey