import os
import pygame
import random
import json
import urllib.request
import tkinter
import math
import sys
from PIL import ImageTk, Image
from pypresence import Presence
global RPCDEF
RPCDEF = False
global Idle_Time
discord_presence_details = ""
minutes_listening= 0
idle_time = 0
paused = False
parent = os.path.dirname(os.path.realpath(__file__))
clock = pygame.time.Clock()
keepPlaying = True
global discord_presence_idle_time
discord_presence_idle_time = 0
global path
path = parent+"\\mp3s"
ymod = False
global current_song
global loop
loop = False
global song_playing
global full_name
global time_listening
tk = tkinter
time_listening = 0
client_id = 827672702890147890  # Fake ID, put your real one here
discord_presence_details = "listening for 0 minutes"
client_id = 827672702890147890  # Fake ID, put your real one here


def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host)  # Python 3.x
        return True
    except:
        return False

class discord_rp():
    RPC = None
    def init(self):
        if connect():
            self.RPC = Presence(client_id, pipe=0)  # Initialize the client class
            self.RPC.connect()
        else:
            self.RPC = None
        self.resetpresence()

    def resetpresence(self):
        la = "41b2ae65ce8cb5725598c3e1b60cf476"
        dt = os.path.basename(song_playing)
        if discord_presence_idle_time < 6:
            try:
                details = discord_presence_details
                self.RPC.update(large_image=la, details=dt, state=details)
            except:
                print("discord error")
    def __init__(self):
        self.resetpresence()

def htf():
    root = tk.Tk()
    root.title("Guide")
    frame = tk.Frame(root)
    frame.pack()
    frame.config(bg=bgc)
    howto = tk.Label(frame,
                     fg=fgc,
                     bg=bgc,
                     text=helppage)
    howto.config(font=10)
    howto.pack()
    root.mainloop()
with open(parent+"\\Extra files\\json files\\settings.json") as file:
    json_file=json.load(file)
    if json_file['darkmode']:
        bgc = "black"
        fgc = "white"
    elif json_file["darkmode"] == False:
        fgc = "black"
        bgc = "white"

with open(os.path.dirname(os.path.realpath(__file__))+"\\Extra files\\json files\\storage.json", 'r+') as file:
    json_file=json.load(file)
    if json_file["firststartup"] == True:
        with open('C:\\Users\\William Schroeder\\Documents\\Codes\\Python\\beathouse\\Extra files\\txt files\\fs guide.txt') as z:
            helppage = "thank you for downloading beathouse "+z.read()
            json_file["firststartup"] = False
            file.seek(0)  # <--- should reset file position to the beginning.
            json.dump(json_file, file, indent=4)
            file.truncate()
        htf()

    with open('C:\\Users\\William Schroeder\\Documents\\Codes\\Python\\beathouse\\Extra files\\txt files\\guide.txt') as file:
        helppage = file.read()


def searchandplay(tosearch, loopbool):
    for file in os.listdir(path):
        full_path = os.path.join(path, file)
        full_name = os.path.basename(full_path)

        if tosearch.lower() == full_name.lower():
            song = (os.path.join(path, full_name))
            globals()['current_song'] = song
            pygame.mixer.music.load(song)
            pygame.mixer.music.play()
            if loopbool == True:
                globals()['loop'] = True
    discord_rp()
def randnum(a, b):
    num = random.randint(a, b)
    return num


def numberofmembers(list):
    ammount = -1
    for member in list:
        ammount = ammount+1
    return(ammount)


pygame.init()
pygame.mixer.music.set_volume(0.5)



def randomsong():
    files = []
    for file in os.listdir(path):
        full_path = os.path.join(path, file)
        globals()['full_name'] = os.path.basename(full_path)
        files.append(full_path)
    if globals()['loop'] == True:
        pygame.mixer.music.load(song_playing)
        pygame.mixer.music.play()
    else:
        ammount = numberofmembers(files)
        num = randnum(0, ammount)
        member = files[num]
        globals()['song_playing'] = member
        try:
            pygame.mixer.music.load(member)
            pygame.mixer.music.play()
        except:
            print("error while playing random song")
            randomsong()
    discord_rp()
pygame.init()




def controlmenu():
    root = tk.Toplevel()
    frame = tk.Frame(root)
    frame.pack()
    path = parent+"\\Extra files\\images\\controllermapping.png"
    img = ImageTk.PhotoImage(Image.open(path))
    panel = tk.Label(root, image=img)
    panel.pack(side="bottom", fill="both", expand="yes")
    root.mainloop()
