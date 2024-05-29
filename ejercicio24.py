# personajes de Marvel Cinematic Universe (MCU)
pila_personajes_mcu = [
    ("Iron Man", 9),
    ("Captain America", 7),
    ("Thor", 7),
    ("Hulk", 6),
    ("Black Widow", 8),
    ("Hawkeye", 5),
    ("Spider-Man", 5),
    ("Black Panther", 4),
    ("Doctor Strange", 4),
    ("Scarlet Witch", 4),
    ("Vision", 4),
    ("Ant-Man", 3),
    ("Wasp", 2),
    ("Captain Marvel", 2),
    ("Falcon", 5),
    ("Winter Soldier", 4),
    ("War Machine", 6),
    ("Rocket Raccoon", 5),
    ("Groot", 5)
]

def posicion_rocket_groot(pila):
    posicion_rocket = None
    posicion_groot = None
    for i, (personaje, _) in enumerate(pila, 1):
        if personaje == "Rocket Raccoon":
            posicion_rocket = i
        elif personaje == "Groot":
            posicion_groot = i
    return posicion_rocket, posicion_groot

def personajes_mas_de_5_pelis(pila):
    return [(personaje, pelis) for personaje, pelis in pila if pelis > 5]

def peliculas_viuda_negra(pila):
    for personaje, pelis in pila:
        if personaje == "Black Widow":
            return pelis
    return 0

def personajes_con_iniciales(pila, iniciales):
    return [personaje for personaje, _ in pila if personaje[0] in iniciales]

# a)
posicion_rocket, posicion_groot = posicion_rocket_groot(pila_personajes_mcu)
print(" Posición de Rocket Raccoon:", posicion_rocket)
print(" Posición de Groot:", posicion_groot)

# b)
personajes_mas_5_pelis = personajes_mas_de_5_pelis(pila_personajes_mcu)
print("Personajes que participaron en más de 5 películas:")
for personaje, pelis in personajes_mas_5_pelis:
    print(f"   {personaje}: {pelis} películas")

# c)
pelis_viuda_negra = peliculas_viuda_negra(pila_personajes_mcu)
print("Películas en las que participó Black Widow:", pelis_viuda_negra)

# d)
print("Personajes cuyos nombres empiezan con C, D y G:")
iniciales = ['C', 'D', 'G']
personajes_con_iniciales = personajes_con_iniciales(pila_personajes_mcu, iniciales)
for personaje in personajes_con_iniciales:
    print("   ", personaje)
