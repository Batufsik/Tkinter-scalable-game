### hi!!! i made this because i really like quality of life features in programs
### and i wanted to see if i could make one of them in python
### feel free to use this for your own stuff!

import tkinter as tk

root = tk.Tk()
root.title("Scalilka")

c = tk.Canvas(root, width=300, height=300, bg="white")
c.pack(fill="both", expand=True)

torso = c.create_rectangle(110, 120, 130, 140, fill="black")
l_leg = c.create_rectangle(110, 125, 117, 145, fill="black")
r_leg = c.create_rectangle(123, 125, 130, 145, fill="black")
eye = c.create_rectangle(123, 125, 127, 129, fill="white")

character = [torso,
             l_leg,
             r_leg,
             eye
]


movespeed = 50
dir = 1

def move_right(event):
    global dir
    c.move(torso, movespeed, 0)
    c.move(l_leg, movespeed, 0)
    c.move(r_leg, movespeed, 0)
    c.move(eye, movespeed, 0)
    if dir == 0:
        c.move(eye, 9, 0)
        dir = 1

def move_left(event):
    global dir
    c.move(torso, -movespeed, 0)
    c.move(l_leg, -movespeed, 0)
    c.move(r_leg, -movespeed, 0)
    c.move(eye, -movespeed, 0)
    if dir == 1:
        c.move(eye, -9, 0)
        dir = 0

### i felt like i gained some kind of astral knowledge
### when my brain came up with this function

def upd(event):
    global info_x, info_y
    if info_x != 1:
        if info_x != root.winfo_width() or info_y != root.winfo_height():

            modifier_x = root.winfo_width()/info_x
            modifier_y = root.winfo_height()/info_y
            
            for part in character:
                ocx, ocy, ocx2, ocy2 = c.coords(part)
                c.coords(part, ocx* modifier_x, ocy* modifier_y, ocx2 * modifier_x, ocy2 * modifier_y)
            print("mods", modifier_x, modifier_y)
            print("new resolution", root.winfo_width(), root.winfo_height())
            info_x = root.winfo_width()
            info_y = root.winfo_height()
    else:
        info_x = root.winfo_width()
        info_y = root.winfo_height()




info_x = root.winfo_width()
info_y = root.winfo_height()
print("the initial resolution is, for some reason:", root.winfo_width(), root.winfo_height())



root.bind("<Left>", move_left)
root.bind("<Right>", move_right)
root.bind("<Configure>", upd)


root.mainloop()