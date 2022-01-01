# -*- coding: UTF-8 -*-

# Importar
import operaciones_aritmeticas as operaciones

# Menu
def menu_opciones():
    # Imprimir menú
    print("\n---------------------------------------------------")
    print("Calculadora Amigable V.2 - Menú Principal")
    print("---------------------------------------------------")
    print("| 1. Sumar")
    print("| 2. Restar")
    print("| 3. Multiplicar")
    print("| 4. Dividir")
    print("| 5. Salir")
    print("---------------------------------------------------")
    opcion = input("Seleccione una operación: ")
    print("---------------------------------------------------\n")

    # Retorno
    return opcion


# Capturar números
def capturar_numeros():
    # Menú
    print("\n---------------------------------------------------")
    print("Digite sus números")
    print("---------------------------------------------------")
    
    # Control
    try:
        # Capturar números
        a = float(input("Digite su primer número: "))
        b = float(input("Digite su segundo número: "))
        print("---------------------------------------------------\n")

        # Retorno
        return [a, b]
    except:
        # Imprimir
        print("---------------------------------------------------\n")
        print("Datos incorrectos, intenté nuevamente")

        # Loop
        capturar_numeros()


# Función principal
def main():
    while(True):
        # Capturar menú
        opcion = menu_opciones()

        # Condicional
        if opcion == '1':
            # Capturar numeros
            a, b = capturar_numeros()

            # Operar
            print("El resultado de la suma es: " + str(operaciones.sumar(a, b)))
        elif opcion == '2':
            # Capturar numeros
            a, b = capturar_numeros()

            # Operar
            print("El resultado de la resta es: " + str(operaciones.restar(a, b)))
        elif opcion == '3':
            # Capturar numeros
            a, b = capturar_numeros()

            # Operar
            print("El resultado de la multiplicación es: " + str(operaciones.multiplicar(a, b)))
        elif opcion == '4':
            # Capturar numeros
            a, b = capturar_numeros()

            # Operar
            print("El resultado de la división es: " + str(operaciones.dividir(a, b)))
        elif opcion == '5':
            # Finalizar
            exit()
        else:
            # Operar
            print("Operación incorrecta, intente nuevamente")
        

# Linea ejecucion    
main()