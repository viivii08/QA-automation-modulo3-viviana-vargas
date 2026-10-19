import math


def calcular_raices(a, b, c):
    if a == 0:
        return None

    discriminante = b ** 2 - 4 * a * c

    if discriminante > 0:
        x1 = (-b + math.sqrt(discriminante)) / (2 * a)
        x2 = (-b - math.sqrt(discriminante)) / (2 * a)
        return [x1, x2]

    elif discriminante == 0:
        x = -b / (2 * a)
        return [x]

    else:
        return []


print("Bienvenido/a a la calculadora de ecuaciones cuadraticas")
print("Ingresa los valores de a, b y c, o escribi 'terminar' en a para salir.")

while True:
    texto_a = input("Ingrese el valor de a: ").strip()

    if texto_a.lower() == "terminar":
        print("Gracias, que tengas un buen dia")
        break

    try:
        a = float(texto_a)
        b = float(input("Ingrese el valor de b: "))
        c = float(input("Ingrese el valor de c: "))

        raices = calcular_raices(a, b, c)

        if raices is None:
            print("Error: si a es 0 no es una ecuacion cuadratica")
        elif len(raices) == 2:
            print(f"Hay 2 soluciones: x1 = {raices[0]} y x2 = {raices[1]}")
        elif len(raices) == 1:
            print(f"Hay 1 solucion: x = {raices[0]}")
        else:
            print("No hay solucion (el discriminante es negativo)")

    except ValueError:
        print("Error: tiene que ingresar numeros")