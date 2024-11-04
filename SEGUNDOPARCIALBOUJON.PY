class Pokemon:
    def __init__(self, numero, nombre, tipos):
        self.numero = numero
        self.nombre = nombre
        self.tipos = tipos

    def __repr__(self):
        return f"{self.numero} - {self.nombre} - Tipos: {', '.join(self.tipos)}"

class NodoArbol:
    def __init__(self, pokemon):
        self.pokemon = pokemon
        self.izquierda = None
        self.derecha = None

class ArbolBinarioBusqueda:
    def __init__(self, clave):
        # (nombre, número o tipo)
        self.raiz = None
        self.clave = clave

    def insertar(self, pokemon):
        if not self.raiz:
            self.raiz = NodoArbol(pokemon)
        else:
            self._insertar_recursivo(self.raiz, pokemon)

    def _insertar_recursivo(self, nodo, pokemon):
        # comparo de acuerdo al índice
        if getattr(pokemon, self.clave) < getattr(nodo.pokemon, self.clave):
            if nodo.izquierda is None:
                nodo.izquierda = NodoArbol(pokemon)
            else:
                self._insertar_recursivo(nodo.izquierda, pokemon)
        else:
            if nodo.derecha is None:
                nodo.derecha = NodoArbol(pokemon)
            else:
                self._insertar_recursivo(nodo.derecha, pokemon)

    def buscar(self, valor, coincidencia_parcial=False):
        return self._buscar_recursivo(self.raiz, valor, coincidencia_parcial)

    def _buscar_recursivo(self, nodo, valor, coincidencia_parcial):
        if nodo is None:
            return None
        atributo = getattr(nodo.pokemon, self.clave)
       
        if coincidencia_parcial and self.clave == "nombre" and valor.lower() in atributo.lower():
            return nodo.pokemon
        # si encontramos el valor exacto
        if atributo == valor:
            return nodo.pokemon
        
        # continuo la busqueda en el subarbol adecuado
        if valor < atributo:
            return self._buscar_recursivo(nodo.izquierda, valor, coincidencia_parcial)
        else:
            return self._buscar_recursivo(nodo.derecha, valor, coincidencia_parcial)

    def recorrido_inorden(self):
        # retorna lista en orden ascendente
        return self._recorrido_inorden_recursivo(self.raiz, [])

    def _recorrido_inorden_recursivo(self, nodo, lista):
        if nodo:
            self._recorrido_inorden_recursivo(nodo.izquierda, lista)
            lista.append(nodo.pokemon)
            self._recorrido_inorden_recursivo(nodo.derecha, lista)
        return lista

arbol_por_nombre = ArbolBinarioBusqueda("nombre")
arbol_por_numero = ArbolBinarioBusqueda("numero")
arbol_por_tipo = ArbolBinarioBusqueda("tipos")  # asumo que el primer tipo es el principal

def agregar_pokemon_a_arboles(pokemon):
    arbol_por_nombre.insertar(pokemon)
    arbol_por_numero.insertar(pokemon)
    for tipo in pokemon.tipos:
        arbol_por_tipo.insertar(Pokemon(pokemon.numero, pokemon.nombre, [tipo]))

def buscar_por_proximidad(subcadena):
    resultados = []
    for pokemon in arbol_por_nombre.recorrido_inorden():
        if subcadena.lower() in pokemon.nombre.lower():
            resultados.append(pokemon)
    return resultados

def mostrar_por_tipo(tipo):
    resultados = []
    for pokemon in arbol_por_tipo.recorrido_inorden():
        if tipo in pokemon.tipos:
            resultados.append(pokemon.nombre)
    return resultados

def listado_por_numero():
    return arbol_por_numero.recorrido_inorden()


def listado_por_nombre():
    return arbol_por_nombre.recorrido_inorden()

def mostrar_pokemons_especificos(nombres):
    resultados = []
    for nombre in nombres:
        pokemon = arbol_por_nombre.buscar(nombre)
        if pokemon:
            resultados.append(pokemon)
    return resultados

def contar_pokemons_por_tipo(tipo):
    return len(mostrar_por_tipo(tipo))
# Creo algunos Pokemon de ejemplo
pikachu = Pokemon(25, "Pikachu", ["eléctrico"])
bulbasaur = Pokemon(1, "Bulbasaur", ["planta", "veneno"])
charmander = Pokemon(4, "Charmander", ["fuego"])
squirtle = Pokemon(7, "Squirtle", ["agua"])
jolteon = Pokemon(135, "Jolteon", ["eléctrico"])

# Agrego Pokemon a los árboles
agregar_pokemon_a_arboles(pikachu)
agregar_pokemon_a_arboles(bulbasaur)
agregar_pokemon_a_arboles(charmander)
agregar_pokemon_a_arboles(squirtle)
agregar_pokemon_a_arboles(jolteon)

# Ejemplo de uso
print(buscar_por_proximidad("bul"))  # b) busco por proximidad
print(mostrar_por_tipo("agua"))       # c) muestro Pokemon de tipo agua
print(listado_por_numero())           # d) listo por número
print(listado_por_nombre())           # d) listo por nombre
print(mostrar_pokemons_especificos(["Jolteon", "Lycanroc", "Tyrantrum"]))  # e) mouestro datos de un Pokemon específicos
print(contar_pokemons_por_tipo("eléctrico"))  # f) cuento Pokemon de tipo eléctrico





