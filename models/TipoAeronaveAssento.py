class TipoAeronaveAssento:
    def __init__(self, codAeronave = None, idAssento = None):
        self._codAeronave = codAeronave
        self._idAssento = idAssento

    def getCodAeronave(self):
        return self._codAeronave

    def setCodAeronave(self, codAeronave):
        self._codAeronave = codAeronave

    def getIdAssento(self):
        return self._idAssento

    def setIdAssento(self, idAssento):
        self._idAssento = idAssento