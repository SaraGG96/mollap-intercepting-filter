class Tasques:
    
    def __init__(self):
        self.tasques = []  # Lista de filtros
        self.target = None  # Destino final
    
    def getTasques(self):
        return self.tasques
    
    def getTarget(self):
        return self.target
    
    def afegirTasca(self, filter):
        self.tasques.append(filter)
    
    def setTarget(self, target):
        self.target = target
