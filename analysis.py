# This program is to import and analyze the Iris dataset by R.A. Fisher

# Author Eva Czeyda-Pommersheim

from multiprocessing import Value
from statistics import stdev
from isort import file
from nbformat import write
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd 


# Read in the original iris.data file and print its content
iris = pd.read_csv('iris_ds.data', sep=',', header = None)
print('The original file is with no column names:\n', iris, "\n", file=open("summary.txt", "wt"))


# This content has no header/column names only the raw data listed by Species
# Add column names to the imported datafile by creating the list [cols]
cols = ['Sepal Length', 'Sepal Width','Petal Length','Petal Width', 'Species']

# Create a new dataframe with the column names using the names argument
iris2 = pd.read_csv('iris_ds.data', sep=',', names = cols)
print("The dataframe now includes the column names: \n",iris2, "\n", file=open("summary.txt", "at"))

# Review and summarize the dataframe content:


print("The first five rows of the dataframe are:\n", iris2.head(), "\n", file=open("summary.txt", "at")) 
print("The last rows of the dataframe are:\n", iris2.tail(), "\n", file=open("summary.txt", "at"))
print("Every 50th item of the dataframe are:\n:", iris2.loc[::50], "\n", file=open("summary.txt", "at"))

#This method prints information about a DataFrame including the index dtype and columns
# non-null values and memory usage.
# [https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.info.html]
# this function only has a return of None and can only be printed
# into a file if it is passed into a buffer (solution sourced from above link)
import io
buffer = io.StringIO()
iris2.info(buf=buffer)
s = buffer.getvalue()
print("Brief overview of the dataset, type of data, column names, null values:\n", s, "\n", file=open("summary.txt", "at"))

# In order to get an overview of the dataset from a statistical perspective
# the data.describe() function can be used and will output a detailed overview of each numeric variable
# Such as the mean and standard deviation of the sepal width and length, petal width and length
# the min and max as well as the percentile values
# all of these give an understanding of the data, allows to compare the four numeric variables

print("Each feature (numerical attribute data) can be reviewed as a distribution:\n", iris2.describe(), "\n", file=open("summary.txt", "at"))

# Each attribute has 50 datapoints across the 3 species of the Iris flower:
print("This dataset explores the above attributes across three species:\n", iris2.Species.value_counts(), "\n", file=open("summary.txt", "at"))

# Distribution of the attribute data can also be reviewed by these species:
print("Following are the mean values of each attribute by species:\n", iris2.groupby('Species').mean(), "\n", file=open("summary.txt", "at"))
print("The standard deviation of the attributes by species are: \n", iris2.groupby('Species').std(), "\n", file=open("summary.txt", "at"))
print("The minimum of the attributes by species are: \n", iris2.groupby('Species').min(), "\n", file=open("summary.txt", "at"))
print("The maximum value of the attributes by species are: \n", iris2.groupby('Species').max(), "\n", file=open("summary.txt", "at"))
print("The median value of the attributes by species are: \n", iris2.groupby('Species').median(), "\n", file=open("summary.txt", "at"))
print("Checking for any correlation between attribute variables by species: \n", iris2.groupby("Species").corr(), "\n", file=open("summary.txt", "at"))
