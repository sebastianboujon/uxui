pila_episodio_v = ["Luke Skywalker", "Darth Vader", "Princess Leia", "Han Solo", "Chewbacca", "Yoda"]
pila_episodio_vii = ["Rey", "Finn", "Kylo Ren", "Poe Dameron", "BB-8", "Luke Skywalker"]

interseccion = list(set(pila_episodio_v) & set(pila_episodio_vii))

print("Personajes que aparecen en los dos episodios:")
for personaje in interseccion:
    print(personaje)