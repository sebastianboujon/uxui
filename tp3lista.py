#Ejercicio 6
superheroes = [
    {"nombre": "Linterna Verde", "año_aparicion": 1959, "casa": "DC", "biografia": "Un héroe con un traje verde que tiene un anillo de poder."},
    {"nombre": "Wolverine", "año_aparicion": 1974, "casa": "Marvel", "biografia": "Héroe con garras retráctiles y capacidad de regeneración."},
    {"nombre": "Dr. Strange", "año_aparicion": 1963, "casa": "Marvel", "biografia": "Hechicero Supremo con habilidades mágicas."},
    {"nombre": "Capitana Marvel", "año_aparicion": 1968, "casa": "Marvel", "biografia": "Héroe con fuerza sobrehumana y habilidades de vuelo."},
    {"nombre": "Mujer Maravilla", "año_aparicion": 1941, "casa": "DC", "biografia": "Héroe con fuerza, velocidad y habilidades de combate."},
    {"nombre": "Flash", "año_aparicion": 1940, "casa": "DC", "biografia": "El hombre más rápido del mundo."},
    {"nombre": "Star-Lord", "año_aparicion": 1976, "casa": "Marvel", "biografia": "Líder de los Guardianes de la Galaxia y experto en combate espacial."}
]
# a. Eliminar el nodo que contiene la información de Linterna Verde
def eliminar_linterna_verde(superheroes):
    return [h for h in superheroes if h["nombre"] != "Linterna Verde"]

# b. Año de aparición de Wolverine
def mostrar_ano_wolverine(superheroes):
    for h in superheroes:
        if h["nombre"] == "Wolverine":
            return h["año_aparicion"]
    return None

# c. Cambiar la casa de Dr. Strange a Marvel
def cambiar_casa_dr_strange(superheroes):
    for h in superheroes:
        if h["nombre"] == "Dr. Strange":
            h["casa"] = "Marvel"
            break

# d. Nombre de aquellos superhéroes que en su biografía menciona la palabra traje o armadura
def superheroe_con_traje_o_armadura(superheroes):
    nombres = [h["nombre"] for h in superheroes if "traje" in h["biografia"].lower() or "armadura" in h["biografia"].lower()]
    return nombres

# e. Nombre y la casa de los superhéroes cuya fecha de aparición sea anterior a 1963
def superheroe_anterior_1963(superheroes):
    return [(h["nombre"], h["casa"]) for h in superheroes if h["año_aparicion"] < 1963]

# f. Casa a la que pertenece Capitana Marvel y Mujer Maravilla
def casa_capitana_y_mujer_maravilla(superheroes):
    casas = {}
    for h in superheroes:
        if h["nombre"] in ["Capitana Marvel", "Mujer Maravilla"]:
            casas[h["nombre"]] = h["casa"]
    return casas

# g. Iunformación de Flash y Star-Lord
def info_flash_y_star_lord(superheroes):
    info = {}
    for h in superheroes:
        if h["nombre"] in ["Flash", "Star-Lord"]:
            info[h["nombre"]] = h
    return info

# h. Superhéroes que comienzan con la letra B, M y S
def superheroe_iniciales(superheroes):
    iniciales = ['B', 'M', 'S']
    return [h["nombre"] for h in superheroes if h["nombre"][0] in iniciales]

# i. Cuántos superhéroes hay de cada casa de cómic
def conteo_casas(superheroes):
    conteo = {"Marvel": 0, "DC": 0}
    for h in superheroes:
        if h["casa"] in conteo:
            conteo[h["casa"]] += 1
    return conteo

superheroes = eliminar_linterna_verde(superheroes)
print(mostrar_ano_wolverine(superheroes))
cambiar_casa_dr_strange(superheroes)
print(superheroe_con_traje_o_armadura(superheroes))
print(superheroe_anterior_1963(superheroes))
print(casa_capitana_y_mujer_maravilla(superheroes))
print(info_flash_y_star_lord(superheroes))
print(superheroe_iniciales(superheroes))
print(conteo_casas(superheroes))


#ejercicio 15
entrenadores = [
    {
        "nombre": "Ash",
        "torneos_ganados": 5,
        "batallas_perdidas": 10,
        "batallas_ganadas": 30,
        "pokemons": [
            {"nombre": "Pikachu", "nivel": 35, "tipo": "Eléctrico", "subtipo": None},
            {"nombre": "Charizard", "nivel": 50, "tipo": "Fuego", "subtipo": "Volador"}
        ]
    },
    {
        "nombre": "Misty",
        "torneos_ganados": 3,
        "batallas_perdidas": 15,
        "batallas_ganadas": 20,
        "pokemons": [
            {"nombre": "Starmie", "nivel": 40, "tipo": "Agua", "subtipo": None},
            {"nombre": "Bulbasaur", "nivel": 30, "tipo": "Planta", "subtipo": "Veneno"}
        ]
    },
    {
        "nombre": "Brock",
        "torneos_ganados": 4,
        "batallas_perdidas": 8,
        "batallas_ganadas": 25,
        "pokemons": [
            {"nombre": "Onix", "nivel": 45, "tipo": "Roca", "subtipo": "Tierra"},
            {"nombre": "Vulpix", "nivel": 30, "tipo": "Fuego", "subtipo": None}
        ]
    }
]
# a. Cantidad de Pokémons de un determinado entrenador
def cantidad_pokemons(entrenadores, nombre_entrenador):
    for entrenador in entrenadores:
        if entrenador["nombre"] == nombre_entrenador:
            return len(entrenador["pokemons"])
    return 0

