import pandas as pd
from project3.models import User

df = pd.DataFrame({'id': ['x','y','z'],
                   'Username':  ['B','A','C'],
                    'Score' : [75,92,56]})
print(df)



# changing order of columns
df = df.reindex_axis(['id','Username','Score'], axis=1)

# appending
df.loc[3] = ['a','A', 96]

print (df)
