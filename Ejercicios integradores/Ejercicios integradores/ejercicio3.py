def contarPalabras(cadena):
    diccionario = {}

    palabras = cadena.split()
    for palabra in palabras:
        if palabra in diccionario:
            diccionario[palabra] += 1
        else:
            diccionario[palabra] = 1

    return diccionario

cadena = "hola profe puede repetir hola profe"

resultado = contarPalabras(cadena)

print(resultado)
