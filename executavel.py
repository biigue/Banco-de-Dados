# coding: utf8
from tkinter import *
from tkinter import ttk
import tkinter as tk


from controller.dbController import *
from models.Reserva import Reserva

class TabelaReserva(Toplevel):
    def __init__(self, master=None):
        Toplevel.__init__(self, master=master)
        # Configuração da janela principal
        self.title('Tabela Reserva')
        self.configure(background='gray94')
        self.geometry('480x540')


        #entradas
        self.textocodReserva = tk.Label(self, text="Codígo da Reserva(Inteiro) *")
        self.textocodReserva.grid(column=2, row=0, padx=(100, 10), pady=5)
        self.entradacodReserva = tk.Entry(self)
        self.entradacodReserva.grid(column=3, row=0,
                              sticky='EW')

        self.textopass = tk.Label(self, text="Passageiro")
        self.textopass.grid(column=2, row=1, padx =(100,10), pady= 5)
        self.entradapass = tk.Entry(self)
        self.entradapass.grid(column=3, row=1,
                         sticky='EW')

        self.textoprazo = tk.Label(self, text="Prazo (AAAA/MM/DD)")
        self.textoprazo.grid(column=2, row=2, padx=(100, 10), pady=5)
        self.entradaprazo = tk.Entry(self)
        self.entradaprazo.grid(column=3, row=2,
                         sticky='EW')

        #Botões /fazer o click deles
        ##command=self.inserirBanco(self.entradacodReserva, self.entradapass, self.entradaprazo) < isso vai depois do text do button, ou algo assim pra setar a func

        self.botaoInserir = tk.Button(self, text=u"Inserir", command=self.inserirBanco)  # criamos o objeto botão
        self.botaoInserir.grid(column=2, row=3, padx=(100, 10), pady=5)

        self.botaoAlterar = tk.Button(self, text=u"Alterar", command=self.clickAlterar)  # criamos o objeto botão
        self.botaoAlterar.grid(column=3, row=3)

        self.botaoExcluir = tk.Button(self, text=u"Excluir", command=self.clickDeletar)  # criamos o objeto botão
        self.botaoExcluir.grid(column=2, row=4, padx=(100, 10), pady=5)

        self.botaoBuscar = tk.Button(self, text=u"Buscar", command=self.clickBuscar)  # criamos o objeto botão
        self.botaoBuscar.grid(column=3, row=4)

        #log
        self.var = StringVar()
        self.var.set('')
        self.log_reserva = tk.Label(self, textvariable = self.var)
        self.log_reserva.grid(column=2, row=5, pady=10)



        #visualizar a tabela de retorno

        self.listbox = Listbox(self)
        self.listbox.grid(column=2,columnspan=12, row=7, padx=(40, 10))
        self.listbox.configure(bg='white', width=40, borderwidth= 30)
        self.criarTabela()

    def criarTabela(self):
        self.updateTabela()

    def updateTabela(self):
        self.listbox.delete(0, END)
        self.listbox.insert(END, "    código, nome, prazo")
        reservas = getReservas()

        for item in reservas:
            text = '    '
            text += str(item.getCodigoReserva()) + ', '
            text += str(item.getPassageiro()) + ', '
            text += str(item.getPrazo())
            self.listbox.insert(tk.END, text)


        #funcoes dos clicks
    def inserirBanco(self):
        self.var.set('')
        codReserva = (self.entradacodReserva.get())  # pega as entradas
        passageiro = (self.entradapass.get())
        prazo = (self.entradaprazo.get())
        if codReserva == '':
            self.var.set('>>>Favor insira o Código da reserva')
        else:
            reserva = Reserva(codReserva, passageiro, prazo)
            self.entradacodReserva.delete(0, tk.END)
            self.entradapass.delete(0, tk.END) # apaga o campo destino
            self.entradaprazo.delete(0, tk.END)
            if getReserva(codReserva) is None:
                if insertReserva(reserva):
                    self.var.set('>>>Cadastro Concluido')
                    self.updateTabela()
                else:
                    self.var.set('>>>Erro')
            else:
                self.var.set('>>>Código da Reserva já existe')
        #else
        #self.var.set('>>>Log do Erro')

    def clickAlterar(self):
        self.var.set('')
        codReserva = (self.entradacodReserva.get())  # pega as entradas
        passageiro = (self.entradapass.get())
        prazo = (self.entradaprazo.get())
        if codReserva == '':
            self.var.set('>>>Favor insira o Código da reserva')
        else:
            reserva = Reserva(codReserva, passageiro, prazo)
            self.entradacodReserva.delete(0, tk.END)
            self.entradapass.delete(0, tk.END)
            self.entradaprazo.delete(0, tk.END)
            if getReserva(codReserva) is not None:
                if updateReserva(reserva):
                    self.var.set('>>>Alteração Realizada')
                    self.updateTabela()
                else:
                    self.var.set('>>>Erro')
            else:
                self.var.set('>>>Não existe reserva com este código')


    def clickDeletar(self):
        self.var.set('')
        codReserva = (self.entradacodReserva.get())  # pega as entradas
        passageiro = (self.entradapass.get())
        prazo = (self.entradaprazo.get())
        if codReserva == '':
            self.var.set('>>>Favor insira o Código da reserva')
        else:
            self.entradacodReserva.delete(0, tk.END)
            self.entradapass.delete(0, tk.END)  # apaga o campo destino
            self.entradaprazo.delete(0, tk.END)
            if getReserva(codReserva) is not None:
                reserva = Reserva(codReserva)
                if deleteReserva(reserva):
                    self.var.set('>>>Reserva excluida com sucesso')
                    self.entradacodReserva.delete(0, tk.END)
                    self.entradapass.delete(0, tk.END)
                    self.entradaprazo.delete(0, tk.END)
                    self.updateTabela()
                else:
                    self.var.set('>>>Erro')
            else:
                self.var.set('>>>Não existe reserva com este código')

    def clickBuscar(self):
        self.var.set('')
        codReserva = (self.entradacodReserva.get())  # pega as entradas
        if codReserva == '':
            self.var.set('>>>Favor insira o Código da reserva')
        else:
            reserva = getReserva(codReserva)
            if reserva is None:
                self.var.set('>>>Não existe reserva com este código')
            else:
                self.entradacodReserva.delete(0, tk.END)
                self.entradapass.delete(0, tk.END)  # apaga o campo destino
                self.entradaprazo.delete(0, tk.END)
                self.entradacodReserva.insert(0, reserva.getCodigoReserva())
                self.entradapass.insert(0, reserva.getPassageiro())
                self.entradaprazo.insert(0, reserva.getPrazo())
                self.var.set('>>>Busca concluida com sucesso')
        #enviar o comando pro banco e listar na lista de baixo


