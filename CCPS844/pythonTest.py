import pandas as pd

x = {'one':[1,2,3], 'two':[4,5,6]}

df = pd.DataFrame(x)
df.set_index(['a','b','c'])

print(df)
