def get_int():
    while True:
        try:
            valor = int(input("Ingrese un valor "))
            return valor
        except ValueError:
            print("El valor ingresado no es valido")

#recursiva#

def get_int():
    try:
        valor = int(input("Ingrese un valor"))
        return valor
    except ValueError:
        print("El valor ingresado no es válido")