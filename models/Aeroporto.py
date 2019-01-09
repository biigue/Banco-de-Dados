class Aeroporto:
    def __init__(self):
        self._codigo = None
        self._nome = None
        self._codigoCidade = None

    def getCodigo(self):
        return self._codigo

    def setCodigo(self, codigo):
        self._codigo = codigo

    def getNome(self):
        return self._nome

    def setNome(self, nome):
        self._nome = nome

    def getCodigoCidade(self):
        return self._codigoCidade

    def setCodigoCidade(self, codigoCidade):
        self._codigoCidade = codigoCidade