import pandas as pd
import numpy as np

np.random.seed(33) # set the random seed for reproducibility

# Pandas series is buit on top of Numpy arrays, but it has Named Index
s = pd.Series([1, 2, 3, 4, 5])
print(f"\n s = \n{s}") # original series

# add the named index to the series
s.index = ['a', 'b', 'c', 'd', 'e']

print(f"\n s = \n{s}") # original series
print(f"\n s.index = \n{s.index}") # index of the series
print(f"\n s.values = \n{s.values}") # values of the series
print(f"\n s.dtype = \n{s.dtype}") # data type of the series
print(f"\n s.shape = \n{s.shape}") # shape of the series
print(f"\n s.size = \n{s.size}") # total number of elements in the series
print(f"\n s[0] = \n{s[0]}") # access the first element of the series using integer index
print(f"\n s['a'] = \n{s['a']}") # access the first element of the series using named index
print(f"\n s[1:4] = \n{s[1:4]}") # access a slice of the series using integer index
print(f"\n s['b':'d'] = \n{s['b':'d']}") # access a slice of the series using named index
print(f"\n s[s > 2] = \n{s[s > 2]}") # access elements of the series that satisfy a condition

# demo build dataframe from a numpy array
data = np.random.rand(5, 3) # create a 2D array of random values between 0 and 1 with shape (5, 3)
df = pd.DataFrame(data, columns=['A', 'B', 'C']) # create a dataframe from the 2D array with specified column names
print(f"\n df = \n{df}") # original dataframe
print(f"\n df.columns = \n{df.columns}") # column names of the dataframe
print(f"\n df.index = \n{df.index}") # index of the dataframe
print(f"\n df.values = \n{df.values}") # values of the dataframe
print(f"\n df.dtypes = \n{df.dtypes}") # data types of the dataframe columns
print(f"\n df.shape = \n{df.shape}") # shape of the dataframe
print(f"\n df.size = \n{df.size}") # total number of elements in the dataframe
print(f"\n df['A'] = \n{df['A']}") # access a column of the dataframe using column name
print(f"\n df.iloc[0] = \n{df.iloc[0]}") # access the first row of the dataframe using integer index
print(f"\n df.loc[0] = \n{df.loc[0]}") # access the first row of the dataframe using label index (same as integer index in this case)
print(f"\n df.iloc[0, 0] = \n{df.iloc[0, 0]}") # access the element in the first row and first column
print(f"\n df.loc[0, 'A'] = \n{df.loc[0, 'A']}") # access the element in the first row and column 'A'
print(f"\n df[df['A'] > 0.5] = \n{df[df['A'] > 0.5]}") # access rows of the dataframe where the values in column 'A' satisfy a condition

# demo build dataframe from a dictionary
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Age': [25, 30, 35, 40, 45],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
        }

df = pd.DataFrame(data) # create a dataframe from the dictionary
print(f"\n df = \n{df}") # original dataframe
print(f"\n df.columns = \n{df.columns}") # column names of the dataframe
print(f"\n df.index = \n{df.index}") # index of the dataframe
print(f"\n df.values = \n{df.values}") # values of the dataframe
print(f"\n df.dtypes = \n{df.dtypes}") # data types of the dataframe columns
print(f"\n df.shape = \n{df.shape}") # shape of the dataframe
print(f"\n df.size = \n{df.size}") # total number of elements in the dataframe
print(f"\n df['Name'] = \n{df['Name']}") # access a column of the dataframe using column name
print(f"\n df.iloc[0] = \n{df.iloc[0]}") # access the first row of the dataframe using integer index
print(f"\n df.loc[0] = \n{df.loc[0]}") # access the first row of the dataframe using label index (same as integer index in this case)
print(f"\n df.iloc[0, 0] = \n{df.iloc[0, 0]}") # access the element in the first row and first column   