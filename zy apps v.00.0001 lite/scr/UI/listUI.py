from Tkinter import *
from scr import dacon

class UI:
    def __init__(self, parent):
        self.win = parent
        self.UI_head()
        self.listing_data()

    def UI_head(self):
        headframe = Frame(self.win)
        headframe.pack()
        O = dacon.Out()
        enofaref = O.get_enofa_ref()
        d_tname = enofaref["tname"]
        option = [" "]
        for li in d_tname:
            print li
            option.append(str(li))

        self.va = StringVar()
        self.va.set(option[0])
        head_om = apply(OptionMenu, (headframe, self.va) + tuple(option))
        head_om.pack()

        head_btn = Button(headframe, text = "refresh",command=self.refresh)
        head_btn.pack()
        s_btn = Button(headframe, text = "spliting",command=self.spliting_print)
        s_btn.pack()
        

    def listing_data(self):
        listframe = Frame(self.win)
        listframe.pack()
        
        tname = self.va.get()
        O = dacon.Out()
        data = O.get_enofa_lists(tname)
        
        self.libox = Listbox(listframe)

        for li in data:
            self.libox.insert(END,li)

        self.libox.pack()

    def refresh(self):        
        tname = self.va.get()
        O = dacon.Out()
        data = O.get_enofa_lists(tname)

        self.libox.delete(0,END)

        for li in data:
            self.libox.insert(END,li)

    def spliting_print(self):
        tname = self.va.get()
        O = dacon.Out()
        data = O.spliting_data(tname)
        

        

    
