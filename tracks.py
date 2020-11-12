# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 22:15:25 2020

@author: AlvinZ
"""
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

cid = "3df68fa9fe484d5486751e473ef32953"
secret = "16d6f9b6225d4c67a02852e129b6ea14"

creds = SpotifyClientCredentials(client_id = cid, client_secret = secret)
sp = spotipy.Spotify(client_credentials_manager = creds)
sp.trace = False

def get_playlist_tracks(username,playlist_id):
    results = sp.user_playlist_tracks(username,playlist_id)
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    return tracks