class Tabela_Reserva_Tsch(Toplevel):
    def __init__(self, master=None):
        Toplevel.__init__(self, master=master)

        # Configuração da janela principal
        self.title('Reserva Trecho')
        self.configure(background='gray94')
        self.geometry('480x540')

        # entradas
        self.textcodData = tk.Label(self, text="Data (AAAA/MM/DD) *")
        self.textcodData.grid(column=2, row=0, padx=(100, 10), pady=5)
        self.entradacodData = tk.Entry(self)
        self.entradacodData.grid(column=3, row=0,
                                    sticky='EW')

        self.txcodreserva2 = tk.Label(self, text="Cod Reserva *") #fazer o select~?
        self.txcodreserva2.grid(column=2, row=1, padx=(100, 10), pady=5)
        self.entradacodreserva2 = tk.Entry(self)
        self.entradacodreserva2.grid(column=3, row=1,
                              sticky='EW')

        self.txtidAssento2 = tk.Label(self, text="Id Assento") #fazer o select~?
        self.txtidAssento2.grid(column=2, row=2, padx=(100, 10), pady=5)
        self.entAssento2 = tk.Entry(self)
        self.entAssento2.grid(column=3, row=2,
                               sticky='EW')

        self.txtidTrecho2 = tk.Label(self, text="Id Trecho") #fazer o select~?
        self.txtidTrecho2.grid(column=2, row=3, padx=(100, 10), pady=5)
        self.entTrecho2 = tk.Entry(self)
        self.entTrecho2.grid(column=3, row=3,
                              sticky='EW')

        # Botões /fazer o click deles
        ##command=self.inserirBanco(self.entradacodReserva, self.entradapass, self.entradaprazo) < isso vai depois do text do button, ou algo assim pra setar a func

        self.botaoInserir2 = tk.Button(self, text=u"Inserir", command=self.inserirBanco)  # criamos o objeto botão
        self.botaoInserir2.grid(column=2, row=4, padx=(100, 10), pady=5)

        self.botaoAlterar2 = tk.Button(self, text=u"Alterar", command=self.clickAlterar)  # criamos o objeto botão
        self.botaoAlterar2.grid(column=3, row=4)

        self.botaoExcluir2 = tk.Button(self, text=u"Excluir", command=self.clickDeletar)  # criamos o objeto botão
        self.botaoExcluir2.grid(column=2, row=5, padx=(100, 10), pady=5)

        self.botaoBuscar2 = tk.Button(self, text=u"Buscar", command=self.clickBuscar)
        self.botaoBuscar2.grid(column=3, row=5)


        # log
        self.var2 = StringVar()
        self.var2.set('')
        self.log_trecho_reserva = tk.Label(self, textvariable=self.var2)
        self.log_trecho_reserva.grid(column=2, row=6, pady=10)


        # visualizar a tabela de retorno
        self.listbox = Listbox(self)
        self.listbox.grid(column=2, columnspan=12, row=7, padx=(40, 10))
        self.listbox.configure(bg='white', width=40, borderwidth=30)
        self.criarTabela()

    def criarTabela(self):
        self.listbox.delete(0, END)
        self.listbox.insert(END, "    Data, Código da Reserva, Número do Assento, ID Trecho")

        for item in getReservaTrechos():
            text = '    '
            text += str(item.getData())+', '
            text += str(item.getCodigoReserva())+', '
            text += str(item.getNumeroAssento())+', '
            text += str(item.getIdTrecho())
            self.listbox.insert(END, text)

#funcoes dos clicks
    def inserirBanco(self):
        self.var2.set('')
        coddata = (self.entradacodData.get())  # pk
        codReserva = (self.entradacodreserva2.get()) #fk
        idAssento = (self.entAssento2.get()) #fk
        idTrecho = (self.entTrecho2.get()) #fk
        #enviar pro banco e voltar com erro ou sucesso
        #se for sucesso
        if coddata == '' or codReserva == '':
            self.var2.set('>>>Favor insira o Código da reserva e a Data')
        else:
            reserva = ReservaTrecho(coddata, codReserva, idAssento, idTrecho)
            if getReservaTrecho(coddata) is None:
                self.entradacodData.delete(0, tk.END)
                self.entradacodreserva2.delete(0, tk.END) # apaga o campo destino
                self.entAssento2.delete(0, tk.END)
                self.entTrecho2.delete(0, tk.END)
                if insertReservaTrecho(reserva):
                    self.var2.set('>>>Cadastro Concluido')#alterar para só funcionar se inserir mesmo
                    self.criarTabela()
                else:
                    self.var2.set('>>>Erro')
            else:
                self.var2.set('>>>Já existe registro com esta data')
        # #else
        # #self.var.set('>>>Log do Erro')

    def clickAlterar(self):
        self.var2.set('')
        coddata = (self.entradacodData.get())  # pk
        codReserva = (self.entradacodreserva2.get())  # fk
        idAssento = (self.entAssento2.get())  # fk
        idTrecho = (self.entTrecho2.get())  # fk
        if coddata == '':
            self.var2.set('>>>Favor insira a data')
        else:
            reserva = ReservaTrecho(coddata, codReserva, idAssento, idTrecho)
            if getReservaTrecho(coddata) is not None:
                self.entradacodData.delete(0, tk.END)
                self.entradacodreserva2.delete(0, tk.END)  # apaga o campo destino
                self.entAssento2.delete(0, tk.END)
                self.entTrecho2.delete(0, tk.END)
                if updateReservaTrecho(reserva):
                    # mensagem log
                    self.var2.set('>>>Cadastro alterado com sucesso')  # alterar para só funcionar se inserir mesmo
                    self.criarTabela()
                else:
                    self.var2.set('>>>Erro')
            else:
                self.var2.set('>>>Não existe registro com esta data')

    def clickDeletar(self):
        self.var2.set('')
        coddata = (self.entradacodData.get())  # pk
        codReserva = (self.entradacodreserva2.get())  # fk
        idAssento = (self.entAssento2.get())  # fk
        idTrecho = (self.entTrecho2.get())  # fk
        #pode deletar sem ter o id, ai deletaria tudo que tem aquele nome por ex
        if codReserva == '':
            self.var2.set('>>>Favor insira o Código da reserva')
        else:
            reserva = ReservaTrecho(coddata, codReserva, idAssento, idTrecho)
            if getReservaTrecho(coddata) is not None:
                self.entradacodData.delete(0, tk.END)
                self.entradacodreserva2.delete(0, tk.END)  # apaga o campo destino
                self.entAssento2.delete(0, tk.END)
                self.entTrecho2.delete(0, tk.END)
                if deleteReservaTrecho(reserva):
                    # mensagem log
                    self.var2.set('>>>Cadastro excluido com sucesso')  # alterar para só funcionar se inserir mesmo
                    self.criarTabela()
                else:
                    self.var2.set('>>>Erro')
            else:
                self.var2.set('>>>Não existe registro com esta data')

    def clickBuscar(self):
        self.var2.set('')
        coddata = (self.entradacodData.get())  # pk
        codReserva = (self.entradacodreserva2.get())  # fk
        idAssento = (self.entAssento2.get())  # fk
        idTrecho = (self.entTrecho2.get())  # fk
        if coddata == '':
            self.var2.set('>>> Favor insira a data')
        else:
            reserva = getReservaTrecho(coddata)
            if reserva is None:
                self.var2.set('>>>Não existe registro com esta data')
            else:
                self.entradacodData.delete(0, tk.END)
                self.entradacodreserva2.delete(0, tk.END)  # apaga o campo destino
                self.entAssento2.delete(0, tk.END)
                self.entTrecho2.delete(0, tk.END)
                self.entradacodData.insert(0, reserva.getData())
                self.entradacodreserva2(0, reserva.getCodigoReserva())
                self.entTrecho2.insert(0, reserva.getIdTrecho())
                self.entAssento2.insert(0, reserva.getNumeroAssento())


