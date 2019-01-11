try:
    from Tkinter import *
    from ttk import *
except ImportError:  # Python 3
    from tkinter import *
    from tkinter.ttk import *

lista=[('a','b','c'),('c','d','e'),('f','g','h')] #dicionario chave valor

class App(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.CreateUI()
        self.LoadTable()
        self.grid(sticky = (N,S,W,E))
        parent.grid_rowconfigure(0, weight = 1)
        parent.grid_columnconfigure(0, weight = 1)

    def CreateUI(self):
        tv = Treeview(self)
        tv['columns'] = ('Passageiro', 'Prazo')  #('Passageiro', 'Prazo', 'status')
        tv.heading("#0", text='Codigo Reserva', anchor='w')
        tv.column("#0", anchor="w")
        tv.heading('Passageiro', text='Passageiro')
        tv.column('Passageiro', anchor='center', width=100)
        tv.heading('Prazo', text='Prazo')
        tv.column('Prazo', anchor='center', width=100)
        #tv.heading('status', text='Status')
        #tv.column('status', anchor='center', width=100)
        tv.grid(sticky = (N,S,W,E))
        self.treeview = tv
        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(0, weight = 1)

    def LoadTable(self):
        self.treeview.insert('', 'end', text="First", values=('10:00',
                             '10:10', 'Ok'))
        self.treeview.insert('', 'end', text="First", values=('10:00',
                                                              '10:10'))
        ins1=lista[1]
        cod=lista[0][1]
        self.treeview.insert('','end',text= 'second',values=(ins1))

def main():
    root = Tk()
    App(root)
    root.mainloop()

if __name__ == '__main__':
    main()