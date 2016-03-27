from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfilename
from util import * 

master = Tk()

tracklist = []
global n_song
n_song=0
global cover
cover = open("./tapes/cover.jpg",'rb').read()

def addTrackCallback():
	global n_song
	n_song+=1
	filename = askopenfilename()
	tracklist.append(filename)
	name = filename.split("/")[-1]
	print(name)
	songslist.insert('', 'end', text=str(n_song), values=(name,))
	
def createCallback():
	global cover
	create_mix(tracklist, cover)


songslist = Treeview(master)
songslist['columns']=("song")
songslist.column("#0", width=25, anchor="w")
songslist.column("song", width=200)
songslist.heading("#0", text="#")
songslist.heading("song", text="Song File name")
ysb = Scrollbar(orient=VERTICAL, command= songslist.yview)
songslist['yscroll'] = ysb.set

ysb.grid(row=0, column=3, sticky=NS)
songslist.grid(row=0, column=0,columnspan=2)


add = Button(master, text='add', command=addTrackCallback)
add.grid(row=1, column=0)

createBtn = Button(master, text='create', command=createCallback)
createBtn.grid(row=1, column=1)

mainloop()