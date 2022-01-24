#  William dos Santos Junqueira

from tkinter import *
from tkinter import colorchooser
from tkinter import filedialog
from PIL import ImageGrab


class App:
    def __init__(self, master):
        self.master = master
        self.master.geometry('800x600')  #  initial size
        self.master['bg'] = '#bfbfbf'

        
        self.topFrame = Frame(self.master).pack()
        self.bottomFrame = Frame(self.master).pack()


        #  Variables
        self.bgcolor = 'white'
        self.fgcolor = 'black'
        self.penwidth = 5
    

        #  Create Menu
        self.menu()
        
        #  Create Toolbar
        self.toolbar()
     
        #  Create Canvas
        self.canvas = Canvas(self.bottomFrame, width=600, height=600, bg=self.bgcolor)
        self.canvas.pack(fill='both', padx=10, pady=10, expand=True)
         
     
    def menu(self):
        #  Menu functions
        def saveFile():

            x = self.master.winfo_rootx() + self.canvas.winfo_x()
            y = self.master.winfo_rooty() + self.canvas.winfo_y()
            x1 = self.canvas.winfo_width()
            y1 = self.canvas.winfo_height()

            self.path = filedialog.asksaveasfilename(initialdir='C:/Users', title='save',
            defaultextension=".png")

            ImageGrab.grab().crop((x,y,x1,y1)).save(self.path)

        
        def clear():
            self.canvas.delete('all')


        def changeBg():
            self.bgcolor = colorchooser.askcolor(color=self.bgcolor)[1]
            self.canvas['bg'] = self.bgcolor


        #  creating menu
        menu = Menu(self.topFrame)
        self.master.config(menu=menu)

        #  menu tabs
        file_menu = Menu(menu)
        background_menu = Menu(menu)
        options_menu = Menu(menu)

        file_menu.add_command(label='save file', command=saveFile)
        background_menu.add_command(label='Background Color', command=changeBg)
        options_menu.add_command(label='Clear Board', command=clear)

        menu.add_cascade(label='File', menu=file_menu, underline=0)
        menu.add_cascade(label='Background', menu=background_menu, underline=0)
        menu.add_cascade(label='Options', menu=options_menu, underline=0)

    
    def toolbar(self):
        def verifytool():
            if self.tool == 'pen':
                self.canvas.bind('<B1-Motion>', paint)
                self.canvas.bind('<ButtonRelease-1>', reset)

            elif self.tool == 'eraser':
                self.canvas.bind('<B1-Motion>',  erase)

            self.master.after(1, verifytool)

        #  Tools  
        def pen():
            self.master.config(cursor='plus')  #  change the cursor
            self.tool = 'pen'

        def eraser():
            self.master.config(cursor='circle')
            self.tool = 'eraser'
        

        #  tool functions
        def paint(e):
            if self.ox and self.oy:

                self.canvas.create_line(self.ox, self.oy, e.x, e.y, width=self.penwidth,
                fill=self.fgcolor, capstyle=ROUND, smooth=True)
        
            self.ox, self.oy = e.x, e.y
        
        def reset(e):
            self.ox, self.oy = None, None

        def erase(e):
            x1, y1 = (e.x-1), (e.y-1)
            x2, y2 = (e.x+1), (e.y+1)
            self.canvas.create_oval(x1, y1, x2, y2, fill=self.bgcolor,
            outline=self.bgcolor, width=25)

        def changePencolor():
            self.fgcolor = colorchooser.askcolor(color=self.fgcolor)[1]
            self.colorbutton['bg'] = self.fgcolor


        #  Frame
        self.tbframe = Frame(self.master, bg='#bfbfbf')
        self.tbframe.pack(side='top', fill='x', padx='10')


        #  variables
        self.ox, self.oy = None, None
        self.tool = ''

        #  Create buttons  
        self.penbutton = Button(self.tbframe, text='pen', command=pen)
        self.eraserbutton = Button(self.tbframe, text='eraser', command=eraser)
        self.colorbutton = Button(self.tbframe, width=3,  bg=self.fgcolor, command=changePencolor)

        self.penbutton.pack(side='left', padx=2, pady=2)
        self.eraserbutton.pack(side='left', padx=2, pady=2)
        self.colorbutton.pack(side='right', padx=5, pady=2)

        verifytool()



if __name__ == '__main__':
    root = Tk()
    root.title('Paint Tkinter')
    App(root)
    root.mainloop()
