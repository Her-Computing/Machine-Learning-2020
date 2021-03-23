import numpy as np 
import pandas as pd
import seaborn as sns

#loading in seaborn dataset
titanic = sns.load_dataset('titanic')

print("beginning of dataset\n", titanic.head()) #printing first five rows of dataset

print("\nunique ages in dataset\n", titanic.age.unique()) #printing all unique ages

print("\naggregated col counts\n", titanic.describe()) #notice that age has 714 counts instead of 891 counts, this means that some cols have no age val, denoted with NaN

#dealing with missing vals by deleting all rows that have NaN, this can have heavy implications on total data
titanic = titanic.dropna()
print(titanic.head())
print("\naggregated col counts\n", titanic.describe()) #down to 182 rows instead of 891