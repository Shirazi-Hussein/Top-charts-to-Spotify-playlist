#billboard charts api (https://github.com/guoguo12/billboard-charts), and 
#spotipy (https://spotipy.readthedocs.io/en/latest/)

import billboard
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from config import CLIENT_ID, CLIENT_SECRET

client_credentials_manager = SpotifyClientCredentials(CLIENT_ID, CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def chartdata():
    """Creates easily traversible chart list"""
    chart = billboard.ChartData('hot-100')
    chart_data = []
    for song in chart:
        song_data = (song.title, song.artist)
        chart_data.append(song_data)
    
    return chart_data


def spotify_search():
    """returns track ids for each song"""
    scope = 'playlist-modify-private'
    chart = chartdata()
    trackid_list = []
    #find a way to get track IDS
    for track in chart:
        searchQuery = track[0]
        searchResults = sp.search(q=searchQuery, limit=1, type='track', market="US")
        trackid_list.append(searchResults['tracks']['items'][0]['uri'])
    return trackid_list

spotify_search()
