# spotify-tests
A script that tests six basic functions in the Spotify API.

# Installation
This script uses a python module called 'spotipy', which can be installed using pip:

sudo pip-install spotipy

The script was written in Python 2.7.9.

The script can be installed by cloning this repository:

(sudo) git clone https://github.com/rishmanisation/spotify-tests/

If you don't have git installed, install git first using:

sudo apt-get install git


# Execution
Just run the script using:

python testing.py username

where your 'username' is the Spotify username that you use to login. If you use Facebook, you will have to login to the Spotify website (www.spotify.com) using Facebook, go to 'Account' and click on the tab that says 'Set device password'. Then, use the number that shows up on that page as the 'username'.


# Initial Setup
When you run the script for the first time, it might throw up an error that tells you to assign the following as environment variables:

SPOTIPY_CLIENT_ID

SPOTIPY_CLIENT_SECRET

SPOTIPY_REDIRECT_URI

To fix this, visit developer.spotify.com. There, click on the tab that says 'My Apps' and create a new 'App'. Once this is done, it should show you a window where you can edit a bunch of fields. It will also show you the Client ID and the Client Secret, and there will be an empty field where you can enter a redirect URI. Enter "http://localhost:8888/callback/" (without the quotation marks) in that field and click 'Add'. Then, go all the way down to the bottom of the page and hit 'Save'.

Open up a terminal window and type the following lines (hit Enter after typing each line):

export SPOTIPY_CLIENT_ID=the value of the Client ID field

export SPOTIPY_CLIENT_SECRET=the value of the Client Secret field

export SPOTIPY_REDIRECT_URI=http://localhost:8888/callback/

When you run the program after doing this, it will try to link to your app. Open up the link that shows up on the terminal window in a browser. It will redirect you to another URL. Just copy this URL into the terminal window and hit enter. This authentication is only required once per app.




