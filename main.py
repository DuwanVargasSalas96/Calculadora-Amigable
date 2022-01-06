# -*- coding: UTF-8 -*-

# Importar
import operaciones_aritmeticas as operaciones

# Capturar operacion
def capturar_operacion():
    # Menú
    print("\n---------------------------------------------------")
    print("Calculadora Amigable V.3")
    print("---------------------------------------------------")
    operacion = input("Ingrese su operación (Ej: 2 + 2, 2*2): ")
    
    # Operacion
    return operacion


# Función principal
def main():
    while(True):
        # Capturar operacion
        operacion = capturar_operacion()

        # Condicional
        if "+" in operacion:
            # Capturar números
            a, b = operacion.split("+")

            # Control de errores
            try:
                # Convertir
                a = float(a)
                b = float(b)

                # Imprimir
                print("---------------------------------------------------\n")
                print(operacion + " = " + str(operaciones.sumar(a, b)))
                print("\n---------------------------------------------------\n")
                print("Para salir escriba salir o SALIR")
            except:
                # Imprimir
                print("---------------------------------------------------\n")
                print("Operación incorrecta, intenté nuevamente")
                print("\n---------------------------------------------------\n")
                print("Para salir escriba salir o SALIR")

                # Retorno
                main()
        elif "-" in operacion:
            # Capturar números
            a, b = operacion.split("-")

            # Control de errores
            try:
                # Convertir
                a = float(a)
                b = float(b)

                # Imprimir
                print("---------------------------------------------------\n")
                print(operacion + " = " + str(operaciones.restar(a, b)))
                print("\n---------------------------------------------------\n")
                print("Para salir escriba salir o SALIR")
            except:
                # Imprimir
                print("---------------------------------------------------\n")
                print("Operación incorrecta, intenté nuevamente")
                print("\n---------------------------------------------------\n")
                print("Para salir escriba salir o SALIR")

                # Retorno
                main()
        elif "*" in operacion:
            # Capturar números
            a, b = operacion.split("*")

            # Control de errores
            try:
                # Convertir
                a = float(a)
                b = float(b)

                # Imprimir
                print("---------------------------------------------------\n")
                print(operacion + " = " + str(operaciones.multiplicar(a, b)))
                print("\n---------------------------------------------------\n")
                print("Para salir escriba salir o SALIR")
            except:
                # Imprimir
                print("---------------------------------------------------\n")
                print("Operación incorrecta, intenté nuevamente")
                print("\n---------------------------------------------------\n")
                print("Para salir escriba salir o SALIR")

                # Retorno
                main()
        elif "/" in operacion:
            # Capturar números
            a, b = operacion.split("/")

            # Control de errores
            try:
                # Convertir
                a = float(a)
                b = float(b)

                # Imprimir
                print("---------------------------------------------------\n")
                print(operacion + " = " + str(operaciones.dividir(a, b)))
                print("\n---------------------------------------------------\n")
                print("Para salir escriba salir o SALIR")
            except:
                # Imprimir
                print("---------------------------------------------------\n")
                print("Operación incorrecta, intenté nuevamente")
                print("\n---------------------------------------------------\n")
                print("Para salir escriba salir o SALIR")

                # Retorno
                main()
        elif operacion == 'SALIR' or operacion == 'salir':
            # Salir
            exit()
        else:
            # Imprimir
            print("---------------------------------------------------\n")
            print("Operación incorrecta, intenté nuevamente")


# Linea ejecucion
main()