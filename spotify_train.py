import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

cid = "3df68fa9fe484d5486751e473ef32953"
secret = "16d6f9b6225d4c67a02852e129b6ea14"

creds = SpotifyClientCredentials(client_id = cid, client_secret = secret)
sp = spotipy.Spotify(client_credentials_manager = creds)
sp.trace = False

ids = []
features_list = []

# def get_playlist_tracks(username,playlist_id):
#     results = sp.user_playlist_tracks(username,playlist_id)
#     tracks = results['items']
#     while results['next']:
#         results = sp.next(results)
#         tracks.extend(results['items'])
#     return tracks
    
# playlist = get_playlist_tracks("1246062693","4U5UE0E4GFdFj9e6JeSPNI")

print("Fetching playlist...")

results = sp.user_playlist_tracks("1246062693","4U5UE0E4GFdFj9e6JeSPNI")
playlist = results['items']
while results['next']:
    results = sp.next(results)
    playlist.extend(results['items'])


for track in playlist:
    ids.append(track["track"]["id"])

chunks = [ids[x:x+100] for x in range(0, len(ids), 100)]

for chunk in chunks:
    features_list.append(sp.audio_features(chunk))
    
features_list = [i for sublist in features_list for i in sublist]

df = pd.DataFrame(features_list)

df.to_csv("Lofi_features.csv", index = False)
