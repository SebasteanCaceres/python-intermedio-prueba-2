
def es_primo(num):
    for n in range(2, num):
        if num % n == 0:
            print("No es primo", n, "es divisor")
            return False
    print("Es primo")
    return True

def lista_primos():
    primos = []
    for dividendo in range(2, 1001):     
        for divisor in range(2, dividendo):
                if dividendo % divisor == 0:
                        break
        else:
                primos.append(dividendo)
    print(primos)

if __name__ == "__main__":
    es_primo(799)
    lista_primos()
