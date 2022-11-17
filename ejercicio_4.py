
def bloque_1():
    try:
        mi_lista = ["Python","C","C++","JavaScript"]
        print()
        print(mi_lista[5])
    except IndexError as e:
        print("Exece el largo total de la lista")

def bloque_2(num):
    try:
        resultado = num + 10
    except Exception as e:
        print("Ocurrio un error: ")
        print(e)
        resultado < 0

    print(resultado)

def bloque_3():
    try: 
        capitales  = {
        "Colombia": "Bogotá",
        "Argentina": "Buenos Aires",
        "Perú": "Lima",
        "Chile": "Santiago de Chile",
    }
        print(capitales["Brasil"])
    except KeyError:
        print("El elemento a buscar no existe.")


        

def main():
    # Esta función no debe ser modificada. Modifique las funciones bloque_1, bloque_2, bloque_3 y bloque_4.
    # Si modifica esta sección para hacer pruebas recuerde cambiarla antes de enviar el ejercicio.
    print("Bloque 1")
    bloque_1()
    print("-------------")

    print("Bloque 2")
    bloque_2("dos")
    print("-------------")

    print("Bloque 3")
    bloque_3()
    print("-------------")

if __name__ == '__main__':
    main()