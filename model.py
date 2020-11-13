import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("Lofi_features.csv")

# choose relevant columns

df.columns

df_model = df[["danceability", "energy", "loudness", "mode", "speechiness", "acousticness", "instrumentalness", "liveness", "valence", "tempo"]]

# get dummy data
df_dum = pd.get_dummies(df_model)

# train test split
# multiple linear regression
# lasso regression
# random forest

# tune models GridsearchCV
# test ensembles