class Tabela_Assento(Toplevel):
    def __init__(self, master=None):
        Toplevel.__init__(self, master=master)

        # Configuração da janela principal
        self.title('Assento')
        self.configure(background='gray94')
        self.geometry('480x540')

        # entradas
        self.textnmAssento = tk.Label(self, text="Numero *")
        self.textnmAssento.grid(column=2, row=0, padx=(110, 10), pady=5)
        self.entnmAssento = tk.Entry(self)
        self.entnmAssento.grid(column=3, row=0,
                                 sticky='EW')

        self.txtclasse = tk.Label(self, text="Classe")
        self.txtclasse.grid(column=2, row=1, padx=(110, 10), pady=5)
        self.entclasse = tk.Entry(self)
        self.entclasse.grid(column=3, row=1,
                                     sticky='EW')

        # Botões /fazer o click deles
        ##command=self.inserirBanco(self.entradacodReserva, self.entradapass, self.entradaprazo) < isso vai depois do text do button, ou algo assim pra setar a func

        self.botaoInserir = tk.Button(self, text=u"Inserir",command=self.inserirBanco)  # criamos o objeto botão
        self.botaoInserir.grid(column=2, row=4, padx=(180, 10), pady=5)

        self.botaoAlterar = tk.Button(self, text=u"Alterar",command=self.clickAlterar)  # criamos o objeto botão
        self.botaoAlterar.grid(column=3, row=4)

        self.botaoExcluir = tk.Button(self, text=u"Excluir",command=self.clickDeletar)  # criamos o objeto botão
        self.botaoExcluir.grid(column=2, row=5, padx=(180, 10), pady=5)

        self.botaoBuscar = tk.Button(self, text=u"Buscar",command=self.clickBuscar)  # criamos o objeto botão
        self.botaoBuscar.grid(column=3, row=5)

        # log
        self.var = StringVar()
        self.var.set('')
        self.log_reserva = tk.Label(self, textvariable=self.var)
        self.log_reserva.grid(column=2, row=6, pady=10)

        # visualizar a tabela de retorno

        self.listbox = Listbox(self)
        self.listbox.grid(column=2, columnspan=12, row=7, padx=(40, 10))
        self.listbox.configure(bg='white', width=40, borderwidth=30)
        self.criarTabela()

    def criarTabela(self):
        self.listbox.insert(END, "    Numero Assento, Classe")

        for item in getAssentos():
            text = '    '
            text += str(item.getNumero())+', '
            text += str(item.getClasse())
            self.listbox.insert(END, text)

    #funcoes dos clicks
    def inserirBanco(self):
        self.var.set('')
        numAssento = (self.entnmAssento.get())
        classe = (self.entclasse.get())
        #enviar pro banco e voltar com erro ou sucesso
        #se for sucesso
        if numAssento == '':
            self.var.set('>>>Favor insira o número do assento')
        else:
            if getAssento(numAssento) is None:
                asse = Assento(numAssento, classe)
                if insertAssento(asse):
                    self.var.set('>>>Assento inserido com sucesso')
                    self.entnmAssento.delete(0, END)
                    self.entclasse.delete(0, END)
                    self.criarTabela()
                else:
                    self.var.set('>>>Erro')
            else:
                self.var.set('>>>Número de Assento já cadastrado')

    def clickAlterar(self):
        self.var.set('')
        numAssento = (self.entnmAssento.get())
        classe = (self.entclasse.get())

        if numAssento == '':
            self.var.set('>>>Favor insira o número do assento')
        else:
            if getAssento(numAssento) is not None:
                asse = Assento(numAssento, classe)
                if updateAssento(asse):
                    self.entnmAssento.delete(0, END)
                    self.entclasse.delete(0, END)
                    self.var.set('>>>Assento alterado com sucesso')
                    self.criarTabela()
                else:
                    self.var.ser('>>>Erro')
            else:
                self.var.set('>>>Não existe assento com este número cadastrado')

    def clickDeletar(self):
        self.var.set('')
        numAssento = (self.entnmAssento.get())
        classe = (self.entclasse.get())
        if numAssento == '':
            self.var.set('>>>Favor insira o número do assento')
        else:
            if getAssento(numAssento):
                asse = Assento(numAssento, classe)
                if deleteAssento(asse):
                    self.entnmAssento.delete(0, END)
                    self.entclasse.delete(0, END)
                    self.var.set('>>>Assento deletado com sucesso')
                    self.criarTabela()
                else:
                    self.var.set('>>>Erro')
            else:
                self.var.set('>>>Não existe assento com este número cadastrado')


    def clickBuscar(self):
        self.var.set('')
        numAssento = (self.entnmAssento.get())
        classe = (self.entclasse.get())
        if numAssento == '':
            self.var.set('>>>Favor insira o número do assento')
        else:
            asse = getAssento(numAssento)
            if asse is not None:
                self.entnmAssento.delete(0, END)
                self.entclasse.delete(0, END)
                self.entnmAssento.insert(0, asse.getNumero())
                self.entclasse.insert(0, asse.getClasse())
                self.var.set('>>>Assento encontrado com sucesso')
            else:
                self.var.set('>>>Não existe assento com esse número cadastrado')


class Tabela_Horario(Toplevel):
    def __init__(self, master=None):
        Toplevel.__init__(self, master=master)

        # Configuração da janela principal
        self.title('Horário')
        self.configure(background='gray94')
        self.geometry('480x540')

        # entradas
        self.txtdiaSemana = tk.Label(self, text="Dia da Semana *")
        self.txtdiaSemana.grid(column=2, row=0, padx=(120, 10), pady=5)
        self.entdiaSemana = tk.Entry(self)
        self.entdiaSemana.grid(column=3, row=0,
                                    sticky='EW')

        self.txhorarioPartida= tk.Label(self, text="Horario Partida")
        self.txhorarioPartida.grid(column=2, row=1, padx=(120, 10), pady=5)
        self.enhorarioPartida = tk.Entry(self)
        self.enhorarioPartida.grid(column=3, row=1,
                              sticky='EW')

        self.txthrChegada = tk.Label(self, text="Horario Chegada")
        self.txthrChegada.grid(column=2, row=2, padx=(120, 10), pady=5)
        self.enthrChegada = tk.Entry(self)
        self.enthrChegada.grid(column=3, row=2,
                               sticky='EW')

        self.txtidTrecho_horario = tk.Label(self, text="Id Trecho") #fazer o select~?
        self.txtidTrecho_horario.grid(column=2, row=3, padx=(120, 10), pady=5)
        self.entTrecho_horario = tk.Entry(self)
        self.entTrecho_horario.grid(column=3, row=3,
                              sticky='EW')

        # Botões /fazer o click deles
        ##command=self.inserirBanco(self.entradacodReserva, self.entradapass, self.entradaprazo) < isso vai depois do text do button, ou algo assim pra setar a func

        self.botaoInserir = tk.Button(self, text=u"Inserir", command=self.inserirBanco)  # criamos o objeto botão
        self.botaoInserir.grid(column=2, row=4, padx=(160, 10), pady=5)

        self.botaoAlterar = tk.Button(self, text=u"Alterar", command=self.clickAlterar)  # criamos o objeto botão
        self.botaoAlterar.grid(column=3, row=4)

        self.botaoExcluir = tk.Button(self, text=u"Excluir", command=self.clickDeletar)  # criamos o objeto botão
        self.botaoExcluir.grid(column=2, row=5, padx=(160, 10), pady=5)

        self.botaoBuscar = tk.Button(self, text=u"Buscar", command=self.clickBuscar)  # criamos o objeto botão
        self.botaoBuscar.grid(column=3, row=5)

        # log
        self.var = StringVar()
        self.var.set('')
        self.log_reserva = tk.Label(self, textvariable=self.var)
        self.log_reserva.grid(column=2, row=6, pady=10)

        # visualizar a tabela de retorno

        self.listbox = Listbox(self)
        self.listbox.grid(column=2, columnspan=12, row=7, padx=(40, 10))
        self.listbox.configure(bg='white', width=40, borderwidth=30)
        self.criarTabela()

    def criarTabela(self):
        self.updateTabela()

    def updateTabela(self):
        self.listbox.delete(0, END)
        self.listbox.insert(END, "    Dia da Semana, Hr Partida, Hr Chegada, Trecho")
        lista = getHorarios()

        for item in lista:
            text = '    '
            text += str(item.getDiaSemana()) + ', '
            text += str(item.getHorarioPartida()) + ', '
            text += str(item.getHorarioChegada()) + ', '
            text += str(item.getIdTrecho())
            self.listbox.insert(tk.END, text)

    #funcoes dos clicks
    def inserirBanco(self):
        self.var.set('')
        diaSemana = (self.entdiaSemana.get())
        horaro_partida = (self.enhorarioPartida.get())
        horario_chegada = (self.enthrChegada.get())
        trecho = (self.entTrecho_horario.get()) #fk
        if diaSemana == '' or trecho == '':
            self.var.set('>>>Favor insira o dia da semana e o id do trecho')
        else:
            if getHorario(diaSemana) is None:
                hor = Horario(diaSemana, horaro_partida, horario_chegada, trecho)
                if insertHorario(hor):
                    self.var.set('>>>Horario cadastrado com sucesso')
                    self.entdiaSemana.delete(0, END)
                    self.enhorarioPartida.delete(0, END)
                    self.enthrChegada.delete(0, END)
                    self.entTrecho_horario.delete(0, END)
                    self.criarTabela()
                else:
                    self.var.set('>>>Erro')
            else:
                self.var.set('>>>Dia da semana já cadastrado')



    def clickAlterar(self):
        self.var.set('')
        diaSemana = (self.entdiaSemana.get())
        horaro_partida = (self.enhorarioPartida.get())
        horario_chegada = (self.enthrChegada.get())
        trecho = (self.entTrecho_horario.get())  # fk
        if diaSemana == '' or trecho == '':
            self.var.set('>>>Favor insira o dia da semana e o trecho')
        else:
            if getHorario(diaSemana) is not None:
                hor = Horario(diaSemana, horaro_partida, horario_chegada, trecho)
                if updateHorario(hor):
                    self.var.set('>>>Horario atualizado com sucesso')
                    self.entdiaSemana.delete(0, END)
                    self.enhorarioPartida.delete(0, END)
                    self.enthrChegada.delete(0, END)
                    self.entTrecho_horario.delete(0, END)
                    self.criarTabela()
                else:
                    self.var.set('>>>Erro')
            else:
                self.var.set('>>>Não exite horario cadastrado para esse dia da semana')


    def clickDeletar(self):
        self.var.set('')
        diaSemana = (self.entdiaSemana.get())
        horaro_partida = (self.enhorarioPartida.get())
        horario_chegada = (self.enthrChegada.get())
        trecho = (self.entTrecho_horario.get())  # fk
        if diaSemana == '':
            self.var.set('>>>Favor insira o dia da semana')
        else:
            if getHorario(diaSemana) is not None:
                hor = Horario(diaSemana, horaro_partida, horario_chegada, trecho)
                if deleteHorario(hor):
                    self.entdiaSemana.delete(0, END)
                    self.enhorarioPartida.delete(0, END)
                    self.enthrChegada.delete(0, END)
                    self.entTrecho_horario.delete(0, END)
                    self.criarTabela()
                else:
                    self.var.set('>>>Erro')
            else:
                self.var.set('>>>Não exite horario cadastrado para esse dia da semana')

    def clickBuscar(self):
        self.var.set('')
        diaSemana = (self.entdiaSemana.get())
        horaro_partida = (self.enhorarioPartida.get())
        horario_chegada = (self.enthrChegada.get())
        trecho = (self.entTrecho_horario.get())  # fk
        if diaSemana == '':
            self.var.set('>>>Favor insira o dia da semana')
        else:
            asse = getHorario(diaSemana)
            if asse is not None:
                self.entdiaSemana.delete(0, END)
                self.enhorarioPartida.delete(0, END)
                self.enthrChegada.delete(0, END)
                self.entTrecho_horario.delete(0, END)
                self.entdiaSemana.insert(0, asse.getDiaSemana())
                self.enhorarioPartida.insert(0, asse.setHorarioPartida())
                self.enthrChegada.insert(0, asse.getHorarioChegada())
                self.entTrecho_horario.insert(0, asse.getIdTrecho())
                self.var.set('>>>Busca concluida com sucesso')
            else:
                self.var.set('>>>Não foi encontrado nenhum horario cadastrado nesse dia da semana')


