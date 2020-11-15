# Lofi Genre Predictor
- Developed a tool that predicts if a certain track's author on Spotify is part of the lofi genre.
- Analyzed over 2500 songs of various genres on Spotify, taken from Spotify's numerous genre-specific playlists.
- Used [track audio features](https://developer.spotify.com/documentation/web-api/reference/tracks/get-audio-features/) provided by Spotify API as predictors; fit using logistic regression models.
- Built a client facing API using flask

## Important Things to Know
- I originally began this project to predict if a specific track would be part of the lofi genre. However, Spotify tracks do not have genre attached to them. Genres are only attached to albums and artists. I settled with predicting artist genre instead.
- I have considered the following genres to be lofi: **chillhop, lo-fi beats, japanese chillhop**
- My response variable is whether or not a track's artist was part of the lofi genre. My explanatory variables were the various track audio features.


## Code and Resources Used
**Python Version**: 3.7.9

**Packages**: Spotipy, pandas, numpy, sklearn, matplotlib, flask, json, pickle

**Web Framework Requirements**: `pip install -r requirements.txt`

**Inspiration and Data Preparation Article**: https://opendatascience.com/a-machine-learning-deep-dive-into-my-spotify-data/

**Flask Productionization**: https://towardsdatascience.com/productionize-a-machine-learning-model-with-flask-and-heroku-8201260503d2

## Spotify Track Audio Features Used as Predictors
With each track, we used the following features to fit our model:
- Danceability
- Energy
- Instrumentalness
- Liveness
- Loudness
- Mode
- Speechiness
- Tempo
- Acousticness
- Valence

## Data Cleaning
After getting the initial data from the Spotify API, I needed to clean a few parts and add some fields so that our data would be presentable and usable for our model. Here are some of the changes I made:
- Added a field for track name (taken via Spotify API)
- Added a field for artist name (taken via Spotify API)
- Added a field for artist genre (taken via Spotify API)
- Parsed lists containing genres from artist genres
- Added a field for if a track's artist is affiliated with the lofi genre

## Exploratory Data Analysis
During the EDA, I took a look at the distributions of the predictors and the value counts for the different genres present in my model playlist. Here are some highlights!

## Model Building
I split the dataset into training and testing sets with a test size of 20%. I decided to just use a logistic regression model since I had many predictors (audio features) and one qualitative response variable (Is the artist part of the lofi genre?). 

After running the model on the test set, I found that my model had an accuracy of 

## Productionization
Using the tutorial listed above, I created a flask API endpoint that takes in a request with a list of values corresponding to the relevant track audio features and returns a prediction of whether or not the song's artist is part of the lofi genre. The endpoint was hosted on a local webserver.

## Expanding and Improving on the Project
I would love to continue this project further by refining the model to give a prediction for what genre the song's artist is a part of, rather than if the artist is part of just the lofi genre. I'd also like to test out different models and see if there are any approaches that are more accurate.
