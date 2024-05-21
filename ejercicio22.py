def usarLaFuerza(mochila, indice=0, objetos_sacados=0):
    if indice >= len(mochila):
        return False, objetos_sacados
    
    objeto_actual = mochila[indice]
    
    if objeto_actual == "sable de luz":
        return True, objetos_sacados
    
    objetos_sacados += 1
    
    return usarLaFuerza(mochila, indice + 1, objetos_sacados)

mochila = ["comida", "botiquín", "sable de luz", "mapa", "ropa"]
encontrado, objetos_necesarios = usarLaFuerza(mochila)

if encontrado:
    print(f"¡Se encontró un sable de luz! Se necesitaron sacar {objetos_necesarios} objetos.")
else:
    print("No se encontró un sable de luz en la mochila.")