class Tabela_Voo(Toplevel):
    def __init__(self, master=None):
        Toplevel.__init__(self, master=master)

        # Configuração da janela principal
        self.title('Vôo')
        self.configure(background='gray94')
        self.geometry('480x540')

        # entradas
        self.txtnumVoo= tk.Label(self, text="Numero *")
        self.txtnumVoo.grid(column=2, row=0, padx=(120, 10), pady=5)
        self.entnumVoo = tk.Entry(self)
        self.entnumVoo.grid(column=3, row=0,
                                    sticky='EW')



        # Botões /fazer o click deles
        ##command=self.inserirBanco(self.entradacodReserva, self.entradapass, self.entradaprazo) < isso vai depois do text do button, ou algo assim pra setar a func

        self.botaoInserir = tk.Button(self, text=u"Inserir", command=self.inserirBanco)  # criamos o objeto botão
        self.botaoInserir.grid(column=2, row=4, padx=(160, 10), pady=5)

        self.botaoAlterar = tk.Button(self, text=u"Alterar", command=self.clickAlterar)  # criamos o objeto botão
        self.botaoAlterar.grid(column=3, row=4)

        self.botaoExcluir = tk.Button(self, text=u"Excluir", command=self.clickDeletar)  # criamos o objeto botão
        self.botaoExcluir.grid(column=2, row=5, padx=(160, 10), pady=5)

        self.botaoBuscar = tk.Button(self, text=u"Buscar", command=self.clickBuscar)  # criamos o objeto botão
        self.botaoBuscar.grid(column=3, row=5)

        # log
        self.var = StringVar()
        self.var.set('')
        self.log_reserva = tk.Label(self, textvariable=self.var)
        self.log_reserva.grid(column=2, row=6, pady=10)

        # visualizar a tabela de retorno

        self.listbox = Listbox(self)
        self.listbox.grid(column=2, columnspan=12, row=7, padx=(40, 10))
        self.listbox.configure(bg='white', width=40, borderwidth=30)
        self.criarTabela()

    def criarTabela(self):
        self.updateTabela()

    def updateTabela(self):
        self.listbox.delete(0, END)
        self.listbox.insert(END, "    Numero Vôo")
        lista = getVoos()

        for item in lista:
            text = '    '
            text += str(item.getNumero())

            self.listbox.insert(tk.END, text)

    #funcoes dos clicks
    def inserirBanco(self):
        self.var.set('')
        nmVoo = (self.entnumVoo.get())
        if nmVoo == '':
            self.var.set('>>>Favor insira o Número do Vôo')
        else:
            if getVoo(nmVoo) is None:
                voo = Voo(nmVoo)
                if insertVoo(voo):
                    self.var.set('>>>Voo cadastrado com sucesso')
                    self.entnumVoo.delete(0, END)
                    self.updateTabela()
                else:
                    self.var.set('>>>Erro')
            else:
                self.var.set('>>>Voo já cadastrado')


    def clickAlterar(self):
        self.var.set('>>>Não é possivel alterar o voo, pois ele só possui um campo')
        nmVoo = (self.entnumVoo.get())  # pega as entradas



    def clickDeletar(self):
        self.var.set('')
        nmVoo = (self.entnumVoo.get())  # pega as entradas

        if nmVoo == '':
            self.var.set('>>>Favor insira o Número do Vôo')
        else:
            if getVoo(nmVoo) is not None:
                voo = Voo(nmVoo)
                if deleteVoo(voo):
                    self.var.set('>>>Voo deletado com sucesso')
                    self.entnumVoo.delete(0, END)
                    self.updateTabela()
                else:
                    self.var.set('>>>Erro')
            else:
                self.var.set('>>>Voo não cadastrado')

    def clickBuscar(self):
        self.var.set('')
        nmVoo = (self.entnumVoo.get())  # pega as entradas
        if nmVoo == '':
            self.var.set('>>>Favor insira o Número do Vôo')
        else:
            if getVoo(nmVoo) is not None:
                self.var.set('>>>Voo encontrado com sucesso')
            else:
                self.var.set('>>>Voo não encontrado')


