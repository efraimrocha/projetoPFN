# import tkinter


# class Win(tkinter.Tk):

#     def __init__(self, master=None):
#         tkinter.Tk.__init__(self, master)
#         self.overrideredirect(True)
#         self._offsetx = 0
#         self._offsety = 0
#         self.bind('<Button-1>', self.clickwin)
#         self.bind('<B1-Motion>', self.dragwin)

#     def dragwin(self, event):
#         x = self.winfo_pointerx() - self._offsetx
#         y = self.winfo_pointery() - self._offsety
#         self.geometry('+{x}+{y}'.format(x=x, y=y))

#     def clickwin(self, event):
#         self._offsetx = event.x
#         self._offsety = event.y


# win = Win()
# win.mainloop()
from tkinter import *
# onde criaremos os controles q serão exibidos


class Application:
    def __init__(self, master=None):
        self.widget1 = Frame(master)
        self.widget1.pack(padx=100, pady=150)
        self.msg = Label(self.widget1, text="Primeiro widget")
        self.msg["font"] = ("Calibri", "9", "italic")
        self.msg.pack ()
        self.sair = Button(self.widget1)
        self.sair["text"] = "Clique aqui"
        self.sair["font"] = ("Calibri", "9")
        self.sair["width"] = 10
        self.sair.bind("<Button-1>", self.mudarTexto)
        self.sair.pack ()

    def mudarTexto(self, event):
        if self.msg["text"] == "Primeiro widget":
            self.msg["text"] = "O botão recebeu um clique"
        else:
            self.msg["text"] = "Primeiro widget"



root = Tk()
Application(root)
root.mainloop()
