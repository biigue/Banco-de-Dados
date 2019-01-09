# coding: utf8
from tkinter import *
from tkinter import ttk


class Application:
    def __init__(self, master=None):
        # seta os containers
        self.container1 = Frame(master)
        self.container1["pady"] = 10
        self.container1.pack()
        self.container2 = Frame(master)
        self.container2["padx"] = 20
        self.container2["pady"] = 10
        self.container2.pack()
        self.container3 = Frame(master)
        self.container3["padx"] = 30
        self.container3["pady"] = 20
        self.container3.pack()

        # modifica o container 1
        self.titulo = Label(self.container1, text="Reserva de Vôo")
        self.titulo2 = Label(self.container1, text="Escolha uma tabela")
        self.titulo["font"] = ("Calibri", "9", "bold")
        self.titulo2["font"] = ("Calibri", "9")
        self.titulo.pack()
        self.titulo2.pack()

        # adiciona os bts - linha 1
        self.reserva = Button(self.container2)
        self.reserva["text"] = "Reserva"
        self.reserva["font"] = ("Calibri", "8")
        self.reserva["width"] = 12
        self.reserva["command"] = self.click_reserva
        self.reserva.pack(side=LEFT)

        self.rvs_trecho = Button(self.container2)
        self.rvs_trecho["text"] = "Reserva Trecho"
        self.rvs_trecho["font"] = ("Calibri", "8")
        self.rvs_trecho["width"] = 12
        # self.rvs_trecho["command"] = self.verificaSenha
        self.rvs_trecho.pack(side=LEFT)

        self.assento = Button(self.container2)
        self.assento["text"] = "Assento"
        self.assento["font"] = ("Calibri", "8")
        self.assento["width"] = 12
        # self.assento["command"] = self.verificaSenha
        self.assento.pack(side=LEFT)

        self.horario = Button(self.container2)
        self.horario["text"] = "Horario"
        self.horario["font"] = ("Calibri", "8")
        self.horario["width"] = 12
        # self.horario["command"] = self.verificaSenha
        self.horario.pack(side=LEFT)

        self.voo = Button(self.container2)
        self.voo["text"] = "Vôo"
        self.voo["font"] = ("Calibri", "8")
        self.voo["width"] = 12
        # self.voo["command"] = self.verificaSenha
        self.voo.pack(side=LEFT)

        # linha 2
        self.trecho = Button(self.container3)
        self.trecho["text"] = "Trecho"
        self.trecho["font"] = ("Calibri", "8")
        self.trecho["width"] = 12
        # self.trecho["command"] = self.verificaSenha
        self.trecho.pack(side=LEFT)

        self.aeroporto = Button(self.container3)
        self.aeroporto["text"] = "Aeroporto"
        self.aeroporto["font"] = ("Calibri", "8")
        self.aeroporto["width"] = 12
        # self.aeroporto["command"] = self.verificaSenha
        self.aeroporto.pack(side=LEFT)

        self.cidade = Button(self.container3)
        self.cidade["text"] = "Cidade"
        self.cidade["font"] = ("Calibri", "8")
        self.cidade["width"] = 12
        # self.cidade["command"] = self.verificaSenha
        self.cidade.pack(side=LEFT)

        self.tipoAeronave = Button(self.container3)
        self.tipoAeronave["text"] = "Tipo Aeronave"
        self.tipoAeronave["font"] = ("Calibri", "8")
        self.tipoAeronave["width"] = 12
        # self.tipoAeronave["command"] = self.verificaSenha
        self.tipoAeronave.pack(side=LEFT)

        self.tipoaeronave_assento = Button(self.container3)
        self.tipoaeronave_assento["text"] = "Aeronave_Lugar"
        self.tipoaeronave_assento["font"] = ("Calibri", "8")
        self.tipoaeronave_assento["width"] = 12
        # self.tipoaeronave_assento["command"] = self.verificaSenha
        self.tipoaeronave_assento.pack(side=LEFT)


    def click_reserva(self):
        self.jan = Toplevel()
        self.l = Label(self.jan, text='Reserva')
        self.l.pack()

        self.txtnome = Entry(self.jan)
        self.txtnome["width"] = 25
        self.txtnome.pack()



        b = Button(self.jan, text='Voltar', command=self.fecha_jan)
        b.pack()
        #self.jan.geometry('500x200')
        self.jan.transient(root)  #
        self.jan.focus_force()  #
        self.jan.grab_set()  #



    def fecha_jan(self):
        self.jan.destroy()


root = Tk()
root.geometry("500x200")
Application(root)
root.mainloop()




