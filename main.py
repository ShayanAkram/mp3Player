from tkinter import *
import pygame
from PIL import Image, ImageTk
from tkinter import filedialog

pygame.mixer.init()
is_paused = 0
new_list = []


def play_song():
    path = str(song_list.get(ACTIVE))
    pygame.mixer.music.load(path)
    pygame.mixer.music.play(0)


def pause_song():
    global is_paused
    if not is_paused:
        pygame.mixer.music.pause()
        is_paused = 1
    else:
        pygame.mixer.music.unpause()
        is_paused = 0


def stop_song():
    pygame.mixer.music.stop()
    song_list.selection_clear(ACTIVE)


def load_song():
    global new_list
    selection = filedialog.askopenfilename(
        title="Select", initialdir="C:", filetypes=[("mp3 files", "*.mp3")], multiple=True)
    new_list = list(selection)
    for i in range(len(new_list)):
        song_list.insert(i + 1, new_list[i])


top = Tk()

top.geometry("400x350")
top.resizable(0, 0)
top.title('Mp3 Player')

load = Image.open("bg.jpg")
new_load = load.resize((400, 350))
bg = ImageTk.PhotoImage(new_load)

canvas1 = Canvas(top)
canvas1.place(relx=0, rely=0, relwidth=1, relheight=1)
# Display image
canvas1.create_image(0, 0, image=bg, anchor="nw")

scrollbar = Scrollbar(top, bg='#fcc')

lbl = Label(
    top, text="Mp3 Player", bg='black', fg='white', font=([12]))

song_list = Listbox(top, yscrollcommand=scrollbar.set, bg='#cfc')

scrollbar.config(command=song_list.yview)

play_img = PhotoImage(file='play.png')
pause_img = PhotoImage(file='pause.png')
stop_img = PhotoImage(file='stop.png')

play = Button(top, image=play_img, height=35, width=35, command=play_song)
pause = Button(top, image=pause_img, height=35, width=35, command=pause_song)
stop = Button(top, image=stop_img, height=35, width=35, command=stop_song)
load = Button(top, text="Load Songs", bg="#ccf", padx=12, pady=10, command=load_song)

scrollbar.place(relx=0.95, rely=0.2, relwidth=0.05, relheight=0.35)
lbl.place(relx=0.35, rely=0.1)
song_list.place(relx=0.0, rely=0.2, relwidth=0.95, relheight=0.35)
play.place(relx=0.25, rely=0.6)
pause.place(relx=0.45, rely=0.6)
stop.place(relx=0.65, rely=0.6)
load.place(relx=0.38, rely=0.74)

top.mainloop()
