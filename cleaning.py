import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

cid = "3df68fa9fe484d5486751e473ef32953"
secret = "16d6f9b6225d4c67a02852e129b6ea14"

creds = SpotifyClientCredentials(client_id = cid, client_secret = secret)
sp = spotipy.Spotify(client_credentials_manager = creds)
sp.trace = False

df = pd.read_csv('Lofi_features.csv')

song_names = []
artist_names = []
album_genre = []
i = 1
for track in df["id"]:
    song_names.append((sp.track(track))["name"])
    artist_names.append(sp.track(track)["artists"][0]["name"])
    album_genre.append(sp.artist(sp.track(track)["album"]["id"]))
    print("Iteration", i)
    i += 1

columns = list(df.columns)
columns = [columns[-1]] + columns[:-1]
df = df[columns]

df.drop(["type", "id", "uri", "track_href", "analysis_url"], axis = 1, inplace = True)

df["Song Name"] = song_names
df["Artist Names"] = artist_names
df["Artist Genre"] = artist_genre

columns = ["Song Name", "Artist Names", "Artist Genre", "danceability", "energy", "key", "loudness", 
           "mode", "speechiness", "acousticness", "instrumentalness", "liveness", "valence", "tempo",
           "duration_ms", "time_signature"]

df = df[columns] 

df.to_csv("Lofi_features.csv", index = False)

