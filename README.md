# Mollapp - Intercepting Filter

Sara García Garrido — [SaraGG96](https://github.com/SaraGG96)

## Resumen
Este proyecto implementa el patron Intercepting Filter en Python. La idea es que una peticion pase por una cadena de filtros (autenticacion, autorizacion, etc.) antes de llegar al objetivo final (el target). Aqui se modela una app cliente (Mollapp) que dispara una peticion, un programador de tareas que ejecuta filtros en orden, y un target que realiza la accion final.

## Estructura del proyecto
- `main.py`: punto de entrada, crea objetos y dispara la peticion.
- `src/client.py`: interfaz base del cliente.
- `src/mollapp.py`: implementa el cliente que envia peticiones.
- `src/programador_tasques.py`: programador que arma y ejecuta la cadena de filtros.
- `src/tasques.py`: contenedor de filtros y target final.
- `src/filter.py`: define la interfaz `Filter` y filtros concretos.
- `src/target.py`: define el target abstracto y el target real (`Vehicle`).

## Diseño aplicado (Intercepting Filter)
El flujo general queda asi:
1. El cliente crea una peticion y la envia.
2. El programador ejecuta todos los filtros en orden.
3. Cada filtro procesa la peticion y decide si continuar.
4. Al final se ejecuta el target con la misma peticion.

En este ejercicio:
- Los filtros son `Autenticacio` y `Autoritzacio`.
- El target es `Vehicle`, que simula abrir una puerta.
- La peticion se representa con el `username`.

## Paso a paso de la implementacion

### 1) Modelado de interfaces base
Primero defino las clases base para separar responsabilidades:
- `Client` con los metodos `setProgramadorTasques()` y `enviarPeticio()`.
- `Filter` con el metodo `execucio()`.
- `Target` con el metodo `execucio()`.

Esto permite que el flujo sea desacoplado: el cliente no sabe detalles de filtros ni del target, solo invoca el programador de tareas.

### 2) Filtros concretos
En `src/filter.py` implemente dos filtros:
- `Autenticacio`: valida la identidad (simulada con un print).
- `Autoritzacio`: valida permisos (simulada con un print).

Cada filtro implementa `execucio(username)` y deja el sistema listo para el siguiente paso.

### 3) Target real
En `src/target.py` cree `Vehicle`, que representa el recurso protegido. Su `execucio()` imprime que la puerta esta abierta para el usuario.

### 4) Contenedor de tareas
En `src/tasques.py` defini una lista de filtros y una referencia al target. El metodo `execucio()`:
- Recorre los filtros en orden y ejecuta cada uno.
- Al final llama al target.

Este componente es el nucleo del patron porque mantiene el orden y asegura que el target se ejecute solo despues de los filtros.

### 5) Programador de tareas
En `src/programador_tasques.py` cree `ProgramadorTasques`, que encapsula la configuracion de filtros y target:
- Crea `Tasques` y le asigna el target.
- Exponer `setTasca()` para agregar filtros.
- Ejecutar `executarTasques()` para lanzar el flujo completo.

Esto separa la configuracion del flujo de la ejecucion del cliente.

### 6) Cliente (Mollapp)
En `src/mollapp.py` implementé `Mollapp` que solo ve el programador de tareas.   
Cuando se llama a `enviarPeticio(username)`, delega toda la ejecucion al programador.

### 7) Ejecución en `main.py`
El `main.py` arma toda la cadena:
1. Crea el target (`Vehicle`).
2. Crea el programador con el target.
3. Crea filtros y los registra en orden.
4. Crea `Mollapp` y le pasa el programador.
5. Envia la peticion con un `username`.

Asi queda claro el orden de ejecucion y la separacion de responsabilidades.

## Como ejecutar
Desde la raiz del proyecto:
```bash
python main.py
```

## Ejemplo de salida
```text
Autenticacion OK para Francesc
Autorizacion OK para Francesc
Puerta abierta Francesc!
```
