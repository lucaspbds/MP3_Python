from pygame import mixer, time, USEREVENT


def playMusica(playlist):
    for music in playlist:
        mixer.music.load(music)
        mixer.music.play()
        mixer.music.set_endevent(USEREVENT)
        while mixer.music.get_busy():
            time.wait(100)

