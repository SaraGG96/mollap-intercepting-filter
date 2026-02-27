from src.tasques import Tasques

class ProgramadorTasques:

    def __init__(self, target):
        self.tasques = Tasques()
        self.tasques.setTarget(target)
    
    def getTasques(self):
        return self.tasques
    
    def setTasca(self, filter):
        self.tasques.afegirTasca(filter)
    
    def executarTasques(self, username):
        self.tasques.execucio(username)