import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import config

cid = config.CID
secret = config.SECRET

creds = SpotifyClientCredentials(client_id = cid, client_secret = secret)
sp = spotipy.Spotify(client_credentials_manager = creds)
sp.trace = False

df = pd.read_csv('Lofi_features.csv')

# Create new columns with the following information:
# Song Name, Artist Name, Artist Genre

song_names = []
artist_names = []
artist_genre = []
i = 1
for track in df["id"]:
    song_names.append((sp.track(track))["name"])
    artist_names.append(sp.track(track)["artists"][0]["name"])
    artist_genre.append(sp.artist(sp.track(track)["artists"][0]["id"])["genres"])
    print("Iteration", i)
    i += 1

# columns = list(df.columns)
# columns = [columns[-1]] + columns[:-1]
# df = df[columns]

# Drop unnecessary fields and define our new fields

df.drop(["type", "id", "uri", "track_href", "analysis_url"], axis = 1, inplace = True)

df["Song Name"] = song_names
df["Artist Names"] = artist_names
df["Artist Genre"] = artist_genre
# df["Artist Genre"] = df["Artist Genre"].apply(eval)

# Make another column that determines if an artist is of the Lofi genre

lofi = [True if ('chillhop' in genre_list or 'lo-fi beats' in genre_list or 'japanese chillhop' in genre_list) else False for genre_list in df["Artist Genre"]]

df["Is Lofi?"] = lofi

# Reorder our dataset so the information is more readable

columns = ["Song Name", "Artist Names", "Artist Genre", "Is Lofi?", "danceability", "energy", "key", "loudness", 
           "mode", "speechiness", "acousticness", "instrumentalness", "liveness", "valence", "tempo",
           "duration_ms", "time_signature"]

df = df[columns]

df.to_csv("Lofi_features.csv", index = False)