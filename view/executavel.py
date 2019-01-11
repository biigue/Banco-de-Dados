# coding: utf8
from tkinter import *
from tkinter import ttk
import tkinter as tk
#from tkinter import tktable
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
        # table = tktable.Table(parent,
        #                       rows=5,
        #                       cols=5
        #                       )
        # table.pack()



        #funcoes dos clicks
    def inserirBanco(self):
        codReserva = (self.entradacodReserva.get())  # pega as entradas
        passageiro = (self.entradapass.get())
        prazo = (self.entradaprazo.get())
        #enviar pro banco e voltar com erro ou sucesso
        #se for sucesso
        if codReserva == '':
            self.var.set('>>>Favor insira o Código da reserva')
        else:
            reserva = Reserva(codReserva, passageiro, prazo)
            self.entradacodReserva.delete(0, tk.END)
            self.entradapass.delete(0, tk.END) # apaga o campo destino
            self.entradaprazo.delete(0, tk.END)
            insertReserva(reserva)
            #mensagem log
            self.var.set('>>>Cadastro Concluido')#alterar para só funcionar se inserir mesmo
        #else
        #self.var.set('>>>Log do Erro')

    def clickAlterar(self):
        codReserva = (self.entradacodReserva.get())  # pega as entradas
        passageiro = (self.entradapass.get())
        prazo = (self.entradaprazo.get())
        if codReserva == '':
            self.var.set('>>>Favor insira o Código da reserva')
        else:
            reserva = Reserva(codReserva, passageiro, prazo)
            updateReserva(reserva)
            self.var.set('>>>Alteração Realizada')
            self.entradacodReserva.delete(0, tk.END)
            self.entradapass.delete(0, tk.END)  # apaga o campo destino
            self.entradaprazo.delete(0, tk.END)

    def clickDeletar(self):
        codReserva = (self.entradacodReserva.get())  # pega as entradas
        passageiro = (self.entradapass.get())
        prazo = (self.entradaprazo.get())
        if codReserva == '':
            self.var.set('>>>Favor insira o Código da reserva')
        else:
            reserva = Reserva(codReserva)
            deleteReserva(reserva)

    def clickBuscar(self):
        codReserva = (self.entradacodReserva.get())  # pega as entradas
        passageiro = (self.entradapass.get())
        prazo = (self.entradaprazo.get())
        #enviar o comando pro banco e listar na lista de baixo


    #no buscar usar
    #self.entryF.insert(0,str(fFar))


