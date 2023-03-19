def contarPalabras(cadena):
    diccionario = {}

    palabras = cadena.split()
    for palabra in palabras:
        if palabra in diccionario:
            diccionario[palabra] += 1
        else:
            diccionario[palabra] = 1

    return diccionario

cadena = "hola profe puede repetir hola profe o no profe"

resultado = contarPalabras(cadena)

print(resultado)


def palabraRepetida (diccionario):
    palabra = ""
    frecuencia = 0

    for clave,valor in diccionario.items():
        if valor > frecuencia:

            palabra = clave
            frecuencia = valor

    return (palabra, frecuencia)

palabra_repetida, frecuencia = palabraRepetida(resultado)
print(palabra_repetida, frecuencia)