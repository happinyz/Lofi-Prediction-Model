# Lofi Genre Predictor
- Developed a tool that predicts if a certain track on Spotify is part of the lofi genre.
- Analyzed over 2500 songs of various genres on Spotify, taken from Spotify's numerous genre-specific playlists.
- Used [track audio features](https://developer.spotify.com/documentation/web-api/reference/tracks/get-audio-features/) provided by Spotify API as predictors; fit using logistic regression models.
- Built a client facing API using flask

## Defining the Lofi Genre


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
