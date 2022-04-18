# This program is to import and analyze the Iris dataset by R.A. Fisher
# Author Eva Czeyda-Pommersheim

# The following modules were chosen to be imported for this project/analysis:
import numpy as np
import matplotlib as plt # Using matplotlib to visualize data during analysis
from sklearn.datasets import load_iris # Load Iris dataset using sci-kit learn (sklearn) machine learning module
import pandas as pd # Usinig pandas module to analyze the data


data = load_iris()  # Loading the Iris dataset

df = pd.DataFrame(data.data, columns = data.feature_names) # creating the dataframe by adding the column names for each of the variables
df.to_csv('iris_dataset.csv')
print(df.head())                        # Printing the first 5 rows of the dataset to understand the way the data is structured
print(df.info())                        # df.info() gives an overview of the dataframe, provides information on null values if any (in this case none) and the type of the data (float numbers)
print(df.describe())                    # df.describe() gives a statistical review of the four variables, it does not give a breakdown by the Iris species
print(df.to_string())                   # df.to_string() prints out the full dataframe