class Vertice:
    def __init__(self, nombre):
        self.nombre = nombre
        self.adyacentes = {}  # diccionario de personajes con el número de episodios compartidos

    def agregar_adyacente(self, vertice, episodios):
        self.adyacentes[vertice] = episodios

class Grafo:
    def __init__(self):
        self.vertices = {}

    def agregar_vertice(self, nombre):
        if nombre not in self.vertices:
            self.vertices[nombre] = Vertice(nombre)

    def agregar_arista(self, origen, destino, episodios):
        if origen in self.vertices and destino in self.vertices:
            self.vertices[origen].agregar_adyacente(self.vertices[destino], episodios)
            self.vertices[destino].agregar_adyacente(self.vertices[origen], episodios)

class Arista:
    def __init__(self, origen, destino, peso):
        self.origen = origen
        self.destino = destino
        self.peso = peso

    def __lt__(self, other):
        return self.peso < other.peso

class UnionFind:
    def __init__(self, n):
        self.padre = list(range(n))
        self.rango = [0] * n

    def find(self, u):
        if u != self.padre[u]:
            self.padre[u] = self.find(self.padre[u])
        return self.padre[u]

    def union(self, u, v):
        ru = self.find(u)
        rv = self.find(v)
        if ru != rv:
            if self.rango[ru] > self.rango[rv]:
                self.padre[rv] = ru
            elif self.rango[ru] < self.rango[rv]:
                self.padre[ru] = rv
            else:
                self.padre[rv] = ru
                self.rango[ru] += 1

def arbol_expansion_minima(grafo):
    aristas = []
    # obtengo todas las aristas del grafo
    for vertice in grafo.vertices.values():
        for adyacente, peso in vertice.adyacentes.items():
            aristas.append(Arista(vertice, adyacente, peso))

    # ordeno las aristas por peso
    aristas.sort()
    union_find = UnionFind(len(grafo.vertices))

    mst = []
    total_peso = 0
    for arista in aristas:
        origen = list(grafo.vertices.keys()).index(arista.origen.nombre)
        destino = list(grafo.vertices.keys()).index(arista.destino.nombre)
        if union_find.find(origen) != union_find.find(destino):
            union_find.union(origen, destino)
            mst.append(arista)
            total_peso += arista.peso

    # verifico si Yoda está en el árbol de expansión mínima
    contiene_yoda = any(arista.origen.nombre == "Yoda" or arista.destino.nombre == "Yoda" for arista in mst)

    return mst, contiene_yoda
def maximo_episodios_compartidos(grafo):
    max_episodios = 0
    personajes = (None, None)
    for vertice in grafo.vertices.values():
        for adyacente, episodios in vertice.adyacentes.items():
            if episodios > max_episodios:
                max_episodios = episodios
                personajes = (vertice.nombre, adyacente.nombre)
    return max_episodios, personajes
# creo el grafo y añado personajes y relaciones
grafo_star_wars = Grafo()

# Listo personajes a agregar
personajes = [
    "Luke Skywalker", "Darth Vader", "Yoda", "Boba Fett", "C-3PO",
    "Leia", "Rey", "Kylo Ren", "Chewbacca", "Han Solo", "R2-D2", "BB-8"
]

# Agrego los personajes al grafo
for personaje in personajes:
    grafo_star_wars.agregar_vertice(personaje)

for arista in mst:
    print(f"{arista.origen.nombre} - {arista.destino.nombre} con peso {arista.peso}")
print(f"El árbol de expansión mínima contiene a Yoda: {'Sí' if contiene_yoda else 'No'}")

# b) Obtengo el árbol de expansión mínima y verificar si contiene a Yoda
mst, contiene_yoda = arbol_expansion_minima(grafo_star_wars)
print("Árbol de Expansión Mínima:")

# c) Determino el número máximo de episodios compartidos entre dos personajes
max_episodios, personajes = maximo_episodios_compartidos(grafo_star_wars)
print(f"Máximo número de episodios compartidos: {max_episodios} entre {personajes[0]} y {personajes[1]}")

# Agrego conexiones (aristas) entre personajes con el número de episodios compartidos
# Estos son ejemplos de episodios compartidos entre algunos personajes
grafo_star_wars.agregar_arista("Luke Skywalker", "Darth Vader", 4)
grafo_star_wars.agregar_arista("Luke Skywalker", "Leia", 3)
grafo_star_wars.agregar_arista("Luke Skywalker", "Yoda", 2)
grafo_star_wars.agregar_arista("Leia", "Han Solo", 4)
grafo_star_wars.agregar_arista("Leia", "Chewbacca", 3)
grafo_star_wars.agregar_arista("Leia", "C-3PO", 5)
grafo_star_wars.agregar_arista("Han Solo", "Chewbacca", 5)
grafo_star_wars.agregar_arista("Darth Vader", "Yoda", 1)
grafo_star_wars.agregar_arista("Rey", "Kylo Ren", 3)
grafo_star_wars.agregar_arista("R2-D2", "C-3PO", 6)
grafo_star_wars.agregar_arista("BB-8", "Rey", 2)
grafo_star_wars.agregar_arista("Chewbacca", "R2-D2", 2)
