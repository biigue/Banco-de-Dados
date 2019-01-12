from mysql.connector import MySQLConnection, Error
from controller.dbreader import read_db_config
from models.Cidade import Cidade
from models.Assento import Assento
from models.Horario import Horario
from models.Reserva import Reserva
from models.Aeroporto import Aeroporto
from models.Voo import Voo
from models.TipoAeronave import TipoAeronave
from models.Trecho import Trecho
from models.ReservaTrecho import ReservaTrecho
from models.TipoAeronaveAssento import TipoAeronaveAssento


def insertCidade(cidade):
    query = 'INSERT INTO cidade(codCidade, nomeCidade, paisCidade) VALUES(%s, %s, %s)'
    args = (cidade.getCodigo(), cidade.getNome(), cidade.getPais())

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        conn.commit()

        cursor.close()
        conn.close()
        return True

    except Error as e:
        raise Exception(e)


def updateCidade(cidade):

    query = 'UPDATE cidade SET nomeCidade = %s, paisCidade = %s WHERE codCidade = %s'
    args = (cidade.getNome(), cidade.getPais(), cidade.getCodigo())

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        conn.commit()

        cursor.close()
        conn.close()
        return True

    except Error as e:
        raise Exception(e)


def deleteCidade(cidade):

    query = 'DELETE FROM cidade WHERE codCidade = %s'
    args = (cidade.getCodigo(), )

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        conn.commit()

        cursor.close()
        conn.close()
        return True

    except Error as e:
        raise Exception(e)


def getCidade(id):

    query = 'SELECT * FROM cidade WHERE codCidade = %s'
    args = (id, )

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        if cursor.rowcount > 0:
            row = cursor.fetchone()
            cidade = Cidade(row[0], row[1], row[2])
        else:
            cidade = None

        cursor.close()
        conn.close()
        return cidade

    except Error as e:
        raise Exception(e)


def getCidades():

    query = 'SELECT * FROM cidade'

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query)

        cidades = []
        rows = cursor.fetchall()
        for row in rows:
            cidade = Cidade(row[0], row[1], row[2])
            cidades.append(cidade)

        cursor.close()
        conn.close()
        return cidades

    except Error as e:
        raise Exception(e)


def insertAssento(assento):

    query = 'INSERT INTO assento(numero, classe) VALUES(%s, %s)'
    args = (assento.getNumero(), assento.getClasse())

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        conn.commit()

        cursor.close()
        conn.close()
        return True

    except Error as e:
        raise Exception(e)


def updateAssento(assento):

    query = 'UPDATE assento SET numero = %s, classe = %s'
    args = (assento.getNumero(), assento.getClasse())

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        conn.commit()

        cursor.close()
        conn.close()
        return True

    except Error as e:
        raise Exception(e)

def deleteAssento(assento):

    query = 'DELETE FROM assento WHERE numero = %s'
    args = (assento.getNumero(), )

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        conn.commit()

        cursor.close()
        conn.close()
        return True

    except Error as e:
        raise Exception(e)


def getAssento(id):

    query = 'SELECT * FROM assento WHERE numero = %s'
    args = (id,)

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        if cursor.rowcount > 0:
            row = cursor.fetchone()
            assento = Assento(row[0], row[1])
        else:
            assento = None

        cursor.close()
        conn.close()
        return assento

    except Error as e:
        raise Exception(e)


def getAssentos():

    query = 'SELECT * FROM assento'

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query)

        assentos = []
        rows = cursor.fetchall()
        for row in rows:
            assento = Assento(row[0], row[1])
            assentos.append(assento)

        cursor.close()
        conn.close()
        return assentos

    except Error as e:
        raise Exception(e)


def insertHorario(horario):

    query = 'INSERT INTO horario(diaSemana, horarioPartida, horarioChegada, idTrecho) VALUES(%s, %s, %s, %s)'
    args = (horario.getDiaSemana(), horario.getHorarioPartida(), horario.getHorarioChegada(), horario.getIdTrecho())

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        conn.commit()

        cursor.close()
        conn.close()
        return True

    except Error as e:
        raise Exception(e)


def updateHorario(horario):

    query = 'UPDATE horario SET horarioPartida = %s, horarioChegada = %s, idTrecho = %s WHERE diaSemana = %s'
    args = (horario.getHorarioPartida(), horario.getHorarioChegada(), horario.getIdTrecho(), horario.getDiaSemana())

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        conn.commit()

        cursor.close()
        conn.close()
        return True

    except Error as e:
        raise Exception(e)


