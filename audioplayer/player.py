import pygame
import tkinter as tkr
import os


player = tkr.Tk()
player.title('Baby Player')
player.geometry('640x840')


os.chdir("D:/VA - Baby Driver (2017)")
print(os.getcwd)
songlist = os.listdir()


VolumeLevel = tkr.Scale(player, from_=0.0, to_=1.0,
                         orient=tkr.HORIZONTAL, resolution=0.1)


"""Playlist input"""
playlist = tkr.Listbox(player, selectbackground="darkMagenta", highlightcolor='darkMagenta', selectmode=tkr.SINGLE)
print(playlist)
for item in songlist:
    pos = 0
    playlist.insert(pos, item)
    pos += 1


pygame.init()
pygame.mixer.init()


def Play():
    pygame.mixer.music.load(playlist.get(tkr.ACTIVE))
    var.set(playlist.get(tkr.ACTIVE))
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(VolumeLevel.get())
    print(pygame.mixer.music.get_volume())
    print(VolumeLevel.get())


def ExitPlayer():
    pygame.mixer.music.stop()


def Pause():
    pygame.mixer.music.pause()


def UnPause():
    pygame.mixer.music.unpause()


var = tkr.StringVar()
songtitle = tkr.Label(player, textvariable=var)


Button1 = tkr.Button(player, width=5, height=3, text="Play!", command=Play)
Button2 = tkr.Button(player, width=5, height=3, text="Stop!", command=ExitPlayer)
Button3 = tkr.Button(player, width=5, height=3, text="Pause!", command=Pause)
Button4 = tkr.Button(player, width=5, height=3, text="Unpause!", command=UnPause)


songtitle.pack()
Button1.pack(fill="x")
Button2.pack(fill="x")
Button3.pack(fill="x")
Button4.pack(fill="x")
VolumeLevel.pack(fill='x')
playlist.pack(fill='both', expand='yes')

player.mainloop()