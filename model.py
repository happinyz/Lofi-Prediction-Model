import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
import statsmodels.api as sm
import pickle 

df = pd.read_csv("Lofi_features.csv")

# choose relevant columns
df.columns
df_model = df[["Is Lofi?","danceability", "energy", "loudness", "mode", "speechiness", "acousticness", "instrumentalness", "liveness", "valence", "tempo"]]

# get dummy data
df_dum = pd.get_dummies(df_model)

# train test split
x = df_dum.drop('Is Lofi?', axis = 1)
y = df_dum['Is Lofi?'].values

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 40, stratify = df_model["Is Lofi?"])

# Logistic Regression
model = sm.Logit(y, x)
model.fit().summary()

lm = LogisticRegression(max_iter = 1000)
lm.fit(x_train, y_train)
threshold = 0.5

lm.predict(x_test)

cross_lm = cross_val_score(lm, x_train, y_train, cv=10, scoring='accuracy')
print("Cross Validation Accuracy Score:", np.mean(cross_lm))

score = lm.score(x_test, y_test)
print("Test accuracy score:", score)

pickl = {'model': lm}
pickle.dump(pickl, open('model_file' + '.pickle', "wb"))

file_name = 'model_file.pickle'
with open(file_name, 'rb') as pickled:
    data = pickle.load(pickled)
    model = data['model']

model.predict(x_test.iloc[1,:].values.reshape(1,-1))

list(x_test.iloc[1,:])
