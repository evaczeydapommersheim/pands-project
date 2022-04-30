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
g=sns.relplot(data=iris2, kind="scatter", hue="Species", x="Sepal Length", y="Sepal Width", height=5)
g.set(xlabel="Sepal Length", ylabel="Sepal Width") 
plt.title('Iris Data Scatter Plot 1', color = 'blue', size = 10)
plt.savefig('IrisDataScatterPlot1.png')
plt.close()

sns.set_context("notebook")
custom_palette=["red","green","purple"]
sns.set_palette(custom_palette)
g=sns.relplot(data=iris2, kind="scatter", hue="Species", x="Sepal Length", y="Petal Length")
g.set(xlabel="Sepal Length", ylabel="Petal Length")
plt.title('Iris Data Scatter Plot 2', color = 'blue', size = 10)
plt.savefig('IrisDataScatterPlot2.png')
plt.close()

sns.set_context("notebook")
custom_palette=["red","green","purple"]
sns.set_palette(custom_palette)
g=sns.relplot(data=iris2, kind="scatter", hue="Species", x="Sepal Length", y="Petal Width")
g.set(xlabel="Sepal Length", ylabel="Petal Width")
plt.title('Iris Data Scatter Plot 3', color = 'blue', size = 10)
plt.savefig('IrisDataScatterPlot3.png')
plt.close()

sns.set_context("notebook")
custom_palette=["red","green","purple"]
sns.set_palette(custom_palette)
g=sns.relplot(data=iris2, kind="scatter", hue="Species", x="Petal Length", y="Petal Width")
g.set(xlabel="Petal Length", ylabel="Petal Width")
plt.title('Iris Data Scatter Plot 4', color = 'blue', size = 10)
plt.savefig('IrisDataScatterPlot4.png')
plt.close()

# Create a matrix of plot using Seaborn PairGrid solution
# Provides a faster and comprehensive summary of the individual pair plots
# Helps understanding that data through clear visualization

# This is to separate the attribute variables into a list
variables = ['Sepal Length', 'Sepal Width','Petal Length','Petal Width']
# Use of Pairgrid setting diagonal plots to be histograms which will provide a distribution plot of each variable
# Chose scatterplot to plot each individual data by the species of the flower
g = sns.PairGrid(data=iris2, hue = "Species", vars = variables, height=5, aspect=5/5)
g.map_diag(sns.histplot)
g.map_offdiag(sns.scatterplot)
g.add_legend()
g.fig.suptitle
plt.title("Iris Data PairGrid Plot")
plt.savefig('Iris_Features_PairPlot.png')
plt.close()

# Boxplot presentation of individual species, it allows
# to draw comparison at a very high level between the flowers, but would need to be further broken down 
# to be able to use the visualized data for prediction purposes
g=sns.catplot(data=iris2, kind="box", x="Species",y=variables[0])
plt.title("Iris Boxplot 1", c="Blue", size=10)
plt.savefig('Iris_BP_by_Species1.png')
plt.close()

g=sns.catplot(data=iris2, kind="box", x="Species",y=variables[1])
plt.title("Iris Boxplot 2", c="Blue", size=10)
plt.savefig('Iris_BP_by_Species2.png')
plt.close()

g=sns.catplot(data=iris2, kind="box", x="Species",y=variables[2])
plt.title("Iris Boxplot 3", c="Blue", size=10)
plt.savefig('Iris_BP_by_Species3.png')
plt.close()

g=sns.catplot(data=iris2, kind="box", x="Species",y=variables[3])
plt.title("Iris Boxplot 4", c="Blue", size=10)
plt.savefig('Iris_BP_by_Species4.png')
plt.close()
# The heatmap is very useful when trying to establish correlation between variables. 

sns.heatmap(iris2.corr(), annot=True, cmap="Purples")
plt.title("Iris Attributes - Heatmap", c="Blue", size=15)
plt.savefig('Iris_Heatmap.png')
plt.close()