def deleteHorario(horario):

    query = 'DELETE FROM horario WHERE diaSemana = %s'
    args = (horario.getDiaSemana(), )

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        conn.commit()

        cursor.close()
        conn.close()
        return True

    except Error as e:
        raise Exception(e)


def getHorario(id):

    query = 'SELECT * FROM horario WHERE diaSemana = %s'
    args = (id,)

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        if cursor.rowcount > 0:
            row = cursor.fetchone()
            horario = Horario(row[0], row[1], row[2], row[3])
        else:
            horario = None

        cursor.close()
        conn.close()
        return horario

    except Error as e:
        raise Exception(e)


def getHorarios():

    query = 'SELECT * FROM horario'

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query)

        horarios = []
        rows = cursor.fetchall()
        for row in rows:
            horario = Horario(row[0], row[1], row[2], row[3])
            horarios.append(horario)

        cursor.close()
        conn.close()
        return horarios

    except Error as e:
        raise Exception(e)


def insertReserva(reserva):

    query = 'INSERT INTO reserva(codReserva, passageiro, prazo) VALUES(%s, %s, %s)'
    args = (reserva.getCodigoReserva(), reserva.getPassageiro(), reserva.getPrazo())

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        conn.commit()

        cursor.close()
        conn.close()
        return True

    except Error as e:
        raise Exception(e)


def updateReserva(reserva):

    query = 'UPDATE reserva SET passageiro = %s, prazo = %s WHERE codReserva = %s'
    args = (reserva.getPassageiro(), reserva.getPrazo(), reserva.getCodigoReserva())

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        conn.commit()

        cursor.close()
        conn.close()
        return True

    except Error as e:
        raise Exception(e)


def deleteReserva(reserva):

    query = 'DELETE FROM reserva WHERE codReserva = %s'
    args = (reserva.getCodigoReserva(), )

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        conn.commit()

        cursor.close()
        conn.close()
        return True

    except Error as e:
        raise Exception(e)


def getReserva(id):

    query = 'SELECT * FROM reserva WHERE codReserva = %s'
    args = (id,)

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        if cursor.rowcount > 0:
            row = cursor.fetchone()
            reserva = Reserva(row[0], row[1], row[2])
        else:
            reserva = None

        cursor.close()
        conn.close()
        return reserva

    except Error as e:
        raise Exception(e)


def getReservas():

    query = 'SELECT * FROM reserva'

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query)

        reservas = []
        rows = cursor.fetchall()
        for row in rows:
            reserva = Reserva(row[0], row[1], row[2])
            reservas.append(reserva)

        cursor.close()
        conn.close()
        return reservas

    except Error as e:
        raise Exception(e)


def insertAeroporto(aeroporto):

    query = 'INSERT INTO aeroporto(codAeroporto, nomeAeroporto, codCidade) VALUES(%s, %s, %s)'
    args = (aeroporto.getCodigo(), aeroporto.getNome(), aeroporto.getCodigoCidade())

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        conn.commit()

        cursor.close()
        conn.close()
        return True

    except Error as e:
        raise Exception(e)


def updateAeroporto(aeroporto):

    query = 'UPDATE aeroporto SET nomeAeroporto = %s, codCidade = %s WHERE codAeroporto = %s'
    args = (aeroporto.getNome(), aeroporto.getCodigoCidade(), aeroporto.getCodigo())

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        conn.commit()

        cursor.close()
        conn.close()
        return True

    except Error as e:
        raise Exception(e)


def deleteAeroporto(aeroporto):

    query = 'DELETE FROM aeroporto WHERE codAeroporto = %s'
    args = (aeroporto.getCodigo(), )

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        conn.commit()

        cursor.close()
        conn.close()
        return True

    except Error as e:
        raise Exception(e)


def getAeroporto(id):

    query = 'SELECT * FROM aeroport WHERE codAeroporto = %s'
    args = (id,)

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        if cursor.rowcount > 0:
            row = cursor.fetchone()
            aeroporto = Aeroporto(row[0], row[1], row[2])
        else:
            aeroporto = None

        cursor.close()
        conn.close()
        return aeroporto

    except Error as e:
        raise Exception(e)


def getAeroportos():

    query = 'SELECT * FROM aeroporto'

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query)

        aeroportos = []
        rows = cursor.fetchall()
        for row in rows:
            aeroporto = Aeroporto(row[0], row[1], row[2])
            aeroportos.append(aeroporto)

        cursor.close()
        conn.close()
        return aeroportos

    except Error as e:
        raise Exception(e)


