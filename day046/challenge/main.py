import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth

BASE_URL = "https://www.billboard.com/charts/hot-100/"
CLIENT_ID = "ERASED_FOR_SECURITY"
CLIENT_SECRET = "ERASED_FOR_SECURITY"

date = input("Which year you want to travel on? Type date in this format YYYY-MM-DD: ")
response = requests.get(f"{BASE_URL}{date}")
response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')
song_tags = soup.select(selector="li h3", id="title-of-a-story")
song_titles = [song.getText().strip() for song in song_tags[:-7]]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://example.com/callback",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="cache.txt"
    )
)
user_id = sp.current_user()["id"]

song_uris = []
year = date.split("-")[0]
for song in song_titles:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
