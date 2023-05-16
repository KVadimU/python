import tkinter as t
import random, time
#from tkinter import *

def brosok():
    x = random.choice([
        'cub1.png',
        'cub2.png',
        'cub3.png',
        'cub4.png',
        'cub5.png',
        'cub6.png'
        ])
    return x

def img(event):
    global cub1, cub2
    cub1 = t.PhotoImage(file = (brosok()))
    cub2 = t.PhotoImage(file = (brosok()))
    label1['image'] = cub1
    label2['image'] = cub2

root = t.Tk()
root.geometry('400x200')
root.title("Игра в кости. Сделай бросок!!!")
root.resizable(height = False, width = False)
root.iconphoto(True, t.PhotoImage(file = ("iconka.png")))
background_iamge = t.PhotoImage(file = ("holst.png"))
t.Label(root, image = background_iamge).pack()
#кубики
label1 = t.Label(root)
label1.place(relx = 0.3, rely = 0.5, anchor = t.CENTER )#place - место, anchor - якорь центр метки
label2 = t.Label(root)
label2.place(relx = 0.7, rely = 0.5, anchor = t.CENTER )#place - место

root.bind('<1>', img)

img('event')
root.mainloop()
