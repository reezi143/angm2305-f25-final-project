import requests
from tkinter import filedialog
from tkinter import *
import pygame
import os

pygame.mixer.init()

is_paused = False

# Load Music
def load(listbox):
    os.chdir(filedialog.askdirectory(title='choose playlist~♡⊹♬₊⋆'))
    listbox.delete(0, END)

    tracks = os.listdir()

    for track in tracks:
        listbox.insert(END, track)

# Play Music
def play_song(song_name: StringVar):
    song_name.set(song_listbox.get(ACTIVE))
    global is_paused

    if not is_paused: # plays indicated song
        pygame.mixer.music.load(song_listbox.get(ACTIVE))
        pygame.mixer.music.play()
    else: # unpauses currently playing song
        pygame.mixer.music.unpause()
        is_paused = False

# Pause Mong
def pause_song():
    global is_paused
    pygame.mixer.music.pause()
    is_paused = True