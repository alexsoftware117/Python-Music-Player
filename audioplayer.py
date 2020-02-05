# Imports libaries
import pygame
import tkinter as tkr
import os

# Creates the music player window
player = tkr.Tk()

# Modifies the window title and the size
player.title("Alex's Music Player")
player.geometry("300x340")

# Registers the playlist
os.chdir("C:/Music/")
songlist = os.listdir()

# Volume of song
VolumeLevel = tkr.Scale(player,from_=0.0,to_=1.0, orient = tkr.HORIZONTAL, resolution = 0.1)

# Playlist input
playlist = tkr.Listbox(player, highlightcolor="blue", selectmode = tkr.SINGLE)
print(songlist)
for item in songlist:
    pos = 0
    playlist.insert(pos, item)
    pos = pos + 1

# Action events
pygame.init()
pygame.mixer.init()

# Song name
var = tkr.StringVar()
songtitle = tkr.Label(player, textvariable=var)

# Creates function that plays audio
def Play():
    pygame.mixer.music.load(playlist.get(tkr.ACTIVE))
    var.set(playlist.get(tkr.ACTIVE))
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(VolumeLevel.get())

# Creates function that will stop the music
def ExitPlayer():
    pygame.mixer.music.stop()

# Creates function that will pause the music
def Pause():
    pygame.mixer.music.pause()

# Creates function that will unpause paused music
def UnPause():
    pygame.mixer.music.unpause()
    
# Initializes buttons
button1 = tkr.Button(player, width=5, height=3, text="PLAY", command=Play)
button2 = tkr.Button(player, width=5, height=3, text="STOP", command=ExitPlayer)
button3 = tkr.Button(player, width=5, height=3, text="PAUSE", command=Pause)
button4 = tkr.Button(player, width=5, height=3, text="UNPAUSE", command=UnPause)

# Place Widgets into the program
songtitle.pack()
button1.pack(fill="x")
button2.pack(fill="x")
button3.pack(fill="x")
button4.pack(fill="x")
VolumeLevel.pack(fill="x")
playlist.pack(fill="both", expand="yes")

player.mainloop()

# Activates the player
player.mainloop()