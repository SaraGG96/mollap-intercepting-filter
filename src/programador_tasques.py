from src.tasques import Tasques

class ProgramadorTasques:

    def __init__(self, target):
        self.tasques = Tasques()
        self.tasques.setTarget(target)
    