def insertVoo(voo):

    query = 'INSERT INTO voo(numero) VALUES(%s)'
    args = (voo.getNumero(), )

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        conn.commit()

        cursor.close()
        conn.close()
        return True

    except Error as e:
        raise Exception(e)


def deleteVoo(voo):

    query = 'DELETE FROM voo WHERE numero = %s'
    args = (voo.getNumero(), )

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        conn.commit()

        cursor.close()
        conn.close()
        return True

    except Error as e:
        raise Exception(e)


def getVoo(id):

    query = 'SELECT * FROM voo WHERE numero = %s'
    args = (id,)

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        if cursor.rowcount > 0:
            row = cursor.fetchone()
            voo = Voo(row[0])
        else:
            voo = None

        cursor.close()
        conn.close()
        return voo

    except Error as e:
        raise Exception(e)


def getVoos():

    query = 'SELECT * FROM voo'

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query)

        voos = []
        rows = cursor.fetchall()
        for row in rows:
            voo = Voo(row[0])
            voos.append(voo)

        cursor.close()
        conn.close()
        return voos

    except Error as e:
        raise Exception(e)


def insertTipoAeronave(tipoAeronave):

    query = 'INSERT INTO tipoAeronave(codAeronave, descricaoAeronave) VALUES(%s, %s)'
    args = (tipoAeronave.getCodigo(), tipoAeronave.getDescricao())

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        conn.commit()

        cursor.close()
        conn.close()
        return True

    except Error as e:
        raise Exception(e)


def updateTipoAeronave(tipoAeronave):

    query = 'UPDATE tipoAeronave SET descricaoAeronave = %s WHERE codAeronave = %s'
    args = (tipoAeronave.getDescricao(), tipoAeronave.getCodigo())

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        conn.commit()

        cursor.close()
        conn.close()
        return True

    except Error as e:
        raise Exception(e)


def deleteTipoAeronave(tipoAeronave):

    query = 'DELETE FROM tipoAeronave WHERE codAeronave = %s'
    args = (tipoAeronave.getCodigo(), )

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        conn.commit()

        cursor.close()
        conn.close()
        return True

    except Error as e:
        raise Exception(e)


def getTipoAeronave(id):

    query = 'SELECT * FROM tipoAeronave WHERE codAeronave = %s'
    args = (id,)

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        if cursor.rowcount > 0:
            row = cursor.fetchone()
            tipoAeronave = TipoAeronave(row[0], row[1])
        else:
            tipoAeronave = None

        cursor.close()
        conn.close()
        return tipoAeronave

    except Error as e:
        raise Exception(e)


def getTipoAeronaves():

    query = 'SELECT * FROM tipoAeronave'

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query)

        tipoAeronaves = []
        rows = cursor.fetchall()
        for row in rows:
            tipoAeronave = TipoAeronave(row[0], row[1])
            tipoAeronaves.append(tipoAeronave)

        cursor.close()
        conn.close()
        return tipoAeronaves

    except Error as e:
        raise Exception(e)


def insertTipoAeronaveAssento(tipoAeronaveAssento):

    query = 'INSERT INTO tipoaeronave_assento(codAeronave, idAssento) VALUES(%s, %s)'
    args = (tipoAeronaveAssento.getCodAeronave(), tipoAeronaveAssento.getIdAssento())

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        conn.commit()

        cursor.close()
        conn.close()
        return True

    except Error as e:
        raise Exception(e)


def deleteTipoAeronaveAssento(tipoAeronaveAssento):

    query = 'DELETE FROM tipoaeronave_assento WHERE codAeronave = %s AND idAssento = %s'
    args = (tipoAeronaveAssento.getCodAeronave(), tipoAeronaveAssento.getIdAssento())

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        conn.commit()

        cursor.close()
        conn.close()
        return True

    except Error as e:
        raise Exception(e)


def getTipoAeronave(codAeronave, idAssento):

    query = 'SELECT * FROM tipoaeronave_assento WHERE codAeronave = %s, idAssento = %s'
    args = (codAeronave, idAssento)

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        if cursor.rowcount > 0:
            row = cursor.fetchone()
            tipoAeronaveAssento = TipoAeronaveAssento(row[0], row[1])
        else:
            tipoAeronaveAssento = None

        cursor.close()
        conn.close()
        return tipoAeronaveAssento

    except Error as e:
        raise Exception(e)


