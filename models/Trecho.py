class Trecho:
    def __init__(self, idTrecho = None, numVoo = None, codAeronave = None, aeroportoOrigem = None, aeroportoDestino = None):
        self._idTrecho = idTrecho
        self._numeroVoo = numVoo
        self._codigoAeronave = codAeronave
        self._AeroportoOrigem = aeroportoOrigem
        self._AeroportoDestino = aeroportoDestino

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