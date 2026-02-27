
from src.target import Vehicle
from src.filter import Autenticacio, Autoritzacio
from src.programador_tasques import ProgramadorTasques
from src.mollapp import Mollapp


def main():
    
    # 1 => Crear el target (vehículo)
    vehicle = Vehicle()
    
    # 2 => crear el programador de tareas con el target
    programador = ProgramadorTasques(vehicle)
    
    # 3 => crear los filtros
    autenticacio = Autenticacio()
    autoritzacio = Autoritzacio()
    
    # 4 => programar las tareas (añadir filtros en orden)
    programador.setTasca(autenticacio)
    programador.setTasca(autoritzacio)
    
    # 5 => crear la aplicación cliente (Mollapp)
    mollapp = Mollapp()
    
    # 6 => configurar el programador en la app
    mollapp.setProgramadorTasques(programador)
    
    # 7 => usuario que solicita acceso
    username = "Francesc"
    
    # 8 => enviar petición desde la app
    mollapp.enviarPeticio(username)


if __name__ == "__main__":
    main()