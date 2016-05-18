
import spotipy
from  spotipy import util
import unittest
import pprint
import sys
import simplejson as json

'''
All tests require authentication. Hence, this is checked in the main function.

'''

class TestSpotipy(unittest.TestCase):

    '''
    Making sure latest releases are returned when a Get A List of New Releases call is made
    '''
    def test_new_releases(self):
        releases = spotify.new_releases()
        self.assertTrue(len(releases['albums'])>0)

    '''
    Making sure the Get A List of New Releases call fails without a token
    '''
    def test_new_releases_fails_without_token(self):
        self.assertFalse(len(token)==0)

    '''
    Making sure the specified fields are returned when a Get a List of Featured Playlists call is made
    '''
    def test_featured_playlists(self):
        featuredplaylists = spotify.featured_playlists()
        self.assertTrue(len(featuredplaylists['playlists'])>0)

    '''
    Current User's Profile
    '''
    def test_current_user(self):
        currentuser = spotify.current_user()
        self.assertTrue(currentuser['id'] == username)
    
    '''
    Current User's Saved Tracks
    '''
    def test_current_user_saved_tracks(self):
        tracks = spotify.current_user_saved_tracks()
        self.assertTrue(len(tracks['items'])>0)

    '''
    Current User's Saved Albums
    '''
    def test_current_user_saved_albums(self):
        albums = spotify.current_user_saved_albums()
        self.assertTrue(len(albums['items'])>0)
    

if __name__ == '__main__':
    if len(sys.argv) > 1:
        username = sys.argv[1]
        del sys.argv[1]

        scope = 'playlist-modify-public '
        scope += 'user-library-read '
        scope += 'user-follow-read '
        scope += 'user-library-modify '
        scope += 'user-read-private '
        scope += 'user-top-read'

        token = util.prompt_for_user_token(username, scope)
        spotify = spotipy.Spotify(auth=token)
        spotify.trace = False
        unittest.main()
    else:
        print("Usage: %s username" % (sys.argv[0],))