class Tabela_Reserva_Trecho(Toplevel):
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

        self.txcodreserva2 = tk.Label(self, text="Cod Reserva") #fazer o select~?
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

        self.botaoInserir = tk.Button(self, text=u"Inserir")  # criamos o objeto botão
        self.botaoInserir.grid(column=2, row=4, padx=(100, 10), pady=5)

        self.botaoAlterar = tk.Button(self, text=u"Alterar")  # criamos o objeto botão
        self.botaoAlterar.grid(column=3, row=4)

        self.botaoExcluir = tk.Button(self, text=u"Excluir")  # criamos o objeto botão
        self.botaoExcluir.grid(column=2, row=5, padx=(100, 10), pady=5)

        self.botaoBuscar = tk.Button(self, text=u"Buscar")  # criamos o objeto botão
        self.botaoBuscar.grid(column=3, row=5)

        # visualizar a tabela de retorno

        # funcoes dos clicks
        def inserirBanco(self):
            pass


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

        self.botaoInserir = tk.Button(self, text=u"Inserir")  # criamos o objeto botão
        self.botaoInserir.grid(column=2, row=4, padx=(180, 10), pady=5)

        self.botaoAlterar = tk.Button(self, text=u"Alterar")  # criamos o objeto botão
        self.botaoAlterar.grid(column=3, row=4)

        self.botaoExcluir = tk.Button(self, text=u"Excluir")  # criamos o objeto botão
        self.botaoExcluir.grid(column=2, row=5, padx=(180, 10), pady=5)

        self.botaoBuscar = tk.Button(self, text=u"Buscar")  # criamos o objeto botão
        self.botaoBuscar.grid(column=3, row=5)

        # visualizar a tabela de retorno

        # funcoes dos clicks
        def inserirBanco(self, codreserva, passageiro, prazo):
            pass


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

        self.botaoInserir = tk.Button(self, text=u"Inserir")  # criamos o objeto botão
        self.botaoInserir.grid(column=2, row=4, padx=(160, 10), pady=5)

        self.botaoAlterar = tk.Button(self, text=u"Alterar")  # criamos o objeto botão
        self.botaoAlterar.grid(column=3, row=4)

        self.botaoExcluir = tk.Button(self, text=u"Excluir")  # criamos o objeto botão
        self.botaoExcluir.grid(column=2, row=5, padx=(160, 10), pady=5)

        self.botaoBuscar = tk.Button(self, text=u"Buscar")  # criamos o objeto botão
        self.botaoBuscar.grid(column=3, row=5)

        # visualizar a tabela de retorno

        # funcoes dos clicks
        def inserirBanco(self, codreserva, passageiro, prazo):
            pass


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

        self.botaoInserir = tk.Button(self, text=u"Inserir")  # criamos o objeto botão
        self.botaoInserir.grid(column=2, row=4, padx=(160, 10), pady=5)

        self.botaoAlterar = tk.Button(self, text=u"Alterar")  # criamos o objeto botão
        self.botaoAlterar.grid(column=3, row=4)

        self.botaoExcluir = tk.Button(self, text=u"Excluir")  # criamos o objeto botão
        self.botaoExcluir.grid(column=2, row=5, padx=(160, 10), pady=5)

        self.botaoBuscar = tk.Button(self, text=u"Buscar")  # criamos o objeto botão
        self.botaoBuscar.grid(column=3, row=5)

        # visualizar a tabela de retorno

        # funcoes dos clicks
        def inserirBanco(self, codreserva, passageiro, prazo):
            pass


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

        self.botaoInserir = tk.Button(self, text=u"Inserir")  # criamos o objeto botão
        self.botaoInserir.grid(column=2, row=5, padx=(160, 10), pady=5)

        self.botaoAlterar = tk.Button(self, text=u"Alterar")  # criamos o objeto botão
        self.botaoAlterar.grid(column=3, row=5)

        self.botaoExcluir = tk.Button(self, text=u"Excluir")  # criamos o objeto botão
        self.botaoExcluir.grid(column=2, row=6, padx=(160, 10), pady=5)

        self.botaoBuscar = tk.Button(self, text=u"Buscar")  # criamos o objeto botão
        self.botaoBuscar.grid(column=3, row=6)

        # visualizar a tabela de retorno

        # funcoes dos clicks
        def inserirBanco(self, codreserva, passageiro, prazo):
            pass


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

        self.botaoInserir = tk.Button(self, text=u"Inserir")  # criamos o objeto botão
        self.botaoInserir.grid(column=2, row=4, padx=(160, 10), pady=5)

        self.botaoAlterar = tk.Button(self, text=u"Alterar")  # criamos o objeto botão
        self.botaoAlterar.grid(column=3, row=4)

        self.botaoExcluir = tk.Button(self, text=u"Excluir")  # criamos o objeto botão
        self.botaoExcluir.grid(column=2, row=5, padx=(160, 10), pady=5)

        self.botaoBuscar = tk.Button(self, text=u"Buscar")  # criamos o objeto botão
        self.botaoBuscar.grid(column=3, row=5)

        # visualizar a tabela de retorno

        # funcoes dos clicks
        def inserirBanco(self, codreserva, passageiro, prazo):
            pass


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

        self.botaoInserir = tk.Button(self, text=u"Inserir")  # criamos o objeto botão
        self.botaoInserir.grid(column=2, row=4, padx=(160, 10), pady=5)

        self.botaoAlterar = tk.Button(self, text=u"Alterar")  # criamos o objeto botão
        self.botaoAlterar.grid(column=3, row=4)

        self.botaoExcluir = tk.Button(self, text=u"Excluir")  # criamos o objeto botão
        self.botaoExcluir.grid(column=2, row=5, padx=(160, 10), pady=5)

        self.botaoBuscar = tk.Button(self, text=u"Buscar")  # criamos o objeto botão
        self.botaoBuscar.grid(column=3, row=5)

        # visualizar a tabela de retorno

        # funcoes dos clicks
        def inserirBanco(self, codreserva, passageiro, prazo):
            pass


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

        self.botaoInserir = tk.Button(self, text=u"Inserir")  # criamos o objeto botão
        self.botaoInserir.grid(column=2, row=4, padx=(160, 10), pady=5)

        self.botaoAlterar = tk.Button(self, text=u"Alterar")  # criamos o objeto botão
        self.botaoAlterar.grid(column=3, row=4)

        self.botaoExcluir = tk.Button(self, text=u"Excluir")  # criamos o objeto botão
        self.botaoExcluir.grid(column=2, row=5, padx=(160, 10), pady=5)

        self.botaoBuscar = tk.Button(self, text=u"Buscar")  # criamos o objeto botão
        self.botaoBuscar.grid(column=3, row=5)

        # visualizar a tabela de retorno

        # funcoes dos clicks
        def inserirBanco(self, codreserva, passageiro, prazo):
            pass


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

        self.botaoInserir = tk.Button(self, text=u"Inserir")  # criamos o objeto botão
        self.botaoInserir.grid(column=2, row=4, padx=(160, 10), pady=5)

        self.botaoAlterar = tk.Button(self, text=u"Alterar")  # criamos o objeto botão
        self.botaoAlterar.grid(column=3, row=4)

        self.botaoExcluir = tk.Button(self, text=u"Excluir")  # criamos o objeto botão
        self.botaoExcluir.grid(column=2, row=5, padx=(160, 10), pady=5)

        self.botaoBuscar = tk.Button(self, text=u"Buscar")  # criamos o objeto botão
        self.botaoBuscar.grid(column=3, row=5)

        # visualizar a tabela de retorno

        # funcoes dos clicks
        def inserirBanco(self, codreserva, passageiro, prazo):
            pass


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

    #select dos botões
    def handle_event(self, event):
        btn_name = event.widget.cget('text')
        if btn_name.endswith('Reserva'):
            window = TabelaReserva()
        if btn_name.endswith('Reserva Trecho'):
            window = Tabela_Reserva_Trecho()
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