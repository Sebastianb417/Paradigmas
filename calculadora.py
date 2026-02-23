# Funcion que muestra el menu
def menu():
    print("CALCULADORA")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

# Funcion principal
def calculadora():
    
    # Este while hace que el programa se repita hasta que el usuario salga
    while True:
        menu()  # mostramos el menu
        
        # Le pedimos al usuario una opcion
        option = input("Introduce el numero de la operacion deseada: ")
        
        if option == '1':
            # Pedimos los numeros para sumar
            a = float(input("Ingrese el primer numero: "))
            b = float(input("Ingrese el segundo numero: "))
            print("Resultado:", a + b)
        
        elif option == '2':
            # Pedimos los numeros para restar
            a = float(input("Ingrese el primer numero: "))
            b = float(input("Ingrese el segundo numero: "))
            print("Resultado:", a - b)
        
        elif option == '3':
            # Pedimos los numeros para multiplicar
            a = float(input("Ingrese el primer numero: "))
            b = float(input("Ingrese el segundo numero: "))
            print("Resultado:", a * b)
        
        elif option == '4':
            # Pedimos los numeros para dividir
            a = float(input("Ingrese el primer numero: "))
            b = float(input("Ingrese el segundo numero: "))
            
            # Validamos que no sea division por cero
            if b != 0:
                print("Resultado:", a / b)
            else:
                print("No se puede dividir por cero")
        
        elif option == '5':
            # Si elige 5 se cierra el programa
            print("Saliendo...")
            break
        
        else:
            # Por si escribe algo diferente
            print("Opcion no valida")

# Iniciamos el programa
calculadora()
