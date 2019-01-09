class TipoAeronave:
    def __init__(self):
        self._codigo = None
        self._descricao = None

    def getCodigo(self):
        return self._codigo

    def setCodigo(self, codigo):
        self._codigo = codigo

    def getDescricao(self):
        return self._descricao

    def setDescricao(self, descricao):
        self._descricao = descricao