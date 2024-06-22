"""Color to Word 1.0.0 - Convert colors to words.
Copyright (C) 2024  Fonazza-Stent

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>."""

import tkinter as tk
from tkinter import *
from tkinter.filedialog import asksaveasfilename
from tkinter import colorchooser
import csv
from math import sqrt
import linecache

def read_colorlist():
    global RGBlist
    filename='wordcolor.txt'
    """csvfile=open(filename,'r')
    colorstring=csvfile.read()
    csvfile.close()"""
    RGBlist=[]
    RGB=[]
    csvfile=open(filename,'r')
    reader_obj=csv.reader(csvfile)
    for line in reader_obj:
        RGBlist.append(line)
    csvfile.close()

#create main window
def create_main_window():
    global top
    global root
    img=b'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAABuvAAAbrwFeGpEcAAAAB3RJTUUH5gQIDDglaXxNyAAAABl0RVh0Q29tbWVudABDcmVhdGVkIHdpdGggR0lNUFeBDhcAAASCSURBVFjDxZfLbxNXFMZ/c2fsscfxK7XzsPOAJC6BAHkRGpDaCnVFN62oFFVqpSB10Q3brtj2L0DKhmWXbLJHlboAKhVFbUOh0CaUQJqHkQMmTjy2x77ThcGxcWKPI7U90pU8d+6c+/k75zvnXsW2bZv/0TSnC20bHjxM8/ujDG63YGoiTDxmACClzW+LT3nyOIXfrzNx9ijhcNvhAMzPz3Pt2rW6hduls6wWTlaeFSRDnu9xK39jbQ1T3OzYe+cq4RlaAJGv8TE7O8vly5cbA7AsC02rJ2an2AtC7DGCIM8AhrZJ4VU7AlHlRKBYHai+jRofhUKhOQPFYhERDJLp6OCjkRFmL16kMxrll3u73Huw+zocNt9+dxfDnUN36xQMyRfffFDxIaXNx598jaqV+PHWT9yYu0nRtYtlWXUAxNsTOeDh6Chj587RNTLCQiqF7vUyORYhHHShKAqKotDl3SbS9gRd1wkeSeLWtcq7U2Mx+vq7UG0vpCNMjb1P6OEwxZSvOQOvdJ12j4fheByArWyWx8kkx+NxZj7rIZnMoao2t3+4hYIKqLjdJp9/+R6bG2l8bTrRjiAAv95eRpYkvYluVro3WLu7y27GxOf3HgwgJyUT0ShqVbyLUgLg0gQ9cQMpJR7dVfOdx+vmyEBHzVx2pxxzoQri41HS6ztYhWLjEHizWToDgcqzSwj6I5E66nRdrxn72ZHje4DaY0ECXTr+kK9xCL66dIkXuRx/JJO4VJXTPT0EvN465263e092irIvgNHpIdy6xsbTF/QNR3n39IeoqqgHYNs2K7srvCy8JKJH6Iv20h+NNiwg1f/6IACqKjh5ZoCTZwbK6rBKZP5KgrQxeiOoulYGcCd1h8XMYuXD6dA0k+2TDQFUMyCEaFrxSvki6/M/Y21ly+ACOvFLEwizZNZsDrDwaoGSXWrKQLMcqLbM8mZlc4DSdp7tR+to+/UiaUts2wbFGQMHhaDG51vZX2bFQhiawTHjWG3y+EfRROM+ZVlWZRSLxaYAfH0RFFEL1Hc0Ws6BC50XiG3HSOVTdHo6SfgTTR2aplmVbGrT9fo7bXR9Okp6cRWkTeBUHKM7XAagKiongida6uO5XK4lAADe7hDe7lC9DEtYrHKfHVKEiRNjGAXhGMB+3XNf29mB5eXy78FB8PvLAO5zk5esAJDiT7KkSXDecQiqE/JgGWTgxg14A3xhAWZmECaZyuZvbJ17SGRTBqpHU1te3tscIJ+HpSU0QX38VDQUFMchcHym22dO6BjEGKttIkw3BWCaZmXk8/nmAAYHwVXVQTUNBgfLOZDgPO30kiVNgCghultSgaMkDAZhZgaWlspsJBIQfi1DBYUIfUDfoWTopBQDEArB1NThjuWNVGAYxr9/L6ip4aVSDQOZTOa/BfC29HK5HPl83nkoGh3JnNjz58/r6sDa2tqhGGgJgJSS1dVVrl+/XiND0zSZm5vj2bNnSClbrQ/O7OrVq/bk5KStqmrDMT4+bl+5csWpW1txejtu9RLt5JDSUhI6ddiq/QMeSxpTDyo7FgAAAABJRU5ErkJggg=='
    root= tk.Tk()
    top= root
    top.geometry("620x300")
    top.title("Color to Word")
    top.resizable(0,0)
    favicon=tk.PhotoImage(data=img) 
    root.wm_iconphoto(True, favicon)

#ColorDisplayFrame
def color_display_frame():
    global ColorDisplayFrame
    global ColorMatchLabel
    global WordBox
    #global ColorMatchFrame
    #global ColorMatchLabel
    ColorDisplayFrame= Frame(top)
    ColorDisplayFrame.place(x=20, y=20, height=220, width=280)
    ColorDisplayFrame.configure(relief='groove')
    ColorDisplayFrame.configure(borderwidth="2")
    ColorDisplayFrame.configure(relief="groove")
    ColorDisplayFrame.bind("<Button-1>",pick_color_frame)
    
    ColorDisplayLabel=Label(top)
    ColorDisplayLabel.place(x=20,y=240,height=35,width=280)
    ColorDisplayLabel.configure(text="Click to pick a color")

    WordBox=Text(top)
    WordBox.place(x=320, y=20, height=220, width=280)
  
    ColorMatchLabel=Text(top)
    ColorMatchLabel.place(x=320,y=250,height=25,width=280)
    ColorMatchLabel.configure(state="disabled")

#choose color
def pick_color():
    global color
    global R
    global G
    global B
    global RGBcolor
    global pickcheck
    global oldcolor
    global colorsave
    #RGBcolor=0
    color = colorchooser.askcolor(title ="Choose color")
    if str(color[1])!="None":
        ColorDisplayFrame.configure(bg=color[1])
        R,G,B=color[0]
        closest=closest_color((R, G, B))
        labelcolor='R:'+str(R)+' G:'+str(G)+' B:'+str(B)
        ColorMatchLabel.configure(state='normal')
        ColorMatchLabel.delete(1.0,END)
        ColorMatchLabel.insert(INSERT,labelcolor)
        ColorMatchLabel.configure(state="disabled")

def pick_color_frame(event):
    pick_color()

def closest_color(rgb):
    global word
    r, g, b = rgb
    color_diffs = []
    for color in RGBlist:
        word,cr, cg, cb = color
        cr=int(cr)
        cg=int(cg)
        cb=int(cb)
        color_diff = (sqrt((r - cr)**2 + (g - cg)**2 + (b - cb)**2))
        color_diffs.append((color_diff, color))
    color_diffs.sort()
    min_values=color_diffs[:10]
    
    #print (min_values[1][1][0])
    WordBox.configure(state='normal')
    WordBox.delete(1.0,END)
    for n in range (0, 10):
        word=min_values[n][1][0]
        R=min_values[n][1][1]
        G=min_values[n][1][2]
        B=min_values[n][1][3]
        wordcolor=word+' R:'+R+' G:'+G+' B:'+B

        WordBox.insert(INSERT,wordcolor+'\n')
    WordBox.configure(state='disabled')
    #return min(color_diffs)[1]



def rgb_to_hex(r,g,b):
    #return '#%02x%02x%02x' % rgb
    return "#{:02x}{:02x}{:02x}".format(r,g,b)

#convert Hex to RGB
def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

#CopyContextMenu
def create_context_menu():
    global menu
    menu = tk.Menu(root, tearoff = 0)
    menu.add_command(label="Copy", command=copy_text)
    root.bind("<Button-3>", context_menu)

def context_menu(event): 
    try: 
        menu.tk_popup(event.x_root, event.y_root)
    finally: 
        menu.grab_release()
        
def copy_text():
        WordBox.event_generate(("<<Copy>>"))

#main
def main():
    read_colorlist()
    create_main_window()
    color_display_frame()
    create_context_menu()

main()
root.mainloop()
