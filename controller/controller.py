from mysql.connector import MySQLConnection, Error
from dbreader import read_db_config
from models.Cidade import Cidade
from models.Assento import Assento
from models.Horario import Horario


def insertCidade(cidade):
    query = 'INSERT INTO cidade(codCidade, nomeCidade, paisCidade) VALUES(%s, %s, %s)'
    args = (cidade.getCodigo(), cidade.getNome(), cidade.getPais())

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        conn.commit()

    except Error as e:
        raise Exception(e)

    finally:
        cursor.close()
        conn.close()


def updateCidade(cidade):

    query = 'UPDATE cidade SET nomeCidade = %s, paisCidade = %s WHERE codCidade = %s'
    args = (cidade.getNome(), cidade.getPais(), cidade.getCodigo())

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        conn.commit()

    except Error as e:
        raise Exception(e)

    finally:
        cursor.close()
        conn.close()


def deleteCidade(cidade):

    query = 'DELETE FROM cidade WHERE codCidade = %s'
    args = (cidade.getCodigo(), )

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        conn.commit()

    except Error as e:
        raise Exception(e)

    finally:
        cursor.close()
        conn.close()


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
            cidade = Cidade()
            cidade.setCodigo(row[0])
            cidade.setNome(row[1])
            cidade.setPais(row[2])
            cidades.append(cidade)

    except Error as e:
        raise Exception(e)

    finally:
        cursor.close()
        conn.close()
        return cidades


def insertAssento(assento):

    query = 'INSERT INTO assento(numero, classe) VALUES(%s, %s)'
    args = (assento.getNumero(), assento.getClasse())

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        conn.commit()

    except Error as e:
        raise Exception(e)

    finally:
        cursor.close()
        conn.close()


def updateAssento(assento):

    query = 'UPDATE assento SET numero = %s, classe = %s'
    args = (assento.getNumero(), assento.getClasse())

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        conn.commit()

    except Error as e:
        raise Exception(e)

    finally:
        cursor.close()
        conn.close()


def deleteAssento(assento):

    query = 'DELETE FROM assento WHERE numero = %s'
    args = (assento.getNumero(), )

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        conn.commit()

    except Error as e:
        raise Exception(e)

    finally:
        cursor.close()
        conn.close()


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
            assento = Assento()
            assento.setNumero(row[0])
            assento.setClasse(row[1])
            assentos.append(assento)

    except Error as e:
        raise Exception(e)

    finally:
        cursor.close()
        conn.close()
        return assentos


def insertHorario(horario):

    query = 'INSERT INTO horario(diaSemana, horarioPartida, horarioChegada, idTrecho) VALUES(%s, %s, %s, %s)'
    args = (horario.getDiaSemana(), horario.getHorarioPartida(), horario.getHorarioChegada(), horario.getIdTrecho())

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        conn.commit()

    except Error as e:
        raise Exception(e)

    finally:
        cursor.close()
        conn.close()


def updateHorario(horario):

    query = 'UPDATE horario SET horarioPartida = %s, horarioChegada = %s, idTrecho = %s WHERE diaSemana = %s'
    args = (horario.getHorarioPartida(), horario.getHorarioChegada(), horario.getIdTrecho(), horario.getDiaSemana())

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        conn.commit()

    except Error as e:
        raise Exception(e)

    finally:
        cursor.close()
        conn.close()


def deleteHorario(horario):

    query = 'DELETE FROM horario WHERE diaSemana = %s'
    args = (horario.getDiaSemana(), )

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        conn.commit()

    except Error as e:
        raise Exception(e)

    finally:
        cursor.close()
        conn.close()


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
            horario = Horario()
            horario.setDiaSemana(row[0])
            horario.setHorarioPartida(row[1])
            horario.setHorarioChegada(row[2])
            horario.setIdTrecho(row[3])
            horarios.append(horario)

    except Error as e:
        raise Exception(e)

    finally:
        cursor.close()
        conn.close()
        return horarios
