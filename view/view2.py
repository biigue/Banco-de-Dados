# coding: utf8
from tkinter import *
from tkinter import ttk

class FirstWindow(Toplevel):
    def __init__(self, master=None):
        Toplevel.__init__(self, master=master)

        # Configuração da janela principal
        self.title('Primeira Janela')
        self.configure(background='green')
        self.geometry('480x240')

        # container
        self.fw1 = Toplevel()
        self.fw1["pady"] = 10
        self.fw1.pack()
        self.fw2 = Toplevel()
        self.fw2["padx"] = 20
        self.fw2["pady"] = 10
        self.fw2.pack()
        self.fw3 = Toplevel()
        self.fw3["padx"] = 30
        self.fw3["pady"] = 20
        self.fw3.pack()

        self.btIniciar = Button(Toplevel(), text='Iniciar', width=10, command=self.bt_iniciar)
        self.btIniciar.place(x=0, y=0)

        # self.txtnome = Entry(self.fw2)
        # self.txtnome["width"] = 25
        # self.txtnome.pack()




class SecondWindow(Toplevel):
    def __init__(self, master=None):
        Toplevel.__init__(self, master=master)

        # Configuração da janela principal
        self.title('Segunda Janela')
        self.configure(background='darkgray')
        self.geometry('480x240')


class ThirdWindow(Toplevel):
    def __init__(self, master=None):
        Toplevel.__init__(self, master=master)

        # Configuração da janela principal
        self.title('Terceira Janela')
        self.configure(background='yellow')
        self.geometry('480x240')


class MainWindow(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, master=None)

        # Configuração da janela principal
        self.master.title('Escolha a Tabela')
        self.master.geometry('480x240')
        self.configure(borderwidth=4)
        self.configure(background='white')

        #container
        self.container1 = Frame()
        self.container1["pady"] = 10
        self.container1.pack()
        self.container2 = Frame()
        self.container2["padx"] = 20
        self.container2["pady"] = 10
        self.container2.pack()
        self.container3 = Frame()
        self.container3["padx"] = 30
        self.container3["pady"] = 20
        self.container3.pack()

        self.titulo = Label(self.container1, text="Reserva de Vôo")
        self.titulo2 = Label(self.container1, text="Escolha uma tabela")
        self.titulo["font"] = ("Calibri", "9", "bold")
        self.titulo2["font"] = ("Calibri", "9")
        self.titulo.pack()
        self.titulo2.pack()

        for name in ("Reserva", "Reserva Trecho", "Assento", "Horario", "Vôo"):
            self.button = Button(self.container2, text=name)
            self.button.bind("<Button-1>", self.handle_event)
            self.button.pack(side='left', fill='x', expand=True)

        for name in ("Trecho", "Aeroporto", "Cidade", "Tipo Aeronave", "Aeronave Lugar"):
            self.button = Button(self.container3, text=name)
            self.button.bind("<Button-1>", self.handle_event)
            self.button.pack(side='left', fill='x', expand=True)

        # Empacotamos o frame principal
        self.pack(fill='both', expand=True)

    def handle_event(self, event):
        btn_name = event.widget.cget('text')
        if btn_name.endswith('Reserva'):
            window = FirstWindow()
        if btn_name.endswith('Reserva Trecho'):
            window = SecondWindow()
        if btn_name.endswith('Assento'):
            window = ThirdWindow()

        window.mainloop()


if __name__ == '__main__':
    mainWindow = MainWindow()
    mainWindow.mainloop()