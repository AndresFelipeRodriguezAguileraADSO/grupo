import os

def menu():
    while True:
        print("\n--- MENÚ PRINCIPAL V1 ---")
        print("1. Serie de Fibonacci (Estudiante 2)")
        print("2. Calcular Factorial (Estudiante 3)")
        print("3. Verificar si es Primo (Estudiante 4)")
        print("4. Generar N Números Perfectos (Estudiante 5)")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            print("Funcionalidad Fibonacci en construcción...")
            # Aquí el Estudiante 2 pondrá su código
            pass 
        elif opcion == '2':
            print("Funcionalidad Factorial en construcción...")
            # Aquí el Estudiante 3 pondrá su código
            pass
        elif opcion == '3':
            print("Funcionalidad Primos en construcción...")
            # Aquí el Estudiante 4 pondrá su código
            pass
        elif opcion == '4':
            print("Funcionalidad Perfectos en construcción...")
            # Aquí el Estudiante 5 pondrá su código
            pass
        elif opcion == '5':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()