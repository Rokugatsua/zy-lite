from Tkinter import *
from scr import dacon

class UI:
    def __init__(self, parent):
        self.win = Toplevel(parent)
        self.initUI()
        self.formUI()

    def initUI(self):
        self.win.title("Add Csv From Efaktur Export")
        #self.win.geometry("400x600")

    def formUI(self):
        formframe = Frame(self.win)
        formframe.pack()

        lf = LabelFrame(formframe, text = "list .csv file")
        lf.pack()

        scroller = Scrollbar(lf)
        scroller.pack(fill=Y, side=RIGHT)

        self.libox = Listbox(lf, yscrollcommand=scroller.set)
        lidata = self.getlist()
        for li in lidata:
            self.libox.insert(END, li)

        self.libox.pack(fill=BOTH, side=LEFT)
        scroller.config(command=self.libox.yview)
        
        bottomframe = Frame(self.win)
        bottomframe.pack()

        btn_save = Button(bottomframe, text = "Pilih", command= self.save_to_db)
        btn_save.pack()

        btn_refresh = Button(bottomframe,text = "Refresh", command=None)
        btn_refresh.pack()

    def getlist(self):
        O = dacon.Out()
        listdata = O.get_list_csv()
        #listdata = ["1.csv", "2.csv"]
        return listdata
        

    def save_to_db(self):
        csv_name = self.libox.get(self.libox.curselection())
        I = dacon.In()
        I.add_csvfile(csv_name)
        
        