def getplaylists():
    playlists=[]
    for file in os.listdir(parent+"\\Extra files\\playlists"):
        playlists.append(os.path.basename(file))
    return(playlists)
def playlistplay(playlist):
    if playlist == "return":
        globals()["d"] = parent+"\\mp3s"
        randomsong()
    else:
        for file in os.listdir(parent+"\\Extra files\\playlists"):
            if file == playlist:
                globals()["path"] = parent+"\\Extra files\\playlists\\"+file
                randomsong()


def playsng():

        root = tk.Tk()
        frame = tk.Frame(root)
        frame.config(bg=bgc)
        root.config(bg=bgc)
        frame.pack()
        root.title("specific song menu")

        song_to_play = tk.Text(root,
                             height=1,
                             width=49,
                             fg=bgc,
                             bg=fgc)
        song_to_play.pack()
        play = tk.Button(frame,
                         bg=bgc,
                         fg=fgc,
                         text="play",
                         command=lambda: searchandplay(str(song_to_play.get("1.0",'end-1c')),True))
        play.pack(side=tk.BOTTOM)
        pwl = tk.Button(frame,
                         bg=bgc,
                         fg=fgc,
                         text="play + loop",
                         command=lambda: searchandplay(str(song_to_play.get("1.0",'end-1c')),True))
        pwl.pack(side=tk.BOTTOM)
        playable = tk.Label(frame,
                            fg=fgc,
                            bg=bgc,
                            text="Here are the file names input one to play it")
        for member in getplaylists():
            lable = tk.Label(frame,
                             bg=bgc,
                             fg=fgc,
                             text=file)
            lable.pack(side=tk.BOTTOM)
        playable.pack()
        root.mainloop()

def playlistgui():
    root = tk.Tk()
    frame = tk.Frame(root)

    root.config(bg=bgc)
    frame.config(bg=bgc)
    root.title("playlists")
    frame.pack()
    for member in getplaylists():
        label = tk.Label(frame,
                         bg=bgc,
                         fg=fgc,
                         text=member)
        label.pack(side=tk.TOP)
    play = tk.Button(frame,
                    fg =fgc,
                    bg =bgc,
                    text ="play",
                    command =lambda:playlistplay(textbox.get("1.0",'end-1c')))
    play.pack(side=tk.TOP)
    textbox=tk.Text(frame,
                    width=49,
                    height=1,
                    bg=bgc,
                    fg=fgc)
    textbox.pack(side=tk.BOTTOM)
    root.mainloop()

