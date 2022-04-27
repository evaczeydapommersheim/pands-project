# This program is to create visualization of the Iris dataset
# Export images of plots to png files

# Author:Eva Czeyda-Pommersheim

from statistics import stdev
from isort import file
from nbformat import write
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd 



# Read in the original iris.data file and print its content
iris = pd.read_csv('iris_ds.data', sep=',', header = None)
print('The original file is with no column names:\n', iris)


# This content has no header/column names only the raw data listed by Species
# Add column names to the imported datafile by creating the list [cols]
cols = ['Sepal Length', 'Sepal Width','Petal Length','Petal Width', 'Species']

# Create a new dataframe with the column names using the names argument
iris2 = pd.read_csv('iris_ds.data', sep=',', names = cols)
print("The dataframe now includes the column names: \n",iris2)

# Group the attribute variables into one dataframe
#  Use of iloc[] to identify the rows and columns required to break into a sub dataframe
features = iris2.iloc[:,:-1] 
species = iris2.iloc[:,-1]
# print(features.head())
# print(type(features))
# print (species.head())
# print(type(species))

# Print and save histogram plots for each attribute variable
plt.hist(iris2["Sepal Length"])
plt.xlabel("cm")
plt.ylabel("Count")
plt.title("Sepal Length")
plt.savefig("Hist_sepal_length.png")
plt.close()

plt.hist(iris2["Sepal Width"])
plt.xlabel("cm")
plt.ylabel("Count")
plt.title("Sepal Width")
plt.savefig("Hist_sepal_width.png")
plt.close()

plt.hist(iris2["Petal Length"])
plt.xlabel("cm")
plt.ylabel("Count")
plt.title("Petal Length")
plt.savefig("Hist_petal_length.png")
plt.close()

plt.hist(iris2["Petal Width"])
plt.xlabel("cm")
plt.ylabel("Count")
plt.title("Petal Width")
plt.savefig("Hist_petal_width.png")
plt.close()

# Create scatter plots for each pair of the variables

sns.set_context("notebook")
custom_palette=["red","green","purple"]
sns.set_palette(custom_palette)
g=sns.relplot(data=iris2, kind="scatter", hue="Species", x="Sepal Length", y="Sepal Width")
g.set(xlabel="Sepal Length", ylabel="Sepal Width") 
plt.title('Iris Data Scatter Plot 1', color = 'black', size = 15)
plt.savefig('IrisDataScatterPlot1.png')
plt.close()

sns.set_context("notebook")
custom_palette=["red","green","purple"]
sns.set_palette(custom_palette)
g=sns.relplot(data=iris2, kind="scatter", hue="Species", x="Sepal Length", y="Petal Length")
g.set(xlabel="Sepal Length", ylabel="Petal Length")
plt.title('Iris Data Scatter Plot 2', color = 'black', size = 15)
plt.savefig('IrisDataScatterPlot2.png')
plt.close()

sns.set_context("notebook")
custom_palette=["red","green","purple"]
sns.set_palette(custom_palette)
g=sns.relplot(data=iris2, kind="scatter", hue="Species", x="Sepal Length", y="Petal Width")
g.set(xlabel="Sepal Length", ylabel="Petal Width")
plt.title('Iris Data Scatter Plot 3', color = 'black', size = 15)
plt.savefig('IrisDataScatterPlot3.png')
plt.close()

sns.set_context("notebook")
custom_palette=["red","green","purple"]
sns.set_palette(custom_palette)
g=sns.relplot(data=iris2, kind="scatter", hue="Species", x="Petal Length", y="Petal Width")
g.set(xlabel="Petal Length", ylabel="Petal Width")
plt.title('Iris Data Scatter Plot 4', color = 'black', size = 15)
plt.savefig('IrisDataScatterPlot4.png')
plt.close()

