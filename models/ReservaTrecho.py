class ReservaTrecho:
    def __init__(self, data = None, codReserva = None, numAssento = None, idTrecho = None):
        self._data = data
        self._codigoReserva = codReserva
        self._numeroAssento = numAssento
        self._idTrecho = idTrecho
        
    def getData(self):
        return self._data

    def setData(self, data):
        self._data = data
    
    def getCodigoReserva(self):
        return self._codigoReserva

    def setCodigoReserva(self, codigoReserva):
        self._codigoReserva = codigoReserva
    
    def getNumeroAssento(self):
        return self._numeroAssento

    def setNumeroAssento(self, numeroAssento):
        self._numeroAssento = numeroAssento
    
    def getIdTrecho(self):
        return self._idTrecho
    
    def setIdTrecho(self, idTrecho):
        self._idTrecho = idTrecho