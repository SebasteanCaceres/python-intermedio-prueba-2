
from functools import reduce

def calculadora():
    lista = []
    for cal in range (5):
        valor = int(input("Ingrese un entero: "))
        lista.append(valor)
    print(lista)

    suma = reduce(lambda a, b: a + b, lista)
    print("Suma: " , suma)
    
    resta = reduce(lambda a, b: a - b, lista)
    print("Resta: ", resta)

    producto = reduce(lambda a, b: a * b, lista)
    print("Multiplicación: ", producto)

    division = reduce(lambda a, b: a / b, lista)
    print("División: ", division)

    exponente = reduce(lambda a, b: a ** b, lista)
    print("Exponente: ", exponente)

    raiz_cuadrada = reduce(lambda a, b: a ** (1/b), lista)
    print("Raiz cuadrada: ", raiz_cuadrada)





if __name__ == "__main__":
    calculadora()