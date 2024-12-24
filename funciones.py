"""LISTA DE ERRORES A CORREGIR
_Al crear cuenta nueva se debería abrir el archivo creado automáticamente
_Revisar la barra de herramientas
"""

class OptionWindow(Toplevel):
    def __call__(self, options=[], display=True):
        self.options = options

        self.listbox.delete(0, END)
        for key, value in options:
            self.listbox.insert(END, key)

        if display:
            self.display()

    def __init__(self):
        Toplevel.__init__(self, master=root)
        self.options = None
        self.title('Matches')

        self.listbox = Listbox(master=self)

        self.listbox.pack(expand=True, fill=BOTH, side=TOP)
        self.listbox.focus_set()
        self.listbox.activate(0)
        self.listbox.selection_set(0)

        self.listbox.config(width=50)

        self.listbox.bind('<Key-h>',
                          lambda event: self.listbox.event_generate('<Left>'))

        self.listbox.bind('<Key-l>',
                          lambda event: self.listbox.event_generate('<Right>'))

        self.listbox.bind('<Key-k>',
                          lambda event: self.listbox.event_generate('<Up>'))

        self.listbox.bind('<Key-j>',
                          lambda event: self.listbox.event_generate('<Down>'))

        self.listbox.bind('<Escape>', lambda event: self.close())
        self.protocol("WM_DELETE_WINDOW", self.close)
        self.transient(root)
        self.withdraw()

    def display(self):
        self.grab_set()
        self.deiconify()
        self.listbox.focus_set()
        # self.wait_window(self)

    def close(self):
        # When calling destroy or withdraw without
        # self.deoiconify it doesnt give back
        # the focus to the parent window.

        self.deiconify()
        self.grab_release()
        self.withdraw()