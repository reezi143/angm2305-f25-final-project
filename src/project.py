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

# Skip Track
# def next_song():

# Rewind Track
# def previous_song():

# play next song when current song ends?



# GUI #

app = Tk()
app.title('music player⋆｡♬°⭒˚｡⋆♪')
app.geometry('375x500')
app.resizable(0, 0) # prevents resizing

app_icon = PhotoImage(file='icon.png') 
app.iconphoto(False, app_icon)


# Playlist Assets
playlist_box = LabelFrame(app, fg='gray12', text='‧₊˚♪࿐₊˚⊹playlist‧₊˚♪࿐₊˚⊹', bg='rosybrown4')
playlist_box.place(x=0, y=79, height=220, width=375)

song_listbox = Listbox(playlist_box, fg='gray12', font=('Helvetica', 11), selectbackground='antiquewhite4')

scroll_bar = Scrollbar(playlist_box, orient=VERTICAL)
scroll_bar.pack(side=RIGHT, fill=BOTH)

song_listbox.config(yscrollcommand=scroll_bar.set)

scroll_bar.config(command=song_listbox.yview)

song_listbox.pack(fill=BOTH, padx=5, pady=5)


# Title Assets
now_playing = LabelFrame(app, fg='gray12', text='₊°♬˚.⁺now playing⁺.˚♬°₊', bg='mistyrose1', width=375, height=80)
now_playing.place(x=0, y=0)

current_song = StringVar(app, value='♪˚⁺✩not playing✩⁺˚♪')

title_label = Label(now_playing, textvariable=current_song, bg='antiquewhite4', font=("Georgia", 12), width=36)
title_label.place(x=20, y=16)


# Control Panel
control_panel = LabelFrame(app, fg='gray12', text='♪˚⁺control panel⁺˚♪', bg='mistyrose3', width=375, height=202)
control_panel.place(y=300)

play_btn_img = PhotoImage(file='play.png')
play_btn = Button(control_panel, image=play_btn_img, bg='rosybrown1', width=30, height=30,
                  command=lambda: play_song(current_song))
play_btn.place(x=170, y=2)

pause_btn_img = PhotoImage(file='pause.png')
pause_btn = Button(control_panel, image=pause_btn_img, bg='rosybrown1', width=30, height=30,
                    command=lambda: pause_song())
pause_btn.place(x=170, y=72)

next_btn_img = PhotoImage(file='skip.png')
next_btn = Button(control_panel, image=next_btn_img, bg='rosybrown1', width=30, height=30,
                    command=lambda: next_song()) # doesn't work/placeholder
next_btn.place(x=220, y=36)

prev_btn_img = PhotoImage(file='prev.png')
prev_btn = Button(control_panel, image=prev_btn_img, bg='rosybrown1', width=30, height=30,
                    command=lambda: previous_song()) # doesn't work/placeholder

load_btn = Button(control_panel, text='🖤♪~load playlist~♪🖤', bg='rosybrown1', fg='gray12', font=("Georgia", 13), width=35,
                  command=lambda: load(song_listbox))
load_btn.place(x=6, y=118)


# Bottom Strip
deco_frame = LabelFrame(app, bg='rosybrown', width=375, height=24)
deco_frame.place(x=0, y=478)
    # deco_text = '⋆｡‧˚ʚ♪ɞ˚‧｡⋆'


app.mainloop() # keeps app open