def menu():
    pygame.mixer.music.pause()
    root = tk.Tk()
    frame = tk.Frame(root)
    root.config(bg=bgc)
    frame.config(bg=bgc)
    root.title("menu")
    frame.pack()
    frame.config(bg=bgc)
    globals()['songplaying'] = tk.Label(frame,
                            fg=fgc,
                            bg=bgc,
                            text=os.path.basename(song_playing))
    globals()['songplaying'].pack(side=tk.TOP)
    quitcodebutton = tk.Button(frame,
                               bg=bgc,
                               fg=fgc,
                               text="Quit appilication",
                               command=sys.exit)
    quitcodebutton.pack(side=tk.RIGHT)

    closemenubutton = tk.Button(frame,
                                bg=bgc,
                                fg=fgc,
                                text="close menu",
                                command=root.destroy)
    closemenubutton.pack(side=tk.RIGHT)
    def playsng():
        root = tk.Tk()
        frame = tk.Frame(root)
        frame.config(bg=bgc)
        root.config(bg=bgc)
        frame.pack()
        root.title("specific song menu")

        songtoplay = tk.Text(root,
                             height=1,
                             width=49,
                             fg=bgc,
                             bg=fgc)
        songtoplay.pack()
        play = tk.Button(frame,
                         bg=bgc,
                         fg=fgc,
                         text="play",
                         command=lambda: searchandplay(str(songtoplay.get("1.0",'end-1c')),True))
        play.pack(side=tk.BOTTOM)
        pwl = tk.Button(frame,
                         bg=bgc,
                         fg=fgc,
                         text="play + loop",
                         command=lambda: searchandplay(str(songtoplay.get("1.0",'end-1c')),True))
        pwl.pack(side=tk.BOTTOM)
        playable = tk.Label(frame,
                            fg=fgc,
                            bg=bgc,
                            text="Here are the file names input one to play it")
        playable.pack()

        for file in os.listdir(path):
            full_path = os.path.join(parent, file)
            filename =os.path.basename(os.path.join(parent,full_path))
            play_song = tk.Label(frame,
                              bg=bgc,
                              fg=fgc,
                              text=filename)
            play_song.pack()

    playasong = tk.Button(frame,
                          fg=fgc,
                          bg=bgc,
                          text="play specific song",
                          command=playsng)

    conrtols=tk.Button(frame,
                       fg=fgc,
                       bg=bgc,
                       text="view controls",
                       command=controlmenu)
    conrtols.pack(side=tk.LEFT)
    playasong.pack(side=tk.LEFT)
    guide=tk.Button(frame,
                    fg=fgc,
                    bg=bgc,
                    text="how to guide",
                    command=htf)
    guide.pack(side=tk.LEFT)
    playlists=tk.Button(frame,
                        bg=bgc,
                        fg=fgc,
                        text="play playlists",
                        command=playlistgui)
    playlists.pack(side=tk.LEFT)
    with open(parent+"\\Extra files\\json files\\settings.json",'r+') as f:
        thing=json.load(f)
        if thing["darkmode"] == True:
            dmbg="green"
        else:
            dmbg="red"
    global darkmodeswitch
    def changedm():
        with open(parent + "\\Extra files\\json files\\settings.json", 'r+') as f:
            thing = json.load(f)
            if thing["darkmode"] == True:
                thing["darkmode"] = False
                f.seek(0)  # <--- should reset file position to the beginning.
                json.dump(thing, f, indent=4)
                f.truncate()
                darkmodeswitch.config(bg="red")

            else:
                thing["darkmode"] = True
                f.seek(0)  # <--- should reset file position to the beginning.
                json.dump(thing, f, indent=4)
                f.truncate()
                darkmodeswitch.config(bg="green")
    globals()['darkmodeswitch'] = tk.Button(frame,
                                            fg=fgc,
                                            bg=dmbg,
                                            text="darkmode(restart)",
                                            command=changedm)
    def addtolibrary(mp3file):
        mp3s = parent+"\mp3s"
        command="copy /b "+'"'+mp3file+'"'+" "+'"'+mp3s+'"'
        print(command)
        os.system(command)

    def atlbw():
        root = tk.Tk()
        frame = tk.Frame(root)
        frame.pack()
        root.config(bg=bgc)
        frame.config(bg=bgc)
        howto = tk.Label(frame,
                         fg=fgc,
                         bg=bgc,
                         text="Please type the path of the file to add it to the library")
        howto.pack(side=tk.TOP)
        pathinput = tk.Text(frame,
                             fg=fgc,
                             bg=bgc,
                             height = 1)
        pathinput.pack(side=tk.BOTTOM)
        add=tk.Button(frame,
                      fg=fgc,
                      bg=bgc,
                      text="add",
                      command=lambda: addtolibrary(pathinput.get("1.0",'end-1c')))
        add.pack(side=tk.TOP)
        root.mainloop()


    atlb = tk.Button(frame,
                     fg=fgc,
                     bg=bgc,
                     text="add to library",
                     command=atlbw)
    atlb.pack(side=tk.LEFT)

    globals()['darkmodeswitch'].pack(side=tk.RIGHT)
    def resetdiscordrp():
        discord_rp.init(discord_rp())
    resetdrp = tk.Button(frame,
                         fg=fgc,
                         bg=bgc,
                         text="Reset discord presence",
                         command=resetdiscordrp)
    resetdrp.pack(side=tk.LEFT)
    global sng
    global pl
    def editfiles(deletebool):
        playlist_verified = False
        file_verified = False
        mp3s = parent+"\mp3s"
        playlistdir = parent+"\Extra files\playlists"
        for item in os.listdir(playlistdir):
            full_name = os.path.basename(item)
            if full_name == pl.get("1.0",'end-1c'):
                playlist_verified = True
                verified_playlist = os.path.join(playlistdir, item)
        for forfile in os.listdir(mp3s):
            filename = os.path.basename(forfile)
            if filename == sng.get("1.0",'end-1c'):
                verified_file = os.path.join(mp3s,filename)
                file_verified = True
        if file_verified:
            if playlist_verified:
                cmd = "copy /b"+'"'+" "+verified_file+' "'+' "'+verified_playlist+'"'
                os.system(cmd)
                if deletebool == True:
                    delcmd = "del "+'"'+verified_file+'"'
                    os.system(delcmd)
    def playlistaddgui():
        root=tk.Tk()
        root.title("add to playlists")
        frame = tk.Frame(root)
        frame.pack()
        frame.config(bg=bgc)
        root.config(bg=bgc)
        howto = tk.Label(frame,
                         fg=fgc,
                         bg=bgc,
                         text="please input the required information")
        howto.pack(side=tk.TOP)
        plinfo = tk.Label(frame,
                          bg=bgc,
                          fg=fgc,
                          text="please input the playlist you want to move/add this song too")
        plinfo.pack(side=tk.TOP)
        globals()['pl']=tk.Text(frame,
                   fg=fgc,
                   bg=bgc,
                   height=1)
        pl.pack(side=tk.TOP)
        snginfo = tk.Label(frame,
                           fg=fgc,
                           bg=bgc,
                           text="please input the filename of the song you want")
        snginfo.pack(side=tk.TOP)
        globals()['sng']=tk.Text(frame,
                    fg=fgc,
                    bg=bgc,
                    height=1)
        sng.pack(side=tk.TOP)
        addtoplaylist = tk.Button(frame,
                                  fg=fgc,
                                  bg=bgc,
                                  text="add",
                                  command=lambda: editfiles(False))
        addtoplaylist.pack(side=tk.TOP)
        movetoplaylist= tk.Button(frame,
                                  fg=fgc,
                                  bg=bgc,
                                  text="move",
                                  command=lambda: editfiles(True))
        movetoplaylist.pack(side=tk.TOP)
        root.mainloop()
    moveandadd = tk.Button(frame,
                           fg=fgc,
                           bg=bgc,
                           text="move/add songs to playlists",
                           command= lambda:playlistaddgui())
    moveandadd.pack(side=tk.LEFT)
    root.mainloop()
    pygame.mixer.music.unpause()

