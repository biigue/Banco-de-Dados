class Assento:
    def __init__(self):
        self._numero = None
        self._classe = None

    def getNumero(self):
        return self._numero

    def setNumero(self, numero):
        self._numero = numero

    def getClasse(self):
        return self._classe

    def setClasse(self, classe):
        self._classe = classe