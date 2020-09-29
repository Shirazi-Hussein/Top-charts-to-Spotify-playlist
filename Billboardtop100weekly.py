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
    track_list = []
    #find a way to get track IDS
    for track in chart[1:2]:
        searchQuery = track[0] + ' ' + track[1]
        searchResults = sp.search(q=searchQuery, limit=1, type='track', market="US")
# =============================================================================
#         results = sp.search(q='artist:' + track[1] + ' track:' + track[0],
#                                  type='track', limit=1)
# =============================================================================
        print(searchResults)


spotify_search()
