# -*- coding: UTF-8 -*-

# Sumar
def sumar(a, b):
    # Operar
    suma = a + b

    # Retorno
    return suma


# Restar
def restar(a, b):
    # Operar
    resta = a - b

    # Retorno
    return resta


# Multiplicar
def multiplicar(a, b):
    # Operar
    multiplicacion = a * b

    # Retorno
    return multiplicacion


# Dividir
def dividir(a, b):
    # Condicional
    if b != 0:
        # Operar
        division = a / b
    else:
        # Control error
        division = "No es posible dividir por 0"

    # Retorno
    return division


# Funcion principal
def main():
    # Capturar
    print("\n----------------------------------------------------")
    print("| Digite sus Números")
    print("---------------------------------------------------\n")
    a = int(input("Primer número: "))
    b = int(input("Segundo número: "))

    # Imprimir
    print("\n----------------------------------------------------")
    print("| Resultados:")
    print("----------------------------------------------------\n")
    print("Suma: " + str(a) + " + " + str(b) + " = "+ str(sumar(a, b)))
    print("Resta: " + str(a) + " - " + str(b) + " = "+ str(restar(a, b)))
    print("Multiplicación: " + str(a) + " * " + str(b) + " = "+ str(multiplicar(a, b)))
    print("División: " + str(a) + " / " + str(b) + " = "+ str(dividir(a, b)))
    print("\n----------------------------------------------------\n")


# Ejecutar
main()