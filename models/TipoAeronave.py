class TipoAeronave:
    def __init__(self, cod = None, desc = None):
        self._codigo = cod
        self._descricao = desc

    def getCodigo(self):
        return self._codigo

    def setCodigo(self, codigo):
        self._codigo = codigo

    def getDescricao(self):
        return self._descricao

    def setDescricao(self, descricao):
        self._descricao = descricao