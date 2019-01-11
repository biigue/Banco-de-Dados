class Aeroporto:
    def __init__(self, cod = None, nome = None, codCidade = None):
        self._codigo = cod
        self._nome = nome
        self._codigoCidade = codCidade

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