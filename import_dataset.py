# This program is to import the IRIS dataset using sklearn
# Author Eva Czeyda-Pommersheim

import numpy as np
import matplotlib as plt
from sklearn.datasets import load_iris
import pandas as pd

data = load_iris()
df = pd.DataFrame(data.data, columns=data.feature_names)
print(df.info())
print(df.head(10))
