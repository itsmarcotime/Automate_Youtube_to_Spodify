from youtube_client import YoutubeClient
from spodify_client import SpotifyClient

def run():
    # get a list of our playlists from youtube
    youtube_client = YoutubeClient('./creds/client')
    spotify_client = SpotifyClient(os.getenv'SPOTIFY_AUTH_TOKEN')
    playlists = youtube_client.get_playlists()

    # ask which playlist we want to get the music videos from
    for index, playlist in enumerate(playlists):
        print(f"{index}: {playlist.title}")

    choice = input("Enter your choice: ")
    chosen_playlist = playlists[choice]
    print(f"You selected: {chosen_playlist.title}")

    # for each video in the playlist, get the song information from Youtube
    songs = youtube_client.get_videos_from_playlist(chosen_playlist.id)
    print(f"Attempteing to add {len(songs)}")

    # search for the songs on spotify
    for song in songs:
        spotify_song_id = spotify_client.search_song(song.artist, song.track)
        if spotify_song_id:
            added_song = spotify_client.add_song_to_spotify(spotify_song_id)
            if added_song:
                print(f"Added {song.artist}")

if __name__ == '__main__':
    run()