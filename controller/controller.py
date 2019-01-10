from mysql.connector import MySQLConnection, Error
from dbreader import read_db_config
from models.Cidade import Cidade
from models.Assento import Assento


def connectDB():
    db_config = read_db_config()

    try:
        print('Connecting to MySQL database...')
        conn = MySQLConnection(**db_config)

        if conn.is_connected():
            print('connection established.')
        else:
            print('connection failed.')

    except Error as error:
        print(error)

    finally:
        conn.close()
        print('connection closed.')


def insertCidade(cidade):
    query = 'INSERT INTO cidade(codCidade, nomeCidade, paisCidade) VALUES(%s, %s, %s)'
    args = (city.getCodigo(), city.getNome(), city.getPais())

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


def alterarAssento(assento):

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


def deletarAssento(assento):

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