class Tabela_Trecho(Toplevel):
    def __init__(self, master=None):
        Toplevel.__init__(self, master=master)

        # Configuração da janela principal
        self.title('Trecho')
        self.configure(background='gray94')
        self.geometry('480x540')

        # entradas
        self.txtidTrecho_trecho = tk.Label(self, text="ID Trecho *")
        self.txtidTrecho_trecho.grid(column=2, row=0, padx=(120, 10), pady=5)
        self.entidTrecho_trecho = tk.Entry(self)
        self.entidTrecho_trecho.grid(column=3, row=0,
                                    sticky='EW')

        self.txhorarioPartida= tk.Label(self, text="Numero Vôo") #select?
        self.txhorarioPartida.grid(column=2, row=1, padx=(120, 10), pady=5)
        self.enhorarioPartida = tk.Entry(self)
        self.enhorarioPartida.grid(column=3, row=1,
                              sticky='EW')

        self.txt_codaeronave_trecho = tk.Label(self, text="Codigo Aeronave") #select?
        self.txt_codaeronave_trecho.grid(column=2, row=2, padx=(120, 10), pady=5)
        self.ent_codaeronave_trecho = tk.Entry(self)
        self.ent_codaeronave_trecho.grid(column=3, row=2,
                               sticky='EW')

        self.txt_idorigem_trecho = tk.Label(self, text="Id Origem") #fazer o select~?
        self.txt_idorigem_trecho.grid(column=2, row=3, padx=(120, 10), pady=5)
        self.ent_idorigem_trecho = tk.Entry(self)
        self.ent_idorigem_trecho.grid(column=3, row=3,
                              sticky='EW')

        self.txt_idDestino_trecho = tk.Label(self, text="Id Destino")  # fazer o select~?
        self.txt_idDestino_trecho.grid(column=2, row=4, padx=(120, 10), pady=5)
        self.ent_idDestino_trecho = tk.Entry(self)
        self.ent_idDestino_trecho.grid(column=3, row=4,
                                      sticky='EW')

        # Botões /fazer o click deles
        ##command=self.inserirBanco(self.entradacodReserva, self.entradapass, self.entradaprazo) < isso vai depois do text do button, ou algo assim pra setar a func

        self.botaoInserir = tk.Button(self, text=u"Inserir", command=self.inserirBanco)  # criamos o objeto botão
        self.botaoInserir.grid(column=2, row=5, padx=(160, 10), pady=5)

        self.botaoAlterar = tk.Button(self, text=u"Alterar", command=self.clickAlterar)  # criamos o objeto botão
        self.botaoAlterar.grid(column=3, row=5)

        self.botaoExcluir = tk.Button(self, text=u"Excluir", command=self.clickDeletar)  # criamos o objeto botão
        self.botaoExcluir.grid(column=2, row=6, padx=(160, 10), pady=5)

        self.botaoBuscar = tk.Button(self, text=u"Buscar", command=self.clickBuscar)  # criamos o objeto botão
        self.botaoBuscar.grid(column=3, row=6)

        # log
        self.var = StringVar()
        self.var.set('')
        self.log_reserva = tk.Label(self, textvariable=self.var)
        self.log_reserva.grid(column=2, row=6, pady=10)

        # visualizar a tabela de retorno

        self.listbox = Listbox(self)
        self.listbox.grid(column=2, columnspan=12, row=7, padx=(40, 10))
        self.listbox.configure(bg='white', width=60)
        self.criarTabela()

    def criarTabela(self):
        self.updateTabela()

    def updateTabela(self):
        self.listbox.delete(0, END)
        self.listbox.insert(END, "    Trecho, Numero Vôo, Aeronave, Origem, Destino")
        lista = getTrechos()

        for item in lista:
            text = '    '
            text += str(item.getIdTrecho()) + ', '
            text += str(item.getNumeroVoo()) + ', '
            text += str(item.getCodigoAeronave()) + ', '
            text += str(item.getAeroportoOrigem()) + ', '
            text += str(item.getAeroportoDestino())
            self.listbox.insert(tk.END, text)

    #funcoes dos clicks
    def inserirBanco(self):
        self.var.set('')
        trecho = (self.entidTrecho_trecho.get())
        numerovoo = (self.enhorarioPartida.get())
        cod_aeronave = (self.ent_codaeronave_trecho.get())
        origem = (self.ent_idorigem_trecho.get()) #fk
        destino =(self.ent_idDestino_trecho.get()) #fk
        #enviar pro banco e voltar com erro ou sucesso
        #se for sucesso
        if trecho == '':
            self.var.set('>>>Favor insira o trecho')
        else:
            if getTrecho(trecho) is None:
                tre = Trecho(trecho, numerovoo, cod_aeronave, origem, destino)
                if insertTrecho(tre):
                    self.var.set('>>>Trecho cadastrado com sucesso')
                    self.entidTrecho_trecho.delete(0, END)
                    self.enhorarioPartida.delete(0, END)
                    self.ent_codaeronave_trecho.delete(0, END)
                    self.ent_idorigem_trecho.delete(0, END)
                    self.ent_idDestino_trecho.delete(0, END)
                    self.updateTabela()
                else:
                    self.var.set('>>>Erro')
            else:
                self.var.set('>>>Trecho já cadastrado')

    def clickAlterar(self):
        self.var.set('')
        trecho = (self.entidTrecho_trecho.get())
        numerovoo = (self.enhorarioPartida.get())
        cod_aeronave = (self.ent_codaeronave_trecho.get())
        origem = (self.ent_idorigem_trecho.get())  # fk
        destino = (self.ent_idDestino_trecho.get())  # fk
        if trecho == '':
            self.var.set('>>>Favor insira o trecho')
        else:
            if getTrecho(trecho) is not None:
                tre = Trecho(trecho, numerovoo, cod_aeronave, origem, destino)
                if updateTrecho(tre):
                    self.var.set('>>>Trecho atualizado com sucesso')
                    self.entidTrecho_trecho.delete(0, END)
                    self.enhorarioPartida.delete(0, END)
                    self.ent_codaeronave_trecho.delete(0, END)
                    self.ent_idorigem_trecho.delete(0, END)
                    self.ent_idDestino_trecho.delete(0, END)
                    self.updateTabela()
                else:
                    self.var.set('>>>Erro')
            else:
                self.var.set('>>>Trecho não cadastrado')

    def clickDeletar(self):
        self.var.set('')
        trecho = (self.entidTrecho_trecho.get())
        numerovoo = (self.enhorarioPartida.get())
        cod_aeronave = (self.ent_codaeronave_trecho.get())
        origem = (self.ent_idorigem_trecho.get())  # fk
        destino = (self.ent_idDestino_trecho.get())  # fk
        if trecho == '':
            self.var.set('>>>Favor insira o trecho')
        else:
            if getTrecho(trecho) is not None:
                tre = Trecho(trecho, numerovoo, cod_aeronave, origem, destino)
                if deleteTrecho(tre):
                    self.var.set('>>>Trecho deletado com sucesso')
                    self.entidTrecho_trecho.delete(0, END)
                    self.enhorarioPartida.delete(0, END)
                    self.ent_codaeronave_trecho.delete(0, END)
                    self.ent_idorigem_trecho.delete(0, END)
                    self.ent_idDestino_trecho.delete(0, END)
                    self.updateTabela()
                else:
                    self.var.set('>>>Erro')
            else:
                self.var.set('>>>Trecho não cadastrado')

    def clickBuscar(self):
        self.var.set('')
        trecho = (self.entidTrecho_trecho.get())
        numerovoo = (self.enhorarioPartida.get())
        cod_aeronave = (self.ent_codaeronave_trecho.get())
        origem = (self.ent_idorigem_trecho.get())  # fk
        destino = (self.ent_idDestino_trecho.get())  # fk
        if trecho == '':
            self.var.set('>>>Favor insira o trecho')
        else:
            tre = getTrecho(trecho)
            if tre is not None:
                self.entidTrecho_trecho.delete(0, END)
                self.enhorarioPartida.delete(0, END)
                self.ent_codaeronave_trecho.delete(0, END)
                self.ent_idorigem_trecho.delete(0, END)
                self.ent_idDestino_trecho.delete(0, END)
                self.entidTrecho_trecho.insert(0, tre.getIdTrecho())
                self.enhorarioPartida.insert(0, tre.getNumeroVoo())
                self.ent_codaeronave_trecho.insert(0, tre.getCodigoAeronave())
                self.ent_idorigem_trecho.insert(0, tre.getAeroportoOrigem())
                self.ent_idDestino_trecho.insert(0, tre.getAeroportoDestino())
                self.var.set('>>>Busca concluida com sucesso')
            else:
                self.var.set('>>>Não foi encontrado nenhum trecho cadastrado com este codigo')



