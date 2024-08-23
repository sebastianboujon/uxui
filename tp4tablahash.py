class Pokemon:
    def __init__(self, numero, nombre, tipos, nivel):
        self.numero = numero
        self.nombre = nombre
        self.tipos = tipos  
        self.nivel = nivel

    def __str__(self):
        return f'#{self.numero}: {self.nombre} - Tipos: {", ".join(self.tipos)} - Nivel: {self.nivel}'


class TableHash:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def insert(self, key, pokemon):
        self.table[key].append(pokemon)

    def get(self, key):
        return self.table[key]

    def hash_tipo(self, tipo):
        return ord(tipo[0]) % self.size


table_hash_tipo = TableHash(50)  
table_hash_numero = TableHash(10)
table_hash_nivel = TableHash(10)  

def insertarPokemon(pokemon):
    for tipo in pokemon.tipos:
        index_tipo = table_hash_tipo.hash_tipo(tipo)
        table_hash_tipo.insert(index_tipo, pokemon)

    ultimo_digito = pokemon.numero % 10
    table_hash_numero.insert(ultimo_digito, pokemon)

    index_nivel = pokemon.nivel % 10
    table_hash_nivel.insert(index_nivel, pokemon)

def mostrarPokemonsTerminadosEn(terminaciones):
    print("Pokémons cuyos números terminan en", terminaciones)
    for termino in terminaciones:
        lista_pokemons = table_hash_numero.get(termino)
        for pokemon in lista_pokemons:
            print(pokemon)

def mostrarPokemonsMultiploNivel(multiplo):
    print(f"\nPokémons cuyos niveles son múltiplos de {multiplo}:")
    for i in range(table_hash_nivel.size):
        lista_pokemons = table_hash_nivel.get(i)
        for pokemon in lista_pokemons:
            if pokemon.nivel % multiplo == 0:
                print(pokemon)

def mostrarPokemonsPorTipo(tipos_a_mostrar):
    print("\nPokémons de los tipos:", tipos_a_mostrar)
    for tipo in tipos_a_mostrar:
        index_tipo = table_hash_tipo.hash_tipo(tipo)
        lista_pokemons = table_hash_tipo.get(index_tipo)
        for pokemon in lista_pokemons:
            print(pokemon)

insertarPokemon(Pokemon(1, "Bulbasaur", ["Planta", "Veneno"], 16))
insertarPokemon(Pokemon(2, "Ivysaur", ["Planta", "Veneno"], 32))
insertarPokemon(Pokemon(3, "Venusaur", ["Planta", "Veneno"], 50))
insertarPokemon(Pokemon(4, "Charmander", ["Fuego"], 35))
insertarPokemon(Pokemon(25, "Pikachu", ["Eléctrico"], 25))
insertarPokemon(Pokemon(78, "Rapidash", ["Fuego", "Normal"], 40))
insertarPokemon(Pokemon(90, "Articuno", ["Hielo", "Volador"], 70))
insertarPokemon(Pokemon(38, "Ninetales", ["Fuego"], 50))

# Mostrar Pokémon
mostrarPokemonsTerminadosEn([3, 7, 9])
mostrarPokemonsMultiploNivel(2)
mostrarPokemonsMultiploNivel(5)
mostrarPokemonsMultiploNivel(10)
mostrarPokemonsPorTipo(["Acero", "Fuego", "Electrifico", "Hielo"])
