import os
import pygame
from mutagen.id3 import ID3
from tkinter import *






root= Tk()
root.minsize(600,400)

listofsongs =[]
realnames =[]
v= StringVar()
songlabel = Label(root,textvariable=v,width=35 )

index=0

def nextsong(event):
    global index
    index +=1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()
def prevsong(event):
    global index
    index -= 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()

def stopsong(event):
    pygame.mixer.music.stop()
    v.set("")


def updatelabel():
    global index
    global songname
    v.set(realnames[index])
    #return songname
def directorychooser():

    directory = 'C:/Users/Kithu/Desktop/NewFactory/Musik'
    os.chdir(directory)
    for files in os.listdir(directory):
        if files.endswith(".mp3"):
            realdir = os.path.realpath(files)
            audio = ID3(realdir)
            realnames.append(audio['TIT2'].text[0])
            audio2 = ID3(files)

            print("Track:"+audio2.filename )


            listofsongs.append(files)



            #print(files)

    pygame.mixer.init()
    pygame.mixer.music.load(listofsongs[0])
    pygame.mixer.music.play()
def start():
    directorychooser()
    label = Label(root, text='Music Player')
    label.pack()

    listbox = Listbox(root)
    listbox.pack()

    realnames.reverse()

    for items in realnames:
        listbox.insert(0, items)
    realnames.reverse()
    nextbutton = Button(root, text='Next Song')
    nextbutton.pack()

    previousbutton = Button(root, text='Previous Song')
    previousbutton.pack()

    stopbutton = Button(root, text='Stop Music')
    stopbutton.pack()

    nextbutton.bind("<Button-1>", nextsong)

    previousbutton.bind("<Button-1>", prevsong)

    stopbutton.bind("<Button-1>", stopsong)
    songlabel.pack()
    root.mainloop()

start()








