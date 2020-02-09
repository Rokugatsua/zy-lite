from Tkinter import *
from scr import dacon

class UI:
    def __init__(self, parent):
        self.win = Toplevel(parent)
        self.initUI()
        self.formUI()

    def initUI(self):
        self.win.title("Add Refrensi Enofa")
        #self.win.geometry("400x600")

    def formUI(self):
        formframe = Frame(self.win)
        formframe.pack()

        lfenofas = LabelFrame(formframe, text = "Enofa Awal")
        lfenofas.pack()

        self.venofas = StringVar()
        self.venofas.set("")
        fenofas = Entry(lfenofas, textvariable=self.venofas)
        fenofas.pack()
        
        lfenofae = LabelFrame(formframe, text = "Enofa Akhir")
        lfenofae.pack()

        self.venofae = StringVar()
        self.venofae.set("")
        fenofae = Entry(lfenofae, textvariable=self.venofae)
        fenofae.pack()
        
        bottomframe = Frame(self.win)
        bottomframe.pack()

        btn_save = Button(bottomframe, text = "save", command= self.save_to_db)
        btn_save.pack()

    def save_to_db(self):
        daconin = dacon.In()
        vars =  self.venofas.get()
        vare =  self.venofae.get()
        daconin.save_enofa(vars, vare)
        self.return_var()

    def return_var(self):
        self.venofas.set("")
        self.venofae.set("")
