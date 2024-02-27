# Definimos las ciudades y sus distancias iniciales
ciudades = {
    "Arad": {"Zerind": 75, "Timisoara": 118, "Sibiu": 140},
    "Zerind": {"Arad": 75, "Oradea": 71, "Arad": 75},
    "Timisoara": {"Arad": 118, "Lugoj": 111, "Arad": 118},
    "Oradea": {"Zerind": 71, "Sibiu": 151, "Zerind": 71},
    "Lugoj": {"Timisoara": 111, "Mehadia": 70, "Timisoara": 111},
    "Sibiu": {"Arad": 140, "Oradea": 151, "Rimmicu Vilcea": 80, "Fagaras": 99, "Oradea": 151},
    "Mehadia": {"Lugoj": 70, "Dobreta": 75, "Lugoj": 70},
    "Rimmicu Vilcea": {"Sibiu": 80, "Craiova": 146, "Pitesti": 97, "Sibiu": 80},
    "Fagaras": {"Sibiu": 99, "Bucharest": 211, "Sibiu": 99},
    "Dobreta": {"Mehadia": 75, "Craiova": 120, "Mehadia": 75},
    "Craiova": {"Dobreta": 120, "Rimmicu Vilcea": 146, "Pitesti": 138, "Dobreta": 120},
    "Pitesti": {"Rimmicu Vilcea": 97, "Craiova": 138, "Bucharest": 101, "Rimmicu Vilcea": 97},
    "Bucharest": {"Fagaras": 211, "Pitesti": 101, "Giurgiu": 90, "Urziceni": 85, "Pitesti": 101},
    "Giurgiu": {"Bucharest": 90, "Bucharest": 90},
    "Urziceni": {"Bucharest": 85, "Vaslui": 142, "Hirsova": 98, "Bucharest": 85},
    "Vaslui": {"Urziceni": 142, "Lasi": 92, "Urziceni": 142},
    "Hirsova": {"Urziceni": 98, "Eforie": 86, "Urziceni": 98},
    "Lasi": {"Vaslui": 92, "Neamt": 87, "Vaslui": 92},
    "Eforie": {"Hirsova": 86, "Hirsova": 86},
    "Neamt": {"Lasi": 87, "Lasi": 87}
}

# Imprimimos la lista de las ciudades y sus distancias
print("Lista de ciudades y sus distancias:")
for ciudad, vecinos in ciudades.items():
    vecinos_str = ", ".join([f"{vecino} ({distancia})" for vecino, distancia in vecinos.items()])
    print(f"{ciudad}: {vecinos_str}")


#DIJKSTRA
# Función para encontrar la ruta más corta entre dos ciudades
def encontrar_ruta(ciudad_inicio, ciudad_fin):
    # Inicializamos las distancias de todas las ciudades como infinito
    distancias = {ciudad: float('inf') for ciudad in ciudades}

    # La distancia de la ciudad de inicio a sí misma es 0
    distancias[ciudad_inicio] = 0

    # Creamos un diccionario para guardar las ciudades previas en el camino más corto
    previas = {}

    # Creamos un conjunto de ciudades visitadas
    visitadas = set()

    while visitadas != set(ciudades.keys()):
        # Seleccionamos la ciudad no visitada con la distancia más corta
        ciudad_actual = min(ciudades.keys() - visitadas, key=lambda ciudad: distancias[ciudad])

        # Iteramos sobre los vecinos de la ciudad actual
        for vecino, distancia in ciudades[ciudad_actual].items():
            nueva_distancia = distancias[ciudad_actual] + distancia
            if nueva_distancia < distancias[vecino]:
                distancias[vecino] = nueva_distancia
                previas[vecino] = ciudad_actual

        # Marcamos la ciudad actual como visitada
        visitadas.add(ciudad_actual)

    # Construimos la ruta más corta
    ruta = [ciudad_fin]
    while ruta[-1] != ciudad_inicio:
        ruta.append(previas[ruta[-1]])
    ruta.reverse()

    return ruta

# Pedimos al usuario que seleccione las ciudades de origen y destino
ciudad_inicio = input("Ingrese la ciudad de origen: ")
ciudad_fin = input("Ingrese la ciudad de destino: ")

# Encontramos la ruta más corta entre las ciudades seleccionadas por el usuario
ruta_mas_corta= encontrar_ruta(ciudad_inicio, ciudad_fin)

# Imprimimos la ruta más corta encontrada
print(f"\nLa ruta más corta entre {ciudad_inicio} y {ciudad_fin} es: {' -> '.join(ruta_mas_corta)}")
