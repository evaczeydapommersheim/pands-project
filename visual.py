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
# defining a function to do the plotting for all 4 features and outputting into a subplot
def histplot(x):
    
    plt.hist(iris2[x])
    plt.title(x, size = 14, c="Blue")   #setting the subtitles for each subplot
    plt.xlabel("cm", size=10)           #Labelling the axis
    plt.ylabel("Count", size=10)
    plt.xticks(size = 10)               #Setting the text size for the axis
    plt.yticks(size = 10)
    plt.subplots_adjust(left=0.1,
                    bottom=0.1, 
                    right=0.9, 
                    top=0.9, 
                    wspace=0.5, 
                    hspace=1.0)            #adjusts spacing to make the subplots more legible

# APPLYING THE FUNCTION TO PLOT INDIVIDUAL HISTOGRAMS

plt.subplot(2,2,1)                         #set the number of (rows, columns, location) of each plot Top left
histplot("Sepal Length")

plt.subplot(2,2,2)                          #Top right
histplot("Sepal Width")

plt.subplot(2,2,3)                          #Bottom left
histplot("Petal Length")

plt.subplot(2,2,4)                          #Bottom right
histplot("Petal Width")

plt.savefig("Histogram_by features.png")    # save output image to png file
plt.close()                                 # Close the plotting

# SCATTER plots for each pair of the variables using Seaborn 
# DEFINING A FUNCTION TO PLOT THE DESIRED GRAPH
def scatter(x, y):
    sns.set_context("notebook")
    custom_palette=["red","green","purple"]
    sns.set_palette(custom_palette)
    g=sns.relplot(data=iris2, kind="scatter", hue="Species", x=x, y=y, height=5)
    g.set(xlabel=x, ylabel=y)
    sns.move_legend(g, loc="upper center", bbox_to_anchor=(.5, .9), ncol = 3)
    plt.title('Iris Data Scatter Plot', color = 'blue', size = 15, y = 1.2)
    plt.tight_layout()
    
# APPLYING THE FUNCTION TO PLOT INDIVISUAL SCATTER PLOTS
scatter("Sepal Length", "Sepal Width")
plt.savefig('Iris_ScatterPlot1.png')
plt.close()

scatter("Petal Length", "Petal Width")
plt.savefig('Iris_ScatterPlot2.png')
plt.close()

scatter("Petal Length", "Sepal Length")
plt.savefig('Iris_ScatterPlot3.png')
plt.close()

scatter("Sepal Width", "Petal Width")
plt.savefig('Iris_ScatterPlot4.png')
plt.close()


# Create a matrix of plots using Seaborn PairGrid solution
# Provides a faster and more comprehensive summary of the individual pair plots
# Helps understanding the data through clear visualization

# This is to separate the attribute variables into a list
features = ['Sepal Length', 'Sepal Width','Petal Length','Petal Width']

# Use of PAIRGRID setting diagonal plots to be histograms which will provide a distribution plot of each variable
# Chose scatterplot to plot each individual data by the species of the flower

g = sns.PairGrid(data=iris2, hue = "Species", vars = features, height=5, aspect=5/5) #hue is to group the data by different colours for the 3 species
g.map_diag(sns.histplot)    #diagonal plots to be histograms
g.map_offdiag(sns.scatterplot)  #other plots to be scatter plots
g.add_legend()      # add legend to understand the colours
g.fig.suptitle("Iris Data PairGrid Plot")   #add title to the pairplot
plt.tight_layout()
plt.savefig('Iris_Features_PairPlot.png')   #save image to png file
plt.close()

# BOXPLOT presentation of individual species, it allows
# to draw comparison at a very high level between the flowers.

g=sns.catplot(data=iris2, kind="box", x="Species",y=features[0])
plt.title("Iris Boxplot 1", c="Blue", size=15)
plt.xticks(size=10)
plt.yticks(size=10)
plt.tight_layout()
plt.savefig('Iris_BP_by_Species1.png')
plt.close()

g=sns.catplot(data=iris2, kind="box", x="Species",y=features[1])
plt.title("Iris Boxplot 2", c="Blue", size=15)
plt.xticks(size=10)
plt.yticks(size=10)
plt.tight_layout()
plt.savefig('Iris_BP_by_Species2.png')
plt.close()

g=sns.catplot(data=iris2, kind="box", x="Species",y=features[2])
plt.title("Iris Boxplot 3", c="Blue", size=15)
plt.xticks(size=10)
plt.yticks(size=10)
plt.tight_layout()
plt.savefig('Iris_BP_by_Species3.png')
plt.close()

g=sns.catplot(data=iris2, kind="box", x="Species",y=features[3])
plt.title("Iris Boxplot 4", c="Blue", size=15)
plt.xticks(size=10)
plt.yticks(size=10)
plt.tight_layout()
plt.savefig('Iris_BP_by_Species4.png')
plt.close()

# ANOTHER WAY TO PREVIOUS SOLUTION FOR BOXPLOT VISUALIZATION
# By using the pd.melt() function available in Pandas which allows to
# Change the format of the dataframe and differentiate between identifier variables (Iris Species) 
# and measured variables (Iris Features)
# Creating new dataframe "iris3" to use for visualization purposes

iris3 = pd.melt(iris2, id_vars=["Species"], value_vars=["Sepal Length", "Sepal Width", "Petal Length", "Petal Width"])

# print(iris3.loc[::50]) - printed to see how the new df looked like, excluding as it is not required for this exercise 
# print(iris3.head())  - printed to see first 5 lines, excluding as it is not required for this exercise

# BOXPLOT VISUALIZATION using "iris3" dataframe
sns.set_context("notebook")     #set the scale of the plot
sns.set_style("whitegrid")         # set gridlines to run across the graph
ax = sns.boxplot(data=iris3, x="variable", y="value", hue="Species")  # plotting data as boxplots in one plot
# Moving legend from the plot "ax" using the bbox_to_anchor function, setting the number of species
sns.move_legend(ax, "upper center", bbox_to_anchor=(.5, 1.1), ncol = 3, title=None, frameon = False) 
# Setting the title of the plot with offset of "y" to space it away from the graph
sns.despine()
plt.title("Iris - Adjacent Boxplots", y=1.1)
# using the tight layout function to ensure that all data/labels are included in the plot
plt.tight_layout()
plt.yticks(np.arange(0, 10, step=1))
plt.savefig('Iris_Adjacent_Boxplot.png')
plt.close()


# The HEATMAP is very useful when trying to establish correlation between variables. 
# Used Seaborn to generate heatmap, used formatting to make it more presentable
sns.heatmap(iris2.corr(), annot=True, cmap="Purples", linewidths=1.5, linecolor="white", xticklabels=True, yticklabels=True)
sns.set_context("notebook", font_scale=1)
plt.title("Iris Attributes - Heatmap", c="Blue", size=15)
plt.xticks(size=10)
plt.yticks(rotation=90, size=10) # rotation of ylabel text as it was not showing on the plot with the full text length
plt.savefig('Iris_Heatmap.png')
plt.close()





