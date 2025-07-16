from playsound import playsound

import tools

import tkinter as tk
from tkinter import *

animation1 = 1
animation2 = 1
a=1
b=1
click = 1
setter1 = -210
setter2 = 510
setter3 = 80
setter4 = 630
stage1 = ""
stage2 = ""
EcoOut = ""
txt = ""
key = ""
log2= ""

frm = tk.Tk()
frm.geometry('500x710')
tools.tkcenter(frm)
frm.config(bg="#140620")
frm.title("Caesar Cipher Algorithm")

def pSelect(event):
    global click
    click += 1

    def pOn():
        plus.config(text=" - ")
        textarea.place(x=210,y=160)

    def pOff():
        plus.config(text=" + ")
        textarea.place_forget()

    if click % 2 == 0:
        pOn()
    else :
        pOff()

def encrypt():
    global stage1
    global txt
    global key
    global EcoOut
    global log2
    for char in txt:
        if char == ' ':
            stage1 += char
        elif char.isupper():
            stage1 += chr((ord(char) + int(key) - 65) % 26 + 65)
        else:
            stage1 += chr((ord(char) + int(key) - 97) % 26 + 97)

    EcoOut = stage1
    log2 = EcoOut
    result.config(text=EcoOut)
    result.place(x=280, y=365)
    if len(EcoOut) > 6 :
        result.config(font=("Minecraftia", 18))
        result.place(x=220, y=365)
    stage1 =""
    Ec["state"] = DISABLED
    Dc["state"] = NORMAL
    result.config(fg="red")
    playE()


def Dccrypt():
    playD()
    global EcoOut
    global txt
    global key
    global stage2
    global log2

    for char in EcoOut:
        if char == ' ':
            stage2 += char
        elif char.isupper():
            stage2 += chr((ord(char)-int(key)-65)%26 +65)
        else:
            stage2 += chr((ord(char)-int(key)-97)%26 +97)

    DcoOut = stage2
    result.config(text=DcoOut)
    result.place(x=280, y=365)

    if len(DcoOut) > 6 :
        result.config(font=("Minecraftia", 18))
        result.place(x=220, y=365)
    stage2 =""
    Dc["state"] = DISABLED
    Ec["state"] = NORMAL
    result.config(fg="#24E53E")

    a = open("S0urce.txt", "a")
    a.write(txt+"<--(\""+key+"\")-->"+log2+"\n")
    a.close()
    log()


def set1PosYE():
    global setter1
    if setter1 != 0 :
        setter1 += 2
        panel.place(x=setter1 ,y=80)#x=120,y=210
        frm.after(10, set1PosYE)
        frm.update()
        if setter1 == 0:
            plus["state"] = NORMAL
            Ec["state"] = NORMAL



def playE():
    playsound('Sound Effect/sh2-recieve-item.mp3')
def playD():
    playsound('Sound Effect/192.wav')


pp = PhotoImage(file='Artboard – 1.png')
panel = tk.Label(frm,image = pp,bg="#140620",bd=10,width=370,height=600)
#panel.place(x=0,y=80)
plus = tk.Button(frm, text=" + ",font=("Vermin Vibes 1989",18 ),fg='white', pady=2,bg='#222222')
plus.bind("<Button-1>",pSelect)
plus.place(x=160,y=160)
plus["state"] = DISABLED
set1PosYE()

open_button = tk.Button(frm,text='Clear',font=("Vermin Vibes 1989",15 ),fg='#24E53E', pady=8,bg='#222222',command =lambda :[clear()])


mainT = tk.Label(frm, text="Caesar  Cipher \n Algorithm", font=("Metal Gear", 24),bg="#140620",fg="white" )
mainT.place(x=100,y=3)

textarea = tk.Entry(frm, width=20, font=("Arial", 18), borderwidth=3, relief="groove",
                 highlightcolor="white",bg='#222222',fg="white")

keyarea = tk.Entry(frm, width=2, font=("Arial", 18), borderwidth=3, relief="groove",highlightcolor="white",bg='#222222',fg="white",justify='center')
keyarea.place(x=165,y=370)

result = tk.Label(frm,font=("Minecraftia", 24),bg="#140620",fg="white" )

def input():
    global txt
    global key

    txt = textarea.get()
    key = keyarea.get()


def set2PosYE():
    global setter3
    if setter3 != 210 :
        setter3 += 5
        Ec.place(x=120 ,y=setter3)#x=120,y=210
        frm.after(60, set2PosYE)
        frm.update()


def set1PosYD():
    global setter2
    Dc.place_forget()
    if setter2 != 645 :
        setter2 += 5
        Dc.place(x=120 ,y=setter2)#x=120,y=510
        frm.after(30, set1PosYD)
        frm.update()


def set2PosYD():
    global setter4
    if setter4 != 510 :
       setter4 -= 5
       Dc.place(x=120 ,y=setter4)#x=120,y=510
       frm.after(60, set2PosYD)
       frm.update()

def clear():
    text.delete('1.0', END)
    f = open('S0urce.txt', 'r+')
    f.truncate(0)

def log():
    f = open("S0urce.txt", "r")
    text.delete('1.0',END)
    text.insert('1.0', f.readlines())
    text.place(x=20, y=680)
    open_button.place(x=380, y=635)
    frm.geometry('500x835')


text = tk.Text(frm, height=9,width=55,bg="black",fg="#24E53E",state=NORMAL,font=("Courier New",10 ))
#keyboard.add_hotkey('ctrl, 1', lambda: encrypt())


Ec = tk.Button(frm, text="Encrypt",font=("Vermin Vibes 1989",22 ),fg='red', pady=8,bg='#222222', command =lambda :[input(),encrypt(),])
Ec.place(x=120,y=210)
Ec["state"] = DISABLED

Dc = tk.Button(frm, text="Decrypt",font=("Vermin Vibes 1989",22 ),fg='#24E53E', pady=8,bg='#222222',command =lambda :[Dccrypt()])
Dc.place(x=120,y=510)
Dc["state"] = DISABLED



frm.mainloop()





#
#
# folder = 'D:/MotherBase/Cipher'
# fileList = [f for f in os.listdir(folder) if f.endswith('.txt')]
# fileCombo = ttk.Combobox(frm, values=fileList, state='readonly',height=15)
#fileCombo.place(x=20,y=110)
#fileCombo.bind('<<ComboboxSelected>>', file())



# # open button
# open_button = ttk.Button(frm,text='Open a File',command=select_file)
#
# open_button.place(x=50,y=370)
