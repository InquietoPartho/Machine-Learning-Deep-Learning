# -*- coding: utf-8 -*-
"""Complete Pandas.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16PpEQ47e0Iqvy3Xr0HfyOiICFLL7SzNt
"""

!pip install pandas

import pandas as pd

df = pd.read_csv('/content/partho.csv')

df.head()

#creating a Pandas dataframe
lst = ['Pijush','kanti','Roy','Partho',
          'ECE','HSTU']

df = pd.DataFrame(lst)
print(df)

#Creating DataFrame from dict of Ndarray/lists

#python code demostrate creating
#DataFrame from dict narray/ Lists
#By default addresses

#initialise data of lists

data = {'Name' : ['Pijush','Kanti','Roy','Partho'],
        'Age':[20,21,19,18]}

#creating DataFrame

df = pd.DataFrame(data)

print(df)

"""#Dealing with Rows And Columns"""

data = {'Name':['Partho','Pijush','Irtiza','Deya'],
        'Age' :[27,24,22,32],
        'Address':['Lalmonirhat','Aditmari','Kisoreganj','Mymensingh'],
        'Qualification':['AA','XX','AA','CC']}
#convert the dictionary into DataFrame
df = pd.DataFrame(data)

print(df)

#dealing with column
data = {'Name':['Partho','Pijush','Irtiza','Deya'],
        'Age' :[27,24,22,32],
        'Address':['Lalmonirhat','Aditmari','Kisoreganj','Mymensingh'],
        'Qualification':['AA','XX','AA','CC']}
#convert the dictionary into DataFrame
df = pd.DataFrame(data)
#select two columns
print(df[['Name','Qualification']])

df = pd.read_csv('/content/nba.csv')
df.head()

#dealing a row

#making data frame from CSV file
data = pd.read_csv('/content/nba.csv',index_col = "Name")

#retrieving row by loc method

first = data.loc["Avery Bradley"]
second = data.loc["R.J. Hunter"]

print(first,"\n\n\n", second)



"""Pandas Library:
Useful For Data Processing and Analysis

Pandas Data Frame:
Pandas DataFrame is two-dimensional tabular data structure with lebeled axes (rows and Columns)
"""

#importing the pandas library

import pandas as pd
import numpy as np

"""Creating pandas DataFrame"""

boston_df = pd.read_csv('/content/BostonHousing.csv')

df.head()

diabates_df = pd.read_csv('/content/diabetes.csv')

diabates_df.head()

diabates_df.shape

#creating dataframe with random values

random_df = pd.DataFrame(np.random.rand(20,10))

random_df.head()

random_df.shape

"""Inspecting a DataFrame"""

#finding the number of rows and columns

diabates_df.shape

#first 5 rows in a DataFrame
diabates_df.head()

#last 5 rows in the DataFrame

diabates_df.tail()

#information of dataframe

diabates_df.info()

#finding the number of missing values

boston_df.isnull().sum()

diabates_df.head()

#counting the values based on the lebels

diabates_df.value_counts('Outcome')

#grouo the values based on the mean

diabates_df.groupby('Outcome').mean()

"""#statistical Measure"""

#count the number of values
boston_df.count()

#mean value --> column wise
boston_df.mean()

# standard deviation -->column wise
boston_df.std()

#minimum value
boston_df.min()

#maximum value for each column
boston_df.max()

#All the statistical measures of the dataframe
boston_df.describe()

"""#Manipulating a dataframe"""

#adding a column to a dataframe
boston_df['Price'] = boston_df.target

#removing a row

boston_df.drop(index = 0,axis = 0)

#drop a column
boston_df.drop(columns='zn',axis=1)

#locating a row using the index value

boston_df.iloc[2]

#locating a particular column

print(boston_df.iloc[:,0]) #first column of the data frame
print(boston_df.iloc[:,1]) # second column
print(boston_df.iloc[:,2]) #third column
print(boston_df.iloc[:,-1]) #last colmun values

"""Corelation
1. Positive Corelation
2. Negative Corelation
"""

boston_df.corr()

