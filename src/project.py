import requests
from tkinter import filedialog
from tkinter import *
import pygame
import os

pygame.mixer.init()

# Load Music
def load(listbox):
    os.chdir(filedialog.askdirectory(title='choose playlist~♡⊹♬₊⋆'))
    listbox.delete(0, END)

    tracks = os.listdir()

    for track in tracks:
        listbox.insert(END, track)