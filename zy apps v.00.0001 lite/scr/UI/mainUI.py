from Tkinter import *

from UI import listUI, sptex, enofaref


APP_NAME = " "
APP_VERSION = " "

def run_app(name, version, status):
    global APP_NAME
    APP_NAME = str(name)
    global APP_VERSION
    APP_VERSION = str(version) + str(status)

    #run Main UI for this application
    root = Tk()
    app = App(root)
    app.mainloop()

class App(Frame):
    def __init__(self, master=None):
        Frame.__init__(self)
        self.win = master
        self.pack()
        self.initUI()
        self.UI()

    def initUI(self):
        title = APP_NAME + "  -  " + APP_VERSION
        self.win.title(title)
        self.win.geometry("400x600")

    def UI(self):
        self.menucfg()
        self.UI_list()

    def menucfg(self):
        menubar = Menu(self)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="", command=None)
        menubar.add_cascade(label="File", menu=filemenu)

        addmenu = Menu(menubar, tearoff=0)
        addmenu.add_command(label="Enofa Ref", command=self.UI_enofaref)
        addmenu.add_command(label="Efaktur Export", command=self.UI_sptex)
        menubar.add_cascade(label="Add", menu=addmenu)

        self.master.config(menu=menubar)

    def UI_list(self):
        listUI.UI(self)

    def UI_enofaref(self):
        enofaref.UI(self)

    def UI_sptex(self):
        sptex.UI(self)
        
        
    



    