def getTipoAeronaveAssentos():

    query = 'SELECT * FROM tipoaeronave_assento'

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query)

        tipoAeronaveAssentos = []
        rows = cursor.fetchall()
        for row in rows:
            tipoAeronaveAssento = TipoAeronaveAssento(row[0], row[1])
            tipoAeronaveAssentos.append(tipoAeronaveAssento)

        cursor.close()
        conn.close()
        return tipoAeronaveAssentos

    except Error as e:
        raise Exception(e)



def insertTrecho(trecho):

    query = 'INSERT INTO trecho(idTrecho, numero, codAeronave, origem, destino) VALUES(%s, %s, %s, %s, %s)'
    args = (trecho.getIdTrecho(), trecho.getNumeroVoo(), trecho.getCodigoAeronave(), trecho.getAeroportoOrigem(), trecho.getAeroportoDestino())

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        conn.commit()

        cursor.close()
        conn.close()
        return True

    except Error as e:
        raise Exception(e)


def updateTrecho(trecho):

    query = 'UPDATE trecho SET numero = %s, codAeronave = %s, origem = %s, destino = %s WHERE idTrecho = %s'
    args = (trecho.getNumeroVoo(), trecho.getCodigoAeronave(), trecho.getAeroportoOrigem(), trecho.getAeroportoDestino(), trecho.getIdTrecho())

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        conn.commit()

        cursor.close()
        conn.close()
        return True

    except Error as e:
        raise Exception(e)


def deleteTrecho(trecho):

    query = 'DELETE FROM trecho WHERE idTrecho = %s'
    args = (trecho.getIdTrecho(), )

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        conn.commit()

        cursor.close()
        conn.close()
        return True

    except Error as e:
        raise Exception(e)


def getTrecho(id):

    query = 'SELECT * FROM trecho WHERE idTrecho = %s'
    args = (id,)

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        if cursor.rowcount > 0:
            row = cursor.fetchone()
            trecho = Trecho(row[0], row[1], row[2], row[3], row[4])
        else:
            trecho = None

        cursor.close()
        conn.close()
        return trecho

    except Error as e:
        raise Exception(e)


def getTrechos():

    query = 'SELECT * FROM trecho'

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query)

        trechos = []
        rows = cursor.fetchall()
        for row in rows:
            trecho = Trecho(row[0], row[1], row[2], row[3], row[4])
            trechos.append(trecho)

        cursor.close()
        conn.close()
        return trechos

    except Error as e:
        raise Exception(e)


def insertReservaTrecho(reservaTrecho):

    query = 'INSERT INTO rvs_trecho(dataRT, codReserva, idAssento, idTrecho) VALUES(%s, %s, %s, %s)'
    args = (reservaTrecho.getData(), reservaTrecho.getCodigoReserva(), reservaTrecho.getIdTrecho(), reservaTrecho.getIdTrecho())

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        conn.commit()

        cursor.close()
        conn.close()
        return True

    except Error as e:
        raise Exception(e)


def updateReservaTrecho(reservaTrecho):

    query = 'UPDATE rvs_trecho SET codReserva = %s, idAssento = %s, idTrecho = %s WHERE dataRT = %s'
    args = (reservaTrecho.getCodigoReserva(), reservaTrecho.getNumeroAssento(), reservaTrecho.getIdTrecho(), reservaTrecho.getData())

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        conn.commit()

        cursor.close()
        conn.close()
        return True

    except Error as e:
        raise Exception(e)


def deleteReservaTrecho(reservaTrecho):

    query = 'DELETE FROM rvs_trecho WHERE dataRT = %s'
    args = (reservaTrecho.getData(), )

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        conn.commit()

        cursor.close()
        conn.close()
        return True

    except Error as e:
        raise Exception(e)

def getReservaTrecho(id):

    query = 'SELECT * FROM rvs_trecho WHERE dataRT = %s'
    args = (id,)

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        if cursor.rowcount > 0:
            row = cursor.fetchone()
            reservaTrecho = ReservaTrecho(row[0], row[1], row[2], row[3])
        else:
            reservaTrecho = None

        cursor.close()
        conn.close()
        return reservaTrecho

    except Error as e:
        raise Exception(e)


def getReservaTrechos():

    query = 'SELECT * FROM rvs_trecho'

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query)

        reservaTrechos = []
        rows = cursor.fetchall()
        for row in rows:
            reservaTrecho = ReservaTrecho(row[0], row[1], row[2], row[3])
            reservaTrechos.append(reservaTrecho)

        cursor.close()
        conn.close()
        return reservaTrechos

    except Error as e:
        raise Exception(e)
