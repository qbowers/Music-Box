import vlc

play_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

Instance = vlc.Instance()
player = Instance.media_player_new()

Media = Instance.media_new(play_url)
Media.get_mrl()

player.set_nedia(Media)
player.play()