class Tabela_Aeroporto(Toplevel):
    def __init__(self, master=None):
        Toplevel.__init__(self, master=master)

        # Configuração da janela principal
        self.title('Aeroporto')
        self.configure(background='gray94')
        self.geometry('480x540')

        # entradas
        self.txt_codaero_aeroporto = tk.Label(self, text="Cod Aeroporto *")
        self.txt_codaero_aeroporto.grid(column=2, row=0, padx=(120, 10), pady=5)
        self.ent_codaero_aeroporto = tk.Entry(self)
        self.ent_codaero_aeroporto.grid(column=3, row=0,
                                    sticky='EW')

        self.txt_nomeaero_aeroporto= tk.Label(self, text="Nome Aeroporto")
        self.txt_nomeaero_aeroporto.grid(column=2, row=1, padx=(120, 10), pady=5)
        self.ent_nomeaero_aeroporto = tk.Entry(self)
        self.ent_nomeaero_aeroporto.grid(column=3, row=1,
                              sticky='EW')

        self.txt_codCidade_aeroporto = tk.Label(self, text="Codigo Cidade")
        self.txt_codCidade_aeroporto.grid(column=2, row=2, padx=(120, 10), pady=5)
        self.ent_codCidade_aeroporto = tk.Entry(self)
        self.ent_codCidade_aeroporto.grid(column=3, row=2,
                               sticky='EW')

        # Botões /fazer o click deles
        ##command=self.inserirBanco(self.entradacodReserva, self.entradapass, self.entradaprazo) < isso vai depois do text do button, ou algo assim pra setar a func

        self.botaoInserir = tk.Button(self, text=u"Inserir", command=self.inserirBanco)  # criamos o objeto botão
        self.botaoInserir.grid(column=2, row=4, padx=(160, 10), pady=5)

        self.botaoAlterar = tk.Button(self, text=u"Alterar", command=self.clickAlterar)  # criamos o objeto botão
        self.botaoAlterar.grid(column=3, row=4)

        self.botaoExcluir = tk.Button(self, text=u"Excluir", command=self.clickDeletar)  # criamos o objeto botão
        self.botaoExcluir.grid(column=2, row=5, padx=(160, 10), pady=5)

        self.botaoBuscar = tk.Button(self, text=u"Buscar", command=self.clickBuscar)  # criamos o objeto botão
        self.botaoBuscar.grid(column=3, row=5)

        # log
        self.var = StringVar()
        self.var.set('')
        self.log_reserva = tk.Label(self, textvariable=self.var)
        self.log_reserva.grid(column=2, row=6, pady=10)

        # visualizar a tabela de retorno

        self.listbox = Listbox(self)
        self.listbox.grid(column=2, columnspan=12, row=7, padx=(40, 10))
        self.listbox.configure(bg='white', width=60)
        self.criarTabela()

    def criarTabela(self):
        self.updateTabela()

    def updateTabela(self):
        self.listbox.delete(0, END)
        self.listbox.insert(END, "    Cod Aeroporto, Nome Aeroporto, Cidade Aeroporto")
        lista = getAeroportos()

        for item in lista:
            text = '    '
            text += str(item.getCodigo()) + ', '
            text += str(item.getNome()) + ', '
            text += str(item.getCodigoCidade())
            self.listbox.insert(tk.END, text)

    #funcoes dos clicks
    def inserirBanco(self):
        self.var.set('')
        codAero = (self.ent_codaero_aeroporto.get())
        nomeAeroporto = (self.ent_nomeaero_aeroporto.get())
        codCidade = (self.ent_codCidade_aeroporto.get())

        if codAero == '':
            self.var.set('>>>Favor insira o Código do Aeroporto')
        else:
            if getAeroporto(codAero) is None:
                aer = Aeroporto(codAero, nomeAeroporto, codCidade)
                if insertAeroporto(aer):
                    self.var.set('>>>Aeroporto cadastrado com sucesso')
                    self.ent_codaero_aeroporto.delete(0, END)
                    self.ent_codCidade_aeroporto.delete(0, END)
                    self.ent_nomeaero_aeroporto.delete(0, END)
                    self.updateTabela()
                else:
                    self.var.set('>>>Erro')
            else:
                self.var.set('>>>Aeroporto já cadastrado')

    def clickAlterar(self):
        self.var.set('')
        codAero = (self.ent_codaero_aeroporto.get())
        nomeAeroporto = (self.ent_nomeaero_aeroporto.get())
        codCidade = (self.ent_codCidade_aeroporto.get())

        if codAero == '':
            self.var.set('>>>Favor insira o Código do Aeroporto')
        else:
            if getAeroporto(codAero) is not None:
                aer = Aeroporto(codAero, nomeAeroporto, codCidade)
                if updateAeroporto(aer):
                    self.var.set('>>>Aeroporto atualizado com sucesso')
                    self.ent_codaero_aeroporto.delete(0, END)
                    self.ent_codCidade_aeroporto.delete(0, END)
                    self.ent_nomeaero_aeroporto.delete(0, END)
                    self.updateTabela()
                else:
                    self.var.set('>>>Erro')
            else:
                self.var.set('>>>Aeroporto não cadastrado')

    def clickDeletar(self):
        self.var.set('')
        codAero = (self.ent_codaero_aeroporto.get())
        nomeAeroporto = (self.ent_nomeaero_aeroporto.get())
        codCidade = (self.ent_codCidade_aeroporto.get())

        if codAero == '':
            self.var.set('>>>Favor insira o Código do Aeroporto')
        else:
            if getAeroporto(codAero) is not None:
                aer = Aeroporto(codAero, nomeAeroporto, codCidade)
                if deleteAeroporto(aer):
                    self.var.set('>>>Aeroporto deletado com sucesso')
                    self.ent_codaero_aeroporto.delete(0, END)
                    self.ent_codCidade_aeroporto.delete(0, END)
                    self.ent_nomeaero_aeroporto.delete(0, END)
                    self.updateTabela()
                else:
                    self.var.set('>>>Erro')
            else:
                self.var.set('>>>Aeroporto não cadastrado')

    def clickBuscar(self):
        self.var.set('')
        codAero = (self.ent_codaero_aeroporto.get())
        nomeAeroporto = (self.ent_nomeaero_aeroporto.get())
        codCidade = (self.ent_codCidade_aeroporto.get())
        if codAero == '':
            self.var.set('>>>Favor insira o Código do Aeroporto')
        else:
            aer = getAeroporto(codAero)
            if aer is not None:
                self.var.set('>>>Aeroporto encontrado com sucesso')
                self.ent_codaero_aeroporto.delete(0, END)
                self.ent_codCidade_aeroporto.delete(0, END)
                self.ent_nomeaero_aeroporto.delete(0, END)
                self.ent_codaero_aeroporto.insert(0, aer.get)
                self.ent_codCidade_aeroporto.insert(0, aer.getCodigoCidade())
                self.ent_nomeaero_aeroporto.insert(0, aer.getNome())
            else:
                self.var.set('>>>Aeroporto não cadastrado')


class Tabela_Cidade(Toplevel):
    def __init__(self, master=None):
        Toplevel.__init__(self, master=master)

        # Configuração da janela principal
        self.title('Cidade')
        self.configure(background='gray94')
        self.geometry('480x540')

        # entradas
        self.txt_codcidade_cidade = tk.Label(self, text="Cod Cidade *")
        self.txt_codcidade_cidade.grid(column=2, row=0, padx=(120, 10), pady=5)
        self.ent_codcidade_cidade = tk.Entry(self)
        self.ent_codcidade_cidade.grid(column=3, row=0,
                                    sticky='EW')

        self.txt_nomecidade_cidade= tk.Label(self, text="Nome Cidade")
        self.txt_nomecidade_cidade.grid(column=2, row=1, padx=(120, 10), pady=5)
        self.ent_nomecidade_cidade = tk.Entry(self)
        self.ent_nomecidade_cidade.grid(column=3, row=1,
                              sticky='EW')

        self.txt_nomepais_cidade = tk.Label(self, text="Pais Cidade")
        self.txt_nomepais_cidade.grid(column=2, row=2, padx=(120, 10), pady=5)
        self.ent_nomepais_cidade = tk.Entry(self)
        self.ent_nomepais_cidade.grid(column=3, row=2,
                               sticky='EW')

        # Botões /fazer o click deles
        ##command=self.inserirBanco(self.entradacodReserva, self.entradapass, self.entradaprazo) < isso vai depois do text do button, ou algo assim pra setar a func

        self.botaoInserir = tk.Button(self, text=u"Inserir", command=self.clickAlterar)  # criamos o objeto botão
        self.botaoInserir.grid(column=2, row=4, padx=(160, 10), pady=5)

        self.botaoAlterar = tk.Button(self, text=u"Alterar", command=self.clickAlterar)  # criamos o objeto botão
        self.botaoAlterar.grid(column=3, row=4)

        self.botaoExcluir = tk.Button(self, text=u"Excluir", command=self.clickDeletar)  # criamos o objeto botão
        self.botaoExcluir.grid(column=2, row=5, padx=(160, 10), pady=5)

        self.botaoBuscar = tk.Button(self, text=u"Buscar", command=self.clickBuscar)  # criamos o objeto botão
        self.botaoBuscar.grid(column=3, row=5)

        # log
        self.var = StringVar()
        self.var.set('')
        self.log_reserva = tk.Label(self, textvariable=self.var)
        self.log_reserva.grid(column=2, row=6, pady=10)

        # visualizar a tabela de retorno

        self.listbox = Listbox(self)
        self.listbox.grid(column=2, columnspan=12, row=7, padx=(40, 10))
        self.listbox.configure(bg='white', width=60, borderwidth=30)
        self.criarTabela()

    def criarTabela(self):
        self.updateTabela()

    def updateTabela(self):
        self.listbox.delete(0, END)
        self.listbox.insert(END, "    ID, Cidade, País")
        lista = getCidades()

        for item in lista:
            text = '    '
            text += str(item.getCodigo()) + ', '
            text += str(item.getNome()) + ', '
            text += str(item.getPais())
            self.listbox.insert(tk.END, text)

        # funcoes dos clicks
        def inserirBanco(self, codreserva, passageiro, prazo):
            pass

    #funcoes dos clicks
    def inserirBanco(self):
        self.var.set('')
        codCidade = (self.ent_codcidade_cidade.get())
        nomeCidade = (self.ent_nomecidade_cidade.get())
        nomePais = (self.ent_nomepais_cidade.get())
        if codCidade == '':
            self.var.set('>>>Favor insira o Código da Cidade')
        else:
            if getCidade(codCidade) is None:
                cid = Cidade(codCidade, nomeCidade, nomePais)
                if insertCidade(cid):
                    self.var.set('>>>Cidade cadastrada com sucesso')
                    self.ent_codcidade_cidade.delete(0, END)
                    self.ent_nomecidade_cidade.delete(0, END)
                    self.ent_nomepais_cidade.delete(0, END)
                    self.updateTabela()
                else:
                    self.var.set('>>>Erro')
            else:
                self.var.set('>>>Cidade já cadastrada')

    def clickAlterar(self):
        self.var.set('')
        codCidade = (self.ent_codcidade_cidade.get())
        nomeCidade = (self.ent_nomecidade_cidade.get())
        nomePais = (self.ent_nomepais_cidade.get())
        if codCidade == '':
            self.var.set('>>>Favor insira o Código da Cidade')
        else:
            if getCidade(codCidade) is not None:
                cid = Cidade(codCidade, nomeCidade, nomePais)
                if updateCidade(cid):
                    self.var.set('>>>Cidade atualizada com sucesso')
                    self.ent_codcidade_cidade.delete(0, END)
                    self.ent_nomecidade_cidade.delete(0, END)
                    self.ent_nomepais_cidade.delete(0, END)
                    self.updateTabela()
                else:
                    self.var.set('>>>Erro')
            else:
                self.var.set('>>>Cidade não cadastrada')

    def clickDeletar(self):
        self.var.set('')
        codCidade = (self.ent_codcidade_cidade.get())
        nomeCidade = (self.ent_nomecidade_cidade.get())
        nomePais = (self.ent_nomepais_cidade.get())
        if codCidade == '':
            self.var.set('>>>Favor insira o Código da Cidade')
        else:
            if getCidade(codCidade) is not None:
                cid = Cidade(codCidade, nomeCidade, nomePais)
                if deleteCidade(cid):
                    self.var.set('>>>Cidade deletada com sucesso')
                    self.ent_codcidade_cidade.delete(0, END)
                    self.ent_nomecidade_cidade.delete(0, END)
                    self.ent_nomepais_cidade.delete(0, END)
                    self.updateTabela()
                else:
                    self.var.set('>>>Erro')
            else:
                self.var.set('>>>Cidade não cadastrada')

    def clickBuscar(self):
        self.var.set('')
        codCidade = (self.ent_codcidade_cidade.get())
        nomeCidade = (self.ent_nomecidade_cidade.get())
        nomePais = (self.ent_nomepais_cidade.get())
        if codCidade == '':
            self.var.set('>>>Favor insira o Código da Cidade')
        else:
            cid = getCidade(codCidade)
            if cid is not None:
                self.var.set('>>>Cidade encontrada com sucesso')
                self.ent_codcidade_cidade.delete(0, END)
                self.ent_nomecidade_cidade.delete(0, END)
                self.ent_nomepais_cidade.delete(0, END)
                self.ent_codcidade_cidade.insert(0, cid.getCodigo())
                self.ent_nomecidade_cidade.insert(0, cid.getNome())
                self.ent_nomepais_cidade.insert(0, cid.getPais())
            else:
                self.var.set('>>>Cidade não cadastrada')


