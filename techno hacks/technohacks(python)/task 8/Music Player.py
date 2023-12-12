from tkinter import *
import pygame

def play_music():
    pygame.mixer.init()
    pygame.mixer.music.load("song.mp3")
    pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

def main():
    root = Tk()
    root.title("Music Player")

    play_button = Button(root, text="Play", command=play_music)
    play_button.pack()

    stop_button = Button(root, text="Stop", command=stop_music)
    stop_button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()