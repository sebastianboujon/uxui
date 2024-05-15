def rumanoaDecimal(numeroRomano):
    numerosRomanos = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    if len(numeroRomano) == 0:
        return 0
    elif len(numeroRomano) == 1:
        return numerosRomanos[numeroRomano]

    if numerosRomanos[numeroRomano[0]] < numerosRomanos[numeroRomano[1]]:
        return numerosRomanos[numeroRomano[1]] - numerosRomanos[numeroRomano[0]] + rumanoaDecimal(numeroRomano[2:])
    else:
        return numerosRomanos[numeroRomano[0]] + rumanoaDecimal(numeroRomano[1:])


print(rumanoaDecimal("IV"))  
print(rumanoaDecimal("IX"))  
print(rumanoaDecimal("LVIII"))  
print(rumanoaDecimal("MCMXCIV"))  
