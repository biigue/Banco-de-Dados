class Trecho:
    def __init__(self):
        self._idTrecho = None
        self._numeroVoo = None
        self._codigoAeronave = None
        self._AeroportoOrigem = None
        self._AeroportoDestino = None

    def getIdTrecho(self):
        return self._idTrecho

    def setIdTrecho(self, idTrecho):
        self._idTrecho = idTrecho

    def getNumeroVoo(self):
        return self._numeroVoo

    def setNumeroVoo(self, numeroVoo):
        self._numeroVoo = numeroVoo

    def getCodigoAeronave(self):
        return self._codigoAeronave

    def setCodigoAeronave(self, codigoAeronave):
        self._codigoAeronave = codigoAeronave

    def getAeroportoOrigem(self):
        return self._AeroportoOrigem

    def setAeroportoOrigem(self, aeroportoOrigem):
        self._AeroportoOrigem = aeroportoOrigem

    def getAeroportoDestino(self):
        return self._AeroportoDestino

    def setAeroportoDestino(self, aeroportoDestino):
        self._AeroportoDestino = aeroportoDestino