joysticks = []

while keepPlaying:

    for i in range(0, pygame.joystick.get_count()):
        joysticks.append(pygame.joystick.Joystick(i))
        joysticks[-1].init()
        joysticks[-1].get_name()
    if pygame.mixer.music.get_volume() < 0.046875:
        pygame.mixer.music.set_volume(0.046875)

    event = pygame.event.wait(2000)
    print("weee")
    if event.type == 0:
        if paused==True:
            idle_time = idle_time+2

        else:
            globals()['idle_time']=0
            globals()['time_listening']=globals()['time_listening']+2
            if globals()['time_listening'] == 60:
                minutes_listening = minutes_listening+time_listening/60
                globals()['time_listening'] = 0
                q=math.floor(minutes_listening)
                pre_dpd=f"listening for {q} minutes"
                globals()['discord_presence_details'] = pre_dpd
                discord_rp()
        if globals()['idle_time'] >= 60:
            globals()['discord_presence_details'] = "idle"
            discord_rp()
    else:

        if event.type == pygame.JOYBUTTONDOWN:
            if event.button == pygame.CONTROLLER_BUTTON_A:
                if paused == False:
                    paused = True
                    pygame.mixer.music.pause()
                elif paused == True:
                    minutes_listening = minutes_listening - 1
                    time_listening = 58
                    pygame.mixer.music.unpause()
                    paused = False
            if event.button == 7:
                menu()
            if event.button == pygame.CONTROLLER_BUTTON_B:
                paused = True
                randomsong()
                paused = False
            if event.button == pygame.CONTROLLER_BUTTON_X:
                if ymod == True:
                    if loop == False:
                        loop = True
                    elif loop == True:
                        loop = False
                else:
                    paused = True
                    pygame.mixer.music.play()
                    discord_rp()
                    paused = False
            if event.button == 4:
                if ymod == False:
                    print(pygame.mixer.music.get_volume())
                    pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() - 0.01)
                elif ymod == True:
                    pygame.mixer.music.set_volume(0)
            if event.button == 5:
                if ymod == False:
                    pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() + 0.01)
                elif ymod == True:
                    pygame.mixer.music.set_volume(1.0)
            if event.button == pygame.CONTROLLER_BUTTON_Y:
                ymod = True
        if event.type == pygame.JOYBUTTONUP:
            if event.button == pygame.CONTROLLER_BUTTON_Y:
                ymod = False
    if not pygame.mixer.music.get_busy():
        if paused == False:
             randomsong()