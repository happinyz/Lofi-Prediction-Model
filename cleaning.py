import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

cid = "3df68fa9fe484d5486751e473ef32953"
secret = "16d6f9b6225d4c67a02852e129b6ea14"

creds = SpotifyClientCredentials(client_id = cid, client_secret = secret)
sp = spotipy.Spotify(client_credentials_manager = creds)
sp.trace = False

df = pd.read_csv('Lofi_features.csv')

df["Song Name"] = df["id"].apply(lambda x: (sp.track(x))["name"])

columns = list(df.columns)
columns = [columns[-1]] + columns[:-1]
df = df[columns]

df.drop(["type", "id", "uri", "track_href", "analysis_url"], axis = 1, inplace = True)

df.to_csv("Lofi_features.csv", index = False)

