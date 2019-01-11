class Reserva:
    def __init__(self, codReserva = None, passageiro = None, prazo = None):
        self._codigoReserva = codReserva
        self._passageiro = passageiro
        self._prazo = prazo

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