class Reserva:
    def __init__(self):
        self._codigoReserva = None
        self._passageiro = None
        self._prazo = None

    def getCodigoReserva(self):
        return self._codigoReserva

    def setCodigoReserva(self, codigoReserva):
        self._codigoReserva = codigoReserva

    def getPassageiro(self):
        return self._passageiro

    def setPassageiro(self, passageiro):
        self._passageiro = passageiro

    def getPrazo(self):
        return self._prazo

    def setPrazo(self, prazo):
        self._prazo = prazo