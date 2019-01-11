class Horario:
    def __init__(self, diaS = None, horP = None, horC = None, idTrecho = None):
        self._diaSemana = diaS
        self._horarioPartida = horP
        self._horarioChegada = horC
        self._idTrecho = idTrecho

    def getDiaSemana(self):
        return self._diaSemana

    def setDiaSemana(self, diaSemana):
        self._diaSemana = diaSemana

    def getHorarioPartida(self):
        return self._horarioPartida

    def setHorarioPartida(self, horarioPartida):
        self._horarioPartida = horarioPartida

    def getHorarioChegada(self):
        return self._horarioChegada

    def setHorarioChegada(self, horarioChegada):
        self._horarioChegada = horarioChegada

    def getIdTrecho(self):
        return self._idTrecho

    def setIdTrecho(self, idTrecho):
        self._idTrecho = idTrecho