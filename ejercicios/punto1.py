def es_primo(numero):
    if numero < 2:
        return False

    divisor = 2
    while divisor * divisor <= numero:
        if numero % divisor == 0:
            return False
        divisor += 1

    return True


print("Bienvenido/a al verificador de numeros primos")
print("Escribi un numero para saber si es primo, o 'terminar' para salir.")

while True:
    texto = input("Ingrese un numero entero (o 'terminar' para salir): ").strip()

    if texto.lower() == "terminar":
        print("Gracias, que tengas un buen dia")
        break

    try:
        numero = int(texto)

        if es_primo(numero):
            print(f"El numero {numero} es primo")
        else:
            print(f"El numero {numero} no es primo")

    except ValueError:
        print("Error: tiene que ingresar un numero entero")