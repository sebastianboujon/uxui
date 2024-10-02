#ejercicio 11
# Lista de personajes
personajes = [
    {"nombre": "Luke Skywalker", "planeta": "Tatooine"},
    {"nombre": "Han Solo", "planeta": "Corellia"},
    {"nombre": "Leia Organa", "planeta": "Alderaan"},
    {"nombre": "Yoda", "planeta": "Dagobah"},
    {"nombre": "Jar Jar Binks", "planeta": "Naboo"},
    {"nombre": "Chewbacca", "planeta": "Kashyyyk"},
    {"nombre": "Obi-Wan Kenobi", "planeta": "Stewjon"},
    {"nombre": "Rey", "planeta": "Jakku"},
    {"nombre": "Padmé Amidala", "planeta": "Naboo"},
]

def mostrar_personajes_planetas(personas):
    # a. Mostrar los personajes del planeta Alderaan, Endor y Tatooine
    planetas_busqueda = ["Alderaan", "Endor", "Tatooine"]
    resultado = [p for p in personas if p["planeta"] in planetas_busqueda]
    return resultado

def planeta_natal(nombre, personas):
    for p in personas:
        if p["nombre"] == nombre:
            return p["planeta"]
    return None

def insertar_personaje(nuevo_personaje, antes_de, personas):
    for i, p in enumerate(personas):
        if p["nombre"] == antes_de:
            personas.insert(i, nuevo_personaje)
            return
    print(f"{antes_de} no encontrado en la lista.")

def eliminar_personaje_despues(de, personas):
    for i, p in enumerate(personas):
        if p["nombre"] == de and i + 1 < len(personas):
            del personas[i + 1]
            return
    print(f"{de} no encontrado en la lista o no hay personaje después de él.")

# Ejemplos de uso de las funciones
print("Personajes de Alderaan, Endor y Tatooine:")
for personaje in mostrar_personajes_planetas(personajes):
    print(personaje)

print("Planeta natal de Luke Skywalker:", planeta_natal("Luke Skywalker", personajes))
print("Planeta natal de Han Solo:", planeta_natal("Han Solo", personajes))

nuevo_personaje = {"nombre": "Ahsoka Tano", "planeta": "Shili"}
insertar_personaje(nuevo_personaje, "Yoda", personajes)
print("Lista después de insertar Ahsoka Tano antes de Yoda:")
print(personajes)

eliminar_personaje_despues("Jar Jar Binks", personajes)
print("Lista después de eliminar el personaje después de Jar Jar Binks:")
print(personajes)

#ejercicio 22
# Representación de los personajes en una lista
personajes_mcu = [
    {"nombre_personaje": "Tony Stark", "nombre_superheroe": "Iron Man", "genero": "M"},
    {"nombre_personaje": "Steve Rogers", "nombre_superheroe": "Capitán América", "genero": "M"},
    {"nombre_personaje": "Natasha Romanoff", "nombre_superheroe": "Black Widow", "genero": "F"},
    {"nombre_personaje": "Carol Danvers", "nombre_superheroe": "Capitana Marvel", "genero": "F"},
    {"nombre_personaje": "Scott Lang", "nombre_superheroe": "Ant-Man", "genero": "M"},
    {"nombre_personaje": "Peter Parker", "nombre_superheroe": "Spider-Man", "genero": "M"},
    {"nombre_personaje": "Wanda Maximoff", "nombre_superheroe": "Scarlet Witch", "genero": "F"},
]

# a
def nombre_personaje_captain_marvel(personajes):
    for personaje in personajes:
        if personaje["nombre_superheroe"] == "Capitana Marvel":
            return personaje["nombre_personaje"]
    return None

# b
def nombres_superheroes_femeninos(personajes):
    return [personaje["nombre_superheroe"] for personaje in personajes if personaje["genero"] == "F"]

# c
def nombres_personajes_masculinos(personajes):
    return [personaje["nombre_personaje"] for personaje in personajes if personaje["genero"] == "M"]

# d
def nombre_superheroe_scott_lang(personajes):
    for personaje in personajes:
        if personaje["nombre_personaje"] == "Scott Lang":
            return personaje["nombre_superheroe"]
    return None

# e
def datos_nombres_con_s(personajes):
    return [personaje for personaje in personajes if personaje["nombre_personaje"].startswith("S")]

# f
def verificar_carol_danvers(personajes):
    for personaje in personajes:
        if personaje["nombre_personaje"] == "Carol Danvers":
            return personaje["nombre_superheroe"]
    return None

# Uso de las funciones
print("a. Nombre del personaje de la superhéroe Capitana Marvel:", nombre_personaje_captain_marvel(personajes_mcu))
print("b. Nombres de los superhéroes femeninos:", nombres_superheroes_femeninos(personajes_mcu))
print("c. Nombres de los personajes masculinos:", nombres_personajes_masculinos(personajes_mcu))
print("d. Nombre del superhéroe de Scott Lang:", nombre_superheroe_scott_lang(personajes_mcu))
print("e. Datos de superhéroes o personajes cuyos nombres comienzan con 'S':", datos_nombres_con_s(personajes_mcu))
print("f. Nombre del superhéroe de Carol Danvers:", verificar_carol_danvers(personajes_mcu))
