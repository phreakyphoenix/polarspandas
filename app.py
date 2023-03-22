# %%
import pandas as pd
import polars as pl
import numpy as np

# %%
# Create a datafram with 1 million rows and 10 columns
df = pd.DataFrame(np.random.rand(10000000, 10), columns=['col_'+str(i) for i in range(10)])
pl_df = pl.DataFrame(df)

# %%
# Selecting a column
#Pandas
%timeit -r7 -n 1000 df[['col_0','col_1']]

#Polars
%timeit -r7 -n 1000 pl_df[['col_0','col_1']]
%timeit -r7 -n 1000 pl_df.select(pl.col(['col_0','col_1']))

# %%
#Filtering rows 
#Pandas
%timeit -r7 -n 1000 df.query ('col_0>0.5')           
#Polars        
%timeit -r7 -n 1000 pl_df.filter(pl.col('col_0')>0.5)       

# %%
#Grouping by col_0 and calculating the mean of col_1
%timeit -r7 -n 1000 df.groupby('col_0')['col_1'].mean()              
%timeit -r7 -n 1000 df.groupby('col_0')['col_1'].agg('mean')         

#polars
%timeit -r7 -n 1000 pl_df.groupby('col_0').agg([pl.col('col_1').mean()]) #square indexing
%timeit -r7 -n 1000 pl_df.groupby('col_0').agg(pl.mean('col_1'))      #shorter syntax


# %%
#Conversion between wide and long formats
#Pandas
%timeit -r7 -n 1000 pd.melt(df, id_vars=['col_0'], value_vars=['col_1', 'col_2', 'col_3', 'col_4', 'col_5', 'col_6', 'col_7', 'col_8', 'col_9'])
#Polars
%timeit -r7 -n 1000 pl_df.melt(id_vars=['col_0'], value_vars=['col_1', 'col_2', 'col_3', 'col_4', 'col_5', 'col_6', 'col_7', 'col_8', 'col_9'])

# %%



