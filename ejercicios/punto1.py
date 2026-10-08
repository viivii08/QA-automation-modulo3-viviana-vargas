
def es_primo(numero):
    if numero < 2:
        return False

    divisor = 2
    while divisor * divisor <= numero:
        if numero % divisor == 0:
            return False
        divisor += 1

    return True


try:
    numero = int(input("Ingrese un numero entero: "))

    if es_primo(numero):
        print(f"El numero {numero} es primo")
    else:
        print(f"El numero {numero} no es primo")

except ValueError:
    print("Error: tiene que ingresar un numero entero")