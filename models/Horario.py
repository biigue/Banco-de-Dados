class Horario:
    def __init__(self):
        self._diaSemana = None
        self._horarioPartida = None
        self._horarioChegada = None

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