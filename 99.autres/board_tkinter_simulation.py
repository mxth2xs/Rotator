
# imports every file form tkinter and tkinter.ttk
from calendar import c
from tkinter import *
from tkinter.ttk import *
import time
from turtle import width
from matplotlib.pyplot import fill
 
class GFG:

    def __init__(self, master = None):
        self.master = master
        self.x = 0
        self.y = 0
        self.stopVar = 0

        self.C_zoom = 2
        self.speed = 10*self.C_zoom

        # canvas object to create shape
        self.canvas = Canvas(master, width=220*self.C_zoom, height=440*self.C_zoom)
        # creating rectangle
        self.sq_dim = 0
        self.start_snake = [
            110*self.C_zoom - self.sq_dim, 
            220*self.C_zoom - self.sq_dim, 
            110*self.C_zoom + self.sq_dim, 
            220*self.C_zoom + self.sq_dim
        ]
        self.rectangle = self.canvas.create_rectangle(self.start_snake, width=10, outline='green')
        self.pause_msg = self.canvas.create_text(200, 400-20, text="", font="Arial 16 italic", fill="red")
        self.fail_msg = self.canvas.create_text(200,200-20, text="", font="Arial 16 italic", fill="red")
        self.canvas.pack()

        # draw lines
        zoom = self.C_zoom
        #x line maker
        xx = []
        x = [c*20 for c in range(22)]
        for i in range(len(x)):
            xx += [zoom* x[i], 0, zoom* x[i], zoom* 440, zoom* (x[i]+10), zoom* 440, zoom* (x[i]+10), 0 ]
        
        y = [c*20 for c in range(22)]
        yy = []
        for i in range(len(y)):
            yy += [0, zoom* y[i], zoom* 440, zoom* y[i], zoom* 440, zoom* (y[i]+10), 0, zoom* (y[i]+10) ]
        

        self.lines_X = self.canvas.create_line(xx , fill='grey')
        self.lines_Y = self.canvas.create_line(yy, fill="grey")

        self.movement()


    def movement(self):
        self.canvas.move(self.rectangle, self.x, self.y)
        self.canvas.after(120, self.movement)
        self.cur_coords = self.canvas.coords(self.rectangle)

        #If the object is moving
        if self.stopVar == 1:
            #display coordinates
            print(f"Current coords = [{self.cur_coords[0]}, {self.cur_coords[1]}]")
            
                    #if the rectangle is out of the screen.
        if (round(self.cur_coords[0]) > 220*self.C_zoom) | (round(self.cur_coords[0]) < 0) :
            #self.canvas.itemconfig(self.fail_msg, text="")
            self.x = 0
            self.y = 0
            self.stopVar = 0
            self.canvas.delete(self.rectangle)
            self.rectangle = self.canvas.create_rectangle(self.start_snake, width=10, outline='green')
            print(f"Current coords = [{self.cur_coords[0]}, {self.cur_coords[1]}] RESET")

        
        if (round(self.cur_coords[1]) >= 440*self.C_zoom):
            self.canvas.move(self.rectangle,0,-440*self.C_zoom)

        if (round(self.cur_coords[1]) <= 0) :
            self.canvas.move(self.rectangle,0,440*self.C_zoom)


     
    def left(self, event):
        self.canvas.delete(self.pause_msg)
        #if self.stopVar == 0 | self.stopVar == 1:
        self.x = -self.speed
        self.y = 0
        self.stopVar = 1
             
    def right(self, event):
        self.canvas.delete(self.pause_msg)
        #if self.stopVar == 0 | self.stopVar == 1:
        self.x = self.speed
        self.y = 0
        self.stopVar = 1
     
    def up(self, event):
        self.canvas.delete(self.pause_msg)
        #if self.stopVar == 0 | self.stopVar == 1:
        self.x = 0
        self.y = -self.speed
        self.stopVar = 1

    def down(self, event):
        self.canvas.delete(self.pause_msg)
        #if self.stopVar == 0 | self.stopVar == 1:
        self.x = 0
        self.y = self.speed
        self.stopVar = 1
 
    def pause(self, event):
        if self.stopVar == 1:
            self.x = 0
            self.y = 0
            self.stopVar = 0
            self.pause_msg = self.canvas.create_text(200, 400*self.C_zoom, text="Press any movement key to continue.", font="Arial 16 italic", fill="red")


    def reset(self, event):
        self.canvas.delete(self.rectangle)
        self.canvas.delete(self.pause_msg)
        self.canvas.delete(self.fail_msg)
        self.x = 0
        self.y = 0
        self.stopVar = 0
        self.rectangle = self.canvas.create_rectangle(self.start_snake, width=10, outline='green')


if __name__ == "__main__":
    master = Tk()
    gfg = GFG(master)

    master.bind("<KeyPress-Left>", lambda e: gfg.left(e))
    master.bind("<KeyPress-Right>", lambda e: gfg.right(e))
    master.bind("<KeyPress-Up>", lambda e: gfg.up(e))
    master.bind("<KeyPress-Down>", lambda e: gfg.down(e))
    master.bind("<KeyPress-space>", lambda e: gfg.pause(e))
    master.bind("<KeyPress-r>", lambda e: gfg.reset(e))

    # Infinite loop breaks only by interrupt
    mainloop()