# Music Player App

This is a simple music player application built with Python and Kivy.

## Features

- Allows users to search and play songs from Spotify using the Spotify API.
- Displays the currently playing song information.
- Supports play, pause, and resume functionalities.

## Usage

1. Install the required dependencies: `pip install kivy spotipy pygame requests python-dotenv`

2. Set up your Spotify API credentials:
- Create a Spotify developer account at [https://developer.spotify.com/](https://developer.spotify.com/).
- Create a new application and obtain your client ID and client secret.
- Create a `.env` file in the project directory and add the following lines, replacing the placeholders with your actual credentials:
  ```
  client_id_R=<your-client-id>
  client_secret_R=<your-client-secret>
  ```

3. Run the application: `python main.py`

## Examples

Here's an example of the application in action:
![Screenshot (150)](https://github.com/Rithikraj7/music-player-using-kevy/assets/108055323/a763fe6f-d8cb-4cf5-adfa-98735089f174)
![Screenshot (151)](https://github.com/Rithikraj7/music-player-using-kevy/assets/108055323/f3856cac-7695-41fb-8e5a-1acc8bd91f6c)

## Acknowledgments


This program makes use of the following libraries and resources:
- Kivy: [https://kivy.org/](https://kivy.org/)
- Spotipy: [https://spotipy.readthedocs.io/](https://spotipy.readthedocs.io/)
- Pygame: [https://www.pygame.org/](https://www.pygame.org/)
- Spotify API: [https://developer.spotify.com/documentation/web-api/](https://developer.spotify.com/documentation/web-api/)

## License

This project is licensed under the [MIT License](LICENSE).


