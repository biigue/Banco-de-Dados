class Cidade:
    def __init__(self, cod = None, nome = None, pais = None):
        self._codigo = cod
        self._nome = nome
        self._pais = pais

    def getCodigo(self):
        return self._codigo

    def setCodigo(self, codigo):
        self._codigo = codigo

    def getNome(self):
        return self._nome

    def setNome(self, nome):
        self._nome = nome

    def getPais(self):
        return  self._pais

    def setPais(self, pais):
        self._pais = pais