# b. Entrenadores que hayan ganado más de tres torneos
def entrenadores_mas_de_tres_torneos(entrenadores):
    return [entrenador["nombre"] for entrenador in entrenadores if entrenador["torneos_ganados"] > 3]

# c. El Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados
def pokemon_mayor_nivel_entrenador_max_torneos(entrenadores):
    max_torneos = max(entrenadores, key=lambda e: e["torneos_ganados"])
    max_torneos_entrenador = next(e for e in entrenadores if e["nombre"] == max_torneos["nombre"])
    return max(max_torneos_entrenador["pokemons"], key=lambda p: p["nivel"])

# d. Mostrar todos los datos de un entrenador y sus Pokémons
def datos_entrenador_y_pokemons(entrenadores, nombre_entrenador):
    for entrenador in entrenadores:
        if entrenador["nombre"] == nombre_entrenador:
            return entrenador
    return None

# e. Entrenadores cuyo porcentaje de batallas ganadas sea mayor al 79 %
def entrenadores_mayor_79_por_ciento(entrenadores):
    result = []
    for entrenador in entrenadores:
        total_batallas = entrenador["batallas_perdidas"] + entrenador["batallas_ganadas"]
        if total_batallas > 0:
            porcentaje_ganadas = (entrenador["batallas_ganadas"] / total_batallas) * 100
            if porcentaje_ganadas > 79:
                result.append(entrenador["nombre"])
    return result

# f. Entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador
def entrenadores_tipo_y_subtipo(entrenadores):
    result = []
    for entrenador in entrenadores:
        tipos = {(p["tipo"], p["subtipo"]) for p in entrenador["pokemons"]}
        if (("Fuego", None) in tipos and ("Planta", None) in tipos) or (("Agua", "Volador") in tipos):
            result.append(entrenador["nombre"])
    return result

# g. El promedio de nivel de los Pokémons de un determinado entrenador
def promedio_nivel_pokemons(entrenadores, nombre_entrenador):
    for entrenador in entrenadores:
        if entrenador["nombre"] == nombre_entrenador:
            niveles = [p["nivel"] for p in entrenador["pokemons"]]
            if niveles:
                return sum(niveles) / len(niveles)
    return 0

# h. Determinar cuántos entrenadores tienen a un determinado Pokémon
def cantidad_entrenadores_con_pokemon(entrenadores, nombre_pokemon):
    return sum(1 for entrenador in entrenadores if any(p["nombre"] == nombre_pokemon for p in entrenador["pokemons"]))

# i. Entrenadores que tienen Pokémons repetidos
def entrenadores_con_pokemons_repetidos(entrenadores):
    result = []
    for entrenador in entrenadores:
        nombres_pokemons = [p["nombre"] for p in entrenador["pokemons"]]
        if len(nombres_pokemons) != len(set(nombres_pokemons)):
            result.append(entrenador["nombre"])
    return result

# j. Entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Terrakion o Wingull
def entrenadores_con_pokemon_especifico(entrenadores, nombres_pokemons):
    result = []
    for entrenador in entrenadores:
        if any(p["nombre"] in nombres_pokemons for p in entrenador["pokemons"]):
            result.append(entrenador["nombre"])
    return result

# k. Determinar si un entrenador X tiene al Pokémon Y
def entrenador_tiene_pokemon(entrenadores, nombre_entrenador, nombre_pokemon):
    for entrenador in entrenadores:
        if entrenador["nombre"] == nombre_entrenador:
            for pokemon in entrenador["pokemons"]:
                if pokemon["nombre"] == nombre_pokemon:
                    return (entrenador, pokemon)
    return (None, None)
print(cantidad_pokemons(entrenadores, "Ash"))  # a
print(entrenadores_mas_de_tres_torneos(entrenadores))  # b
print(pokemon_mayor_nivel_entrenador_max_torneos(entrenadores))  # c
print(datos_entrenador_y_pokemons(entrenadores, "Brock"))  # d
print(entrenadores_mayor_79_por_ciento(entrenadores))  # e
print(entrenadores_tipo_y_subtipo(entrenadores))  # f
print(promedio_nivel_pokemons(entrenadores, "Ash"))  # g
print(cantidad_entrenadores_con_pokemon(entrenadores, "Charizard"))  # h
print(entrenadores_con_pokemons_repetidos(entrenadores))  # i
print(entrenadores_con_pokemon_especifico(entrenadores, ["Tyrantrum", "Terrakion", "Wingull"]))  # j
entrenador, pokemon = entrenador_tiene_pokemon(entrenadores, "Ash", "Pikachu")  # k
if entrenador and pokemon:
    print(f"Entrenador: {entrenador}")
    print(f"Pokémon: {pokemon}")
else:
    print("Entrenador o Pokémon no encontrado")
