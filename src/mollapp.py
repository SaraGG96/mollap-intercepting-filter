from src.client import Client

class Mollapp(Client):
    
    def __init__(self):
        self.programador_tasques = None
    
    def setProgramadorTasques(self, programador_tasques):
        self.programador_tasques = programador_tasques
    
