#billboard charts api (https://github.com/guoguo12/billboard-charts), and 
#spotipy (https://spotipy.readthedocs.io/en/latest/)

from config import CLIENT_ID, CLIENT_SECRET
import billboard
import spotipy
from spotipy.oauth2 import SpotifyOAuth


# credentials
def credentials():
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(username='truetiming',
                                                   client_id=CLIENT_ID,
                                                   client_secret=CLIENT_SECRET, 
                                                   redirect_uri='http://localhost:8888/callback',
                                                   scope='playlist-modify playlist-modify-public'))
    return sp

    
def chartdata():
    """Creates easily traversible chart list"""
    chart = billboard.ChartData('hot-100')
    chart_data = []
    for song in chart:
        song_data = (song.title, song.artist)
        chart_data.append(song_data)
    
    return chart_data


def spotify_tracklist():
    """returns track ids for each song"""
    sp = credentials()
    chart = chartdata()
    trackid_list = []
    #find a way to get track IDS
    for track in chart:
        searchQuery = track[0]
        searchResults = sp.search(q=searchQuery, limit=1, type='track', market="US")
        trackid_list.append(searchResults['tracks']['items'][0]['uri'])
    return trackid_list


def create_playlist():
    """create the playlist thats gonna be used"""
    sp = credentials()
    sp.user_playlist_create('truetiming', name='Billboard Hot 100')


def grab_playlist():
    """grab the newly created playlist"""
    sp = credentials()
    playlists = sp.current_user_playlists()
    for playlist in playlists['items']:
        if playlist['name'] == 'Billboard Hot 100':
            playlist_id = playlist['uri']
    return playlist_id
    

def add_tracks():
    """add all tracks to the playlist"""
    sp = credentials()
    tracks = spotify_tracklist()
    playlist_id = grab_playlist()
    sp.user_playlist_add_tracks('truetiming', playlist_id, tracks)


if __name__ == "__main__":
    create_playlist()
    add_tracks()