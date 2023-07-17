import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.image import Image
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pygame
import requests
import threading
import os
from dotenv import load_dotenv

load_dotenv()



class MusicApp(App):
    def build(self):
        layout = FloatLayout()

        # Set the background image
        background = Image(source='C:/Users/dilip/PycharmProjects/pythonProjectgit4/image-bg.jpg', allow_stretch=True, keep_ratio=False)
        layout.add_widget(background)

        # Create a label to display the song information
        self.song_label = Label(text='Now Playing: ', size_hint=(0.8, 0.1), pos_hint={'x': 0.1, 'y': 0.7})
        layout.add_widget(self.song_label)

        # Create a text input for entering the next song
        self.text_input = TextInput(hint_text='Enter the next song', size_hint=(0.6, 0.1), pos_hint={'x': 0.2, 'y': 0.5})
        layout.add_widget(self.text_input)

        # Create a button to play the next song
        next_button = Button(text='Play Next Song', size_hint=(0.4, 0.1), pos_hint={'x': 0.3, 'y': 0.3})
        next_button.bind(on_release=self.play_next_song)
        layout.add_widget(next_button)

        # Create a button to pause the currently playing song
        pause_button = Button(text='Pause', size_hint=(0.2, 0.1), pos_hint={'x': 0.1, 'y': 0.1})
        pause_button.bind(on_release=self.pause_song)
        layout.add_widget(pause_button)

        # Create a button to resume the paused song
        resume_button = Button(text='Resume', size_hint=(0.2, 0.1), pos_hint={'x': 0.7, 'y': 0.1})
        resume_button.bind(on_release=self.resume_song)
        layout.add_widget(resume_button)

        self.current_thread = None  # Store the current thread

        return layout

    def play_next_song(self, instance):
        if self.current_thread is not None and self.current_thread.is_alive():
            # If a thread is already running, don't start another one
            return

        # Set up Spotify API credentials
        client_id = os.environ['client_id_R']
        client_secret = os.environ['client_secret_R']

        # Get the track name from the text input
        track_name = self.text_input.text

        # Create a new thread for playing the next song
        self.current_thread = threading.Thread(target=self.play_song, args=(client_id, client_secret, track_name))
        self.current_thread.start()

    def play_song(self, client_id, client_secret, track_name):
        # Authenticate with Spotify API
        client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
        sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

        # Search for a track
        results = sp.search(q=track_name, type='track', limit=1)
        if len(results['tracks']['items']) > 0:
            track_uri = results['tracks']['items'][0]['uri']

            # Get the audio file URL from the Spotify API
            track_info = sp.track(track_uri)
            if 'preview_url' in track_info and track_info['preview_url']:
                audio_file_url = track_info['preview_url']

                # Create the "audio_files" folder if it doesn't exist
                folder_path = "audio_files"
                os.makedirs(folder_path, exist_ok=True)

                # Extract the file name from the audio file URL
                file_name = track_info['id'] + '.mp3'
                audio_file_path = os.path.join(folder_path, file_name)

                # Download the audio file
                response = requests.get(audio_file_url)
                with open(audio_file_path, 'wb') as file:
                    file.write(response.content)


                # Initialize Pygame mixer
                pygame.mixer.init()

                # Load the track
                pygame.mixer.music.load(audio_file_path)

                # Play the track
                pygame.mixer.music.play()

                # Update the song label with the new song information
                self.song_label.text = f'Now Playing: {track_info["name"]} by {track_info["artists"][0]["name"]}'
            else:
                self.song_label.text = 'No preview available for this track'
        else:
            self.song_label.text = 'No matching track found'

    def pause_song(self, instance):
        pygame.mixer.music.pause()

    def resume_song(self, instance):
        pygame.mixer.music.unpause()

if __name__ == '__main__':
    Window.size = (400, 600)
    MusicApp().run()
