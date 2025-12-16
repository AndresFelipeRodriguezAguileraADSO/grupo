import os

# --- ZONA DE FUNCIONES ---

# Estudiante 2: Fibonacci (¡YA IMPLEMENTADO!)
def fibonacci(n):
    fib_sequence = [0, 1]
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

# --- ZONA DEL MENÚ ---

def menu():
    while True:
        print("\n--- MENÚ PRINCIPAL (V1.0) ---")
        print("1. Serie de Fibonacci (Estudiante 2)")
        print("2. Calcular Factorial (Estudiante 3)")
        print("3. Verificar si es Primo (Estudiante 4)")
        print("4. Generar N Números Perfectos (Estudiante 5)")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            # LOGICA DE FIBONACCI
            try:
                n = int(input("¿Cuántos números de Fibonacci desea?: "))
                print(f"Serie: {fibonacci(n)}")
            except ValueError:
                print("Error: Ingrese un número válido.")

        elif opcion == '2':
            # Espacio reservado para Estudiante 3
            print("Funcionalidad Factorial en construcción...")
            pass

        elif opcion == '3':
            # Espacio reservado para Estudiante 4
            print("Funcionalidad Primos en construcción...")
            pass

        elif opcion == '4':
            # Espacio reservado para Estudiante 5
            print("Funcionalidad Perfectos en construcción...")
            pass

        elif opcion == '5':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()