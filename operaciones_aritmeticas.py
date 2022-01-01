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