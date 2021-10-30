from tkinter import *
from PIL import ImageTk, Image
import os
import subprocess

def b1handler():
    os.system('python Pong/pong.py')

def b2handler():
    subprocess.Popen('python car/main.py', shell=True)
    subprocess.Popen('python car/pose.py',shell=True)
def b3handler():
    subprocess.Popen('python SpaceShooter/main.py', shell=True)
    subprocess.Popen('python SpaceShooter/pose2.py', shell=True)

root = Tk()

root.geometry("640x480")

image1 = Image.open("heading.png")
image1= image1.resize((400,100), Image.ANTIALIAS)
image1 = ImageTk.PhotoImage(image1)
label1 = Label(image=image1)
label1.place(x=100,y=10)

pong=Image.open("squat.png")
pong=pong.resize((200,200), Image.ANTIALIAS)
pong = ImageTk.PhotoImage(pong)
label_1 = Label(image=pong) 
label_1.place(x=10,y=150)
button1 = Button(root, text ="Play This", command = b1handler)
button1.place(x=50,y=350)


bicep=Image.open("bicep.png")
bicep=bicep.resize((200,200), Image.ANTIALIAS)
bicep = ImageTk.PhotoImage(bicep)
label_2 = Label(image=bicep) 
label_2.place(x=200,y=150)
button2 = Button(root, text ="Play This", command = b2handler)
button2.place(x=250,y=350)


sbend=Image.open("sbend.jpg")
sbend=sbend.resize((200,200), Image.ANTIALIAS)
sbend = ImageTk.PhotoImage(sbend)
label_3 = Label(image=sbend) 
label_3.place(x=430,y=150)
button3 = Button(root, text ="Play This", command = b3handler)
button3.place(x=480,y=350)

root.mainloop()