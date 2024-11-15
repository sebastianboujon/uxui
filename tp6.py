# Ejercicio 14
class Grafo:
    def __init__(self):
        self.vertices = {}
    
    def agregar_vertice(self, vertice):
        if vertice not in self.vertices:
            self.vertices[vertice] = []

    def agregar_arista(self, origen, destino, peso):
        if origen in self.vertices and destino in self.vertices:
            self.vertices[origen].append((destino, peso))
            self.vertices[destino].append((origen, peso))

    def mostrar_grafo(self):
        for vertice in self.vertices:
            print(f"{vertice} -> {self.vertices[vertice]}")
grafo = Grafo()
ambientes = ["cocina", "comedor", "cochera", "quincho", "baño 1", "baño 2", "habitación 1", "habitación 2", "sala de estar", "terraza", "patio"]
for ambiente in ambientes:
    grafo.agregar_vertice(ambiente)
grafo.agregar_arista("cocina", "comedor", 5)
grafo.agregar_arista("cocina", "baño 1", 8)
grafo.agregar_arista("cocina", "sala de estar", 12)

grafo.mostrar_grafo()

class Grafo:
    def __init__(self):
        self.vertices = {}
        self.aristas = []

    def agregar_vertice(self, vertice):
        if vertice not in self.vertices:
            self.vertices[vertice] = []

    def agregar_arista(self, origen, destino, peso):
        if origen in self.vertices and destino in self.vertices:
            self.vertices[origen].append((destino, peso))
            self.vertices[destino].append((origen, peso))
            self.aristas.append((peso, origen, destino))  # guardo la arista en formato (peso, origen, destino)

    def mostrar_grafo(self):
        for vertice in self.vertices:
            print(f"{vertice} -> {self.vertices[vertice]}")

# funciones auxiliares para Kruskal
class UnionFind:
    def __init__(self, n):
        self.padre = list(range(n))
        self.rango = [0] * n

    def encontrar(self, u):
        if u != self.padre[u]:
            self.padre[u] = self.encontrar(self.padre[u])
        return self.padre[u]

    def union(self, u, v):
        raiz_u = self.encontrar(u)
        raiz_v = self.encontrar(v)
        if raiz_u != raiz_v:
            if self.rango[raiz_u] > self.rango[raiz_v]:
                self.padre[raiz_v] = raiz_u
            else:
                self.padre[raiz_u] = raiz_v
                if self.rango[raiz_u] == self.rango[raiz_v]:
                    self.rango[raiz_v] += 1

def kruskal(grafo):
    union_find = UnionFind(len(grafo.vertices))
    arbol_expansion_minima = []
    costo_total = 0
    
    mapeo_vertices = {vertice: idx for idx, vertice in enumerate(grafo.vertices)}
    
    # Ordeno aristas por peso
    grafo.aristas.sort()
    
    for peso, origen, destino in grafo.aristas:
        u = mapeo_vertices[origen]
        v = mapeo_vertices[destino]
        
        if union_find.encontrar(u) != union_find.encontrar(v):
            union_find.union(u, v)
            arbol_expansion_minima.append((origen, destino, peso))
            costo_total += peso
    
    return arbol_expansion_minima, costo_total

grafo = Grafo()
ambientes = ["cocina", "comedor", "cochera", "quincho", "baño 1", "baño 2", "habitación 1", "habitación 2", "sala de estar", "terraza", "patio"]
for ambiente in ambientes:
    grafo.agregar_vertice(ambiente)

grafo.agregar_arista("cocina", "comedor", 5)
grafo.agregar_arista("cocina", "baño 1", 8)
grafo.agregar_arista("cocina", "sala de estar", 12)
grafo.agregar_arista("comedor", "quincho", 4)
grafo.agregar_arista("comedor", "habitación 1", 7)
grafo.agregar_arista("cochera", "patio", 10)
grafo.agregar_arista("quincho", "patio", 6)
grafo.agregar_arista("baño 1", "baño 2", 3)
grafo.agregar_arista("habitación 1", "habitación 2", 9)
grafo.agregar_arista("sala de estar", "terraza", 11)

print("Grafo completo:")
grafo.mostrar_grafo()

arbol_expansion_minima, costo_total = kruskal(grafo)
print("Árbol de Expansión Mínima:")
for origen, destino, peso in arbol_expansion_minima:
    print(f"{origen} - {destino}: {peso} metros")
print(f"Costo total (metros de cable): {costo_total} metros")

import heapq  

class Grafo:
    def __init__(self):
        self.vertices = {}
        self.aristas = []

    def agregar_vertice(self, vertice):
        if vertice not in self.vertices:
            self.vertices[vertice] = []

    def agregar_arista(self, origen, destino, peso):
        if origen in self.vertices and destino in self.vertices:
            self.vertices[origen].append((destino, peso))
            self.vertices[destino].append((origen, peso))
            self.aristas.append((peso, origen, destino))

    def mostrar_grafo(self):
        for vertice in self.vertices:
            print(f"{vertice} -> {self.vertices[vertice]}")

# Algoritmo de Dijkstra para encontrar el camino más corto
def dijkstra(grafo, inicio, destino):
    distancias = {vertice: float('inf') for vertice in grafo.vertices}
    distancias[inicio] = 0
    cola_prioridad = [(0, inicio)]
    predecesor = {vertice: None for vertice in grafo.vertices}

    while cola_prioridad:
        distancia_actual, vertice_actual = heapq.heappop(cola_prioridad)
        
        if vertice_actual == destino:
            break
        
        for vecino, peso in grafo.vertices[vertice_actual]:
            distancia = distancia_actual + peso
            
            if distancia < distancias[vecino]:
                distancias[vecino] = distancia
                predecesor[vecino] = vertice_actual
                heapq.heappush(cola_prioridad, (distancia, vecino))
    
    camino = []
    paso = destino
    while paso is not None:
        camino.insert(0, paso)
        paso = predecesor[paso]
    
    return camino, distancias[destino]

grafo = Grafo()
ambientes = ["cocina", "comedor", "cochera", "quincho", "baño 1", "baño 2", "habitación 1", "habitación 2", "sala de estar", "terraza", "patio"]
for ambiente in ambientes:
    grafo.agregar_vertice(ambiente)

grafo.agregar_arista("cocina", "comedor", 5)
grafo.agregar_arista("cocina", "baño 1", 8)
grafo.agregar_arista("cocina", "sala de estar", 12)
grafo.agregar_arista("comedor", "quincho", 4)
grafo.agregar_arista("comedor", "habitación 1", 7)
grafo.agregar_arista("cochera", "patio", 10)
grafo.agregar_arista("quincho", "patio", 6)
grafo.agregar_arista("baño 1", "baño 2", 3)
grafo.agregar_arista("habitación 1", "habitación 2", 9)
grafo.agregar_arista("sala de estar", "terraza", 11)

print("Grafo completo:")
grafo.mostrar_grafo()

# Calculo el árbol de expansión mínima (usando Kruskal)
arbol_expansion_minima, costo_total = kruskal(grafo)
print("\nÁrbol de Expansión Mínima:")
for origen, destino, peso in arbol_expansion_minima:
    print(f"{origen} - {destino}: {peso} metros")
print(f"\nCosto total (metros de cable): {costo_total} metros")

# Calculo el camino más corto de "habitación 1" a "sala de estar"
inicio = "habitación 1"
destino = "sala de estar"
camino, distancia_total = dijkstra(grafo, inicio, destino)
print(f"Camino más corto de {inicio} a {destino}: {' -> '.join(camino)}")
print(f"Distancia total (metros de cable): {distancia_total} metros")

#ejercicio 15
class GrafoMaravillas:
    def __init__(self):
        self.vertices = {}
        self.aristas = []
    
    def agregar_maravilla(self, nombre, pais, tipo):
        if nombre not in self.vertices:
            self.vertices[nombre] = {'pais': pais, 'tipo': tipo, 'conexiones': []}
    
    def agregar_arista(self, origen, destino, distancia):
        if origen in self.vertices and destino in self.vertices:
            self.vertices[origen]['conexiones'].append((destino, distancia))
            self.vertices[destino]['conexiones'].append((origen, distancia))
            self.aristas.append((distancia, origen, destino))  # Guardo como (distancia, origen, destino)

    def mostrar_grafo(self):
        for maravilla, info in self.vertices.items():
            print(f"{maravilla} ({info['tipo']} en {info['pais']}) -> {info['conexiones']}")

def kruskal_por_tipo(grafo, tipo):
    union_find = UnionFind(len(grafo.vertices))
    arbol_expansion_minima = []
    costo_total = 0
    
    aristas_tipo = [arista for arista in grafo.aristas if grafo.vertices[arista[1]]['tipo'] == tipo and grafo.vertices[arista[2]]['tipo'] == tipo]
    
    mapeo_vertices = {vertice: idx for idx, vertice in enumerate(grafo.vertices)}
    
    aristas_tipo.sort()
    
    for distancia, origen, destino in aristas_tipo:
        u = mapeo_vertices[origen]
        v = mapeo_vertices[destino]
        
        if union_find.encontrar(u) != union_find.encontrar(v):
            union_find.union(u, v)
            arbol_expansion_minima.append((origen, destino, distancia))
            costo_total += distancia
    
    return arbol_expansion_minima, costo_total

def pais_con_ambos_tipos(grafo):
    paises_tipos = {}
    for maravilla, info in grafo.vertices.items():
        pais = info['pais']
        tipo = info['tipo']
        if pais not in paises_tipos:
            paises_tipos[pais] = set()
        paises_tipos[pais].add(tipo)
    
    paises_ambos_tipos = [pais for pais, tipos in paises_tipos.items() if len(tipos) > 1]
    return paises_ambos_tipos

def pais_multiples_maravillas(grafo):
    paises_maravillas = {}
    for maravilla, info in grafo.vertices.items():
        pais = info['pais']
        tipo = info['tipo']
        if pais not in paises_maravillas:
            paises_maravillas[pais] = {}
        if tipo not in paises_maravillas[pais]:
            paises_maravillas[pais][tipo] = 0
        paises_maravillas[pais][tipo] += 1
    
    paises_multimaravillas = {pais: tipos for pais, tipos in paises_maravillas.items() if any(cantidad > 1 for cantidad in tipos.values())}
    return paises_multimaravillas

grafo = GrafoMaravillas()
maravillas = [
    ("Gran Muralla China", "China", "arquitectónica"),
    ("Petra", "Jordania", "arquitectónica"),
    ("Cristo Redentor", "Brasil", "arquitectónica"),
    ("Machu Picchu", "Perú", "arquitectónica"),
    ("Chichén Itzá", "México", "arquitectónica"),
    ("Coliseo", "Italia", "arquitectónica"),
    ("Taj Mahal", "India", "arquitectónica"),
    ("Amazonía", "Brasil, Perú, Colombia", "natural"),
    ("Bahía de Ha Long", "Vietnam", "natural"),
    ("Cataratas del Iguazú", "Argentina, Brasil", "natural"),
    ("Isla Jeju", "Corea del Sur", "natural"),
    ("Parque Nacional de Komodo", "Indonesia", "natural"),
    ("Río subterráneo de Puerto Princesa", "Filipinas", "natural"),
    ("Table Mountain", "Sudáfrica", "natural"),
]

for nombre, pais, tipo in maravillas:
    grafo.agregar_maravilla(nombre, pais, tipo)

grafo.agregar_arista("Gran Muralla China", "Petra", 7000)
grafo.agregar_arista("Cristo Redentor", "Machu Picchu", 3200)
grafo.agregar_arista("Machu Picchu", "Chichén Itzá", 2600)
grafo.agregar_arista("Chichén Itzá", "Coliseo", 9600)
grafo.agregar_arista("Coliseo", "Taj Mahal", 5900)
grafo.agregar_arista("Amazonía", "Bahía de Ha Long", 17200)
grafo.agregar_arista("Cataratas del Iguazú", "Isla Jeju", 19000)
grafo.agregar_arista("Parque Nacional de Komodo", "Río subterráneo de Puerto Princesa", 2100)
grafo.agregar_arista("Table Mountain", "Amazonía", 7000)

print("Grafo de maravillas:")
grafo.mostrar_grafo()

arbol_arquitectonico, costo_arquitectonico = kruskal_por_tipo(grafo, "arquitectónica")
print("Árbol de Expansión Mínima (Arquitectónico):")
for origen, destino, distancia in arbol_arquitectonico:
    print(f"{origen} - {destino}: {distancia} km")
print(f"Costo total (arquitectónico): {costo_arquitectonico} km")

arbol_natural, costo_natural = kruskal_por_tipo(grafo, "natural")
print("Árbol de Expansión Mínima (Natural):")
for origen, destino, distancia in arbol_natural:
    print(f"{origen} - {destino}: {distancia} km")
print(f"Costo total (natural): {costo_natural} km")

paises_ambos_tipos = pais_con_ambos_tipos(grafo)
print(f"Países con maravillas de ambos tipos: {paises_ambos_tipos}")

paises_multimaravillas = pais_multiples_maravillas(grafo)
print(f"Países con múltiples maravillas del mismo tipo: {paises_multimaravillas}")