class Tabela_Aeronave(Toplevel):
    def __init__(self, master=None):
        Toplevel.__init__(self, master=master)

        # Configuração da janela principal
        self.title('Tipo Aeronave')
        self.configure(background='gray94')
        self.geometry('480x540')

        # entradas
        self.txt_codaeronave_aernonave = tk.Label(self, text="Cod Aeronave *")
        self.txt_codaeronave_aernonave.grid(column=2, row=0, padx=(120, 10), pady=5)
        self.ent_codaeronave_aernonave = tk.Entry(self)
        self.ent_codaeronave_aernonave.grid(column=3, row=0,
                                    sticky='EW')

        self.txt_descaeronave_aernonave= tk.Label(self, text="Descrição Aeronave")
        self.txt_descaeronave_aernonave.grid(column=2, row=1, padx=(120, 10), pady=5)
        self.ent_descaeronave_aernonave = tk.Entry(self)
        self.ent_descaeronave_aernonave.grid(column=3, row=1,
                              sticky='EW')

        # Botões /fazer o click deles
        ##command=self.inserirBanco(self.entradacodReserva, self.entradapass, self.entradaprazo) < isso vai depois do text do button, ou algo assim pra setar a func

        self.botaoInserir = tk.Button(self, text=u"Inserir", command=self.inserirBanco)  # criamos o objeto botão
        self.botaoInserir.grid(column=2, row=4, padx=(160, 10), pady=5)

        self.botaoAlterar = tk.Button(self, text=u"Alterar", command=self.clickAlterar)  # criamos o objeto botão
        self.botaoAlterar.grid(column=3, row=4)

        self.botaoExcluir = tk.Button(self, text=u"Excluir", command=self.clickDeletar)  # criamos o objeto botão
        self.botaoExcluir.grid(column=2, row=5, padx=(160, 10), pady=5)

        self.botaoBuscar = tk.Button(self, text=u"Buscar", command=self.clickBuscar)  # criamos o objeto botão
        self.botaoBuscar.grid(column=3, row=5)

        # log
        self.var = StringVar()
        self.var.set('')
        self.log_reserva = tk.Label(self, textvariable=self.var)
        self.log_reserva.grid(column=2, row=6, pady=10)

        # visualizar a tabela de retorno

        self.listbox = Listbox(self)
        self.listbox.grid(column=2, columnspan=12, row=7, padx=(40, 10))
        self.listbox.configure(bg='white', width=60, borderwidth=30)
        self.criarTabela()

    def criarTabela(self):
        self.updateTabela()

    def updateTabela(self):
        self.listbox.delete(0, END)
        self.listbox.insert(END, "    código Aeronave, Descrição")
        lista = getTipoAeronaves()

        for item in lista:
            text = '    '
            text += str(item.getCodigo()) + ', '
            text += str(item.getDescricao())
            self.listbox.insert(tk.END, text)

    #funcoes dos clicks
    def inserirBanco(self):
        self.var.set('')
        codAeronave = (self.ent_codaeronave_aernonave.get())
        descAeronave = (self.ent_descaeronave_aernonave.get())

        if codAeronave == '':
            self.var.set('>>>Favor insira o Código da Aeronave')
        else:
            if getTipoAeronave(codAeronave) is None:
                aer = TipoAeronave(codAeronave, descAeronave)
                if insertTipoAeronave(aer):
                    self.var.set('>>>Aeronave cadastrada com sucesso')
                    self.ent_codaeronave_aernonave.delete(0, END)
                    self.ent_descaeronave_aernonave.delete(0, END)
                    self.updateTabela()
                else:
                    self.var.set('>>>Erro')
            else:
                self.var.set('>>>Aeronave já cadastrada')

    def clickAlterar(self):
        self.var.set('')
        codAeronave = (self.ent_codaeronave_aernonave.get())
        descAeronave = (self.ent_descaeronave_aernonave.get())

        if codAeronave == '':
            self.var.set('>>>Favor insira o Código da Aeronave')
        else:
            if getTipoAeronave(codAeronave) is not None:
                aer = TipoAeronave(codAeronave, descAeronave)
                if updateTipoAeronave(aer):
                    self.var.set('>>>Aeronave atualizada com sucesso')
                    self.ent_codaeronave_aernonave.delete(0, END)
                    self.ent_descaeronave_aernonave.delete(0, END)
                    self.updateTabela()
                else:
                    self.var.set('>>>Erro')
            else:
                self.var.set('>>>Aeronave não cadastrada')

    def clickDeletar(self):
        self.var.set('')
        codAeronave = (self.ent_codaeronave_aernonave.get())
        descAeronave = (self.ent_descaeronave_aernonave.get())

        if codAeronave == '':
            self.var.set('>>>Favor insira o Código da Aeronave')
        else:
            if getTipoAeronave(codAeronave) is not None:
                aer = TipoAeronave(codAeronave, descAeronave)
                if deleteTipoAeronave(aer):
                    self.var.set('>>>Aeronave deletada com sucesso')
                    self.ent_codaeronave_aernonave.delete(0, END)
                    self.ent_descaeronave_aernonave.delete(0, END)
                    self.updateTabela()
                else:
                    self.var.set('>>>Erro')
            else:
                self.var.set('>>>Aeronave não cadastrada')

    def clickBuscar(self):
        self.var.set('')
        codAeronave = (self.ent_codaeronave_aernonave.get())
        descAeronave = (self.ent_descaeronave_aernonave.get())

        if codAeronave == '':
            self.var.set('>>>Favor insira o Código da Aeronave')
        else:
            aer = getTipoAeronave(codAeronave)
            if aer is not None:
                self.var.set('>>>Aeronave encontrada com sucesso')
                self.ent_codaeronave_aernonave.delete(0, END)
                self.ent_descaeronave_aernonave.delete(0, END)
                self.ent_codaeronave_aernonave.insert(0, aer.getCodigo())
                self.ent_descaeronave_aernonave.insert(0, aer.getDescricao())
                self.updateTabela()
            else:
                self.var.set('>>>Aeronave não cadastrada')


