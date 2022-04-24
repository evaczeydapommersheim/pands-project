# This program is to import and analyze the Iris dataset by R.A. Fisher
# Author Eva Czeyda-Pommersheim

# The following libraries were chosen to be imported for this project/analysis:

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt # Using matplotlib to visualize data during analysis
import pandas as pd 

# Create txt file for summary of each variable
# filename = "summary.txt"

# Define function to write/append txt file with information
# def write_txt(obj):
#    with open (filename, 'at') as f:
#        txt = f.write(str(obj))
 #       print(txt)

# Step 1 - importing the Iris dataset dowloaded from https://archive.ics.uci.edu/ml/datasets/iris
# Added column headers in notepad to inlcude in csv file
iris_data = pd.read_csv('iris.data')

# Step 2 - Print the first 5 lines of the dataset to get a visual of the pandas dataset 
iris_data_structure = iris_data.head()
print("\nThe structure of the dataset is the following:\n", iris_data_structure,"\n")

# Step 3 - use the .info() function to gain information about the dataset
# Describing the 5 variables (columns), the number of datapoints (150) the datatypes and if there are any missing data
# In this case there is no missing data found in the dataset (Column Non-null)
print("\nThere are five variables in the dataset with no empty cells and 150 datapoints:\n")
iris_data.info()

# Step 4 - The the species column can be accessed by using data.species to count the number of datapoints for each species
# There are three species of the Iris flower described by this dataset, 50 datapoints each
species_count = iris_data.Species.value_counts()
print("\nThe dataset includes information about 3 species of the iris flower with 50 datapoints each:\n", species_count, "\n")

# Step 5 - In order to get an overview of the dataset from a statistical perspective
# the data.describe() function can be used and will output a detailed overview of each numeric variable
# Such as the mean and standard deviation of the sepal width and length, petal width and length
# the min and max as well as the percentile values
# all of these give an understanding of the data, allows to compare the four numeric variables

variable_summary = iris_data.describe()
print("\nAdditional statistical information can be gained about the dataset based on the below values:\n", variable_summary, "\n")

# Step 6 - the mode() function describes the values that appear in the dataset most frequently
# By default the function displays all columns/variables in the dataset
# By using the numeric_only = True boolean expression only numeric data is being considered
iris_data_mode = iris_data.mode(numeric_only = True)
print("The most frequently occurring values by variables are: \n", iris_data_mode)

# Step 7 - change the column names to eliminate the (cm) UoM
# Printing the head() of the dataset to review new column names
cols = ["Sepal Length (cm)", "Sepal Width (cm)", "Petal Length (cm)", "Petal Width (cm)"]
iris_data.rename(columns = {cols[0]:"Sepal_Length", cols[1]:"Sepal_Width", cols[2]:"Petal_Length", cols[3]:"Petal_Width"}, inplace=True)
print(iris_data.head())

# Step 8 - check for correlation between the variables:
correlation = iris_data.corr()
print("\nThere is correlation between certain variables:\n", correlation)

# length_features = [iris_data["Sepal_Length"], iris_data["Petal_Length"]]
# width_features = [iris_data["Sepal_Width"], iris_data["Petal_Width"]]

# Step 9 - Visualization of the relationships between the four features (Columns)
# Using seaborn and matplotlib.pyplot libraries
# Save plots in individual png files

g = sns.relplot(x=iris_data["Sepal_Length"],y=iris_data["Sepal_Width"],
kind="scatter", hue=iris_data["Species"])
g.set(xlabel="Sepal Length", ylabel="Sepal Width")
plt.title('Iris Data Scatter Plot 1', color = 'blue', size = 20)
plt.savefig('IrisDataScatterPlot1.png')

g = sns.relplot(x=iris_data["Sepal_Length"],y=iris_data["Petal_Length"],
kind="scatter", hue=iris_data["Species"])
g.set(xlabel="Sepal Length", ylabel="Petal Length")
plt.title('Iris Data Scatter Plot 2', color = 'blue', size = 20)
plt.savefig('IrisDataScatterPlot2.png')

g = sns.relplot(x=iris_data["Petal_Length"],y=iris_data["Petal_Width"],
kind="scatter", hue=iris_data["Species"])
g.set(xlabel="Petal Length", ylabel="Petal Width")
plt.title('Iris Data Scatter Plot 3', color = 'blue', size = 20)
plt.savefig('IrisDataScatterPlot3.png')

g = sns.relplot(x=iris_data["Petal_Width"],y=iris_data["Sepal_Width"],
kind="scatter", hue=iris_data["Species"])
g.set(xlabel="Petal Width", ylabel="Sepal Width")
plt.title('Iris Data Scatter Plot 4', color = 'blue', size = 20)
plt.savefig('IrisDataScatterPlot4.png')




                 
 


                   