class Tabela_Aeronave_Lugar(Toplevel):
    def __init__(self, master=None):
        Toplevel.__init__(self, master=master)

        # Configuração da janela principal
        self.title('Aeronave_Lugar')
        self.configure(background='gray94')
        self.geometry('480x540')

        # entradas
        self.txt_codaeronave_aeroLugar = tk.Label(self, text="Cod Aeronave *")
        self.txt_codaeronave_aeroLugar.grid(column=2, row=0, padx=(120, 10), pady=5)
        self.ent_codaeronave_aeroLugar = tk.Entry(self)
        self.ent_codaeronave_aeroLugar.grid(column=3, row=0,
                                    sticky='EW')

        self.txt_idAssento_aeroLugar= tk.Label(self, text="ID Assento") #select?
        self.txt_idAssento_aeroLugar.grid(column=2, row=1, padx=(120, 10), pady=5)
        self.ent_idAssento_aeroLugar = tk.Entry(self)
        self.ent_idAssento_aeroLugar.grid(column=3, row=1,
                              sticky='EW')



        # Botões /fazer o click deles
        ##command=self.inserirBanco(self.entradacodReserva, self.entradapass, self.entradaprazo) < isso vai depois do text do button, ou algo assim pra setar a func

        self.botaoInserir = tk.Button(self, text=u"Inserir", command=self.inserirBanco)  # criamos o objeto botão
        self.botaoInserir.grid(column=2, row=4, padx=(160, 10), pady=5)

        self.botaoAlterar = tk.Button(self, text=u"Alterar", command=self.clickAlterar)  # criamos o objeto botão
        self.botaoAlterar.grid(column=3, row=4)

        self.botaoExcluir = tk.Button(self, text=u"Excluir", command=self.clickDeletar)  # criamos o objeto botão
        self.botaoExcluir.grid(column=2, row=5, padx=(160, 10), pady=5)

        self.botaoBuscar = tk.Button(self, text=u"Buscar", command=self.clickBuscar)  # criamos o objeto botão
        self.botaoBuscar.grid(column=3, row=5)

        # log
        self.var = StringVar()
        self.var.set('')
        self.log_reserva = tk.Label(self, textvariable=self.var)
        self.log_reserva.grid(column=2, row=6, pady=10)

        # visualizar a tabela de retorno

        self.listbox = Listbox(self)
        self.listbox.grid(column=2, columnspan=12, row=7, padx=(40, 10))
        self.listbox.configure(bg='white', width=60, borderwidth=30)
        self.criarTabela()

    def criarTabela(self):
        self.updateTabela()

    def updateTabela(self):
        self.listbox.delete(0, END)
        self.listbox.insert(END, "    código Aeronave, ID Assento")
        lista = getTipoAeronaveAssentos()

        for item in lista:
            text = '    '
            text += str(item.getCodAeronave()) + ', '
            text += str(item.getIdAssento())
            self.listbox.insert(tk.END, text)

    #funcoes dos clicks
    def inserirBanco(self):
        self.var.set('')
        codaero = (self.ent_codaeronave_aeroLugar.get())
        codasse = (self.ent_idAssento_aeroLugar.get())

        if codaero == '' or codasse == '':
            self.var.set('>>>Favor insira o Codigo da Aeronave e o numero do assento')
        else:
            if getTipoAeronaveAssento(codaero, codasse) is None:
                aer = TipoAeronaveAssento(codaero, codasse)
                if insertTipoAeronaveAssento(aer):
                    self.var.set('>>>Aeronave-assento cadastrada com sucesso')
                    self.ent_codaeronave_aeroLugar.delete(0, END)
                    self.ent_idAssento_aeroLugar.delete(0, END)
                    self.updateTabela()
                else:
                    self.var.set('>>>Erro')
            else:
                self.var.set('>>>Aeronave-assento já cadastrada')

    def clickAlterar(self):
        self.var.set('')
        self.var.set('>>>Não é possivel atualizar um Aeronave-assento')
        codaero = (self.ent_codaeronave_aeroLugar.get())
        codasse = (self.ent_idAssento_aeroLugar.get())

    def clickDeletar(self):
        self.var.set('')
        codaero = (self.ent_codaeronave_aeroLugar.get())
        codasse = (self.ent_idAssento_aeroLugar.get())

        if codaero == '' or codasse == '':
            self.var.set('>>>Favor insira o Codigo da Aeronave e o numero do assento')
        else:
            if getTipoAeronaveAssento(codaero, codasse) is not None:
                aer = TipoAeronaveAssento(codaero, codasse)
                if deleteTipoAeronaveAssento(aer):
                    self.var.set('>>>Aeronave-assento deletado com sucesso')
                    self.ent_codaeronave_aeroLugar.delete(0, END)
                    self.ent_idAssento_aeroLugar.delete(0, END)
                    self.updateTabela()
                else:
                    self.var.set('>>>Erro')
            else:
                self.var.set('>>>Aeronave-assento não cadastrada')

    def clickBuscar(self):
        self.var.set('')
        codaero = (self.ent_codaeronave_aeroLugar.get())
        codasse = (self.ent_idAssento_aeroLugar.get())

        if codaero == '' or codasse == '':
            self.var.set('>>>Favor insira o Codigo da Aeronave e o numero do assento')
        else:
            aer = getTipoAeronaveAssento(codaero, codasse)
            if aer is not None:
                self.var.set('>>>Aeronave-assento encontrado com sucesso')
            else:
                self.var.set('>>>Aeronave-assento não cadastrada')


class MainWindow(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, master=None)

        # Configuração da janela principal
        self.master.title('Escolha a Tabela')
        self.master.geometry('480x240')
        self.configure(borderwidth=4)
        self.configure(background='gray94')

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

        for name in ("Reserva", "Reserva Trecho.", "Assento", "Horario", "Vôo"):
            self.button = Button(self.container2, text=name)
            self.button.bind("<Button-1>", self.handle_event)
            self.button.pack(side='left', fill='x', expand=True)

        for name in ("Trecho", "Aeroporto", "Cidade", "Tipo Aeronave", "Aeronave Lugar"):
            self.button = Button(self.container3, text=name)
            self.button.bind("<Button-1>", self.handle_event)
            self.button.pack(side='left', fill='x', expand=True)

        # Empacotamos o frame principal
        self.pack(fill='both', expand=True)

    #select dos botões
    def handle_event(self, event):
        btn_name = event.widget.cget('text')
        if btn_name.endswith('Reserva'):
            window = TabelaReserva()
        if btn_name.endswith('Reserva Trecho.'):
            window = Tabela_Reserva_Tsch()
        if btn_name.endswith('Assento'):
            window = Tabela_Assento()
        if btn_name.endswith('Horario'):
            window = Tabela_Horario()
        if btn_name.endswith('Vôo'):
            window = Tabela_Voo()
        if btn_name.endswith('Trecho'):
            window = Tabela_Trecho()
        if btn_name.endswith('Aeroporto'):
            window = Tabela_Aeroporto()
        if btn_name.endswith('Cidade'):
            window = Tabela_Cidade()
        if btn_name.endswith('Tipo Aeronave'):
            window = Tabela_Aeronave()
        if btn_name.endswith('Aeronave Lugar'):
            window = Tabela_Aeronave_Lugar()

        window.mainloop()


if __name__ == '__main__':
    mainWindow = MainWindow()
mainWindow.mainloop()



#codigo pra colocar o select na entrada
# listaValores = ["laranja", "limão", "jabuticaba", "manga"]
# self.cbx = ttk.Combobox(self.mainframe, values=listaValores)
# self.cbx.set("limão")
# self.cbx.pack()