import os

# --- ZONA DE FUNCIONES ---

# Estudiante 2: Fibonacci
def fibonacci(n):
    fib_sequence = [0, 1]
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

# Estudiante 3: Factorial
def factorial(n):
    if n < 0:
        return "No existe factorial de negativos"
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        return fact

# Estudiante 4: Número Primo (¡NUEVO!)
def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

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
            try:
                n = int(input("¿Cuántos números de Fibonacci desea?: "))
                print(f"Serie: {fibonacci(n)}")
            except ValueError:
                print("Error: Ingrese un número válido.")

        elif opcion == '2':
            try:
                n = int(input("Ingrese un número para calcular el factorial: "))
                print(f"El factorial es: {factorial(n)}")
            except ValueError:
                print("Error: Ingrese un número entero.")

        elif opcion == '3':
            # LOGICA DE NUMEROS PRIMOS
            try:
                n = int(input("Ingrese un número para verificar si es primo: "))
                if es_primo(n):
                    print(f"El número {n} ES Primo.")
                else:
                    print(f"El número {n} NO es Primo.")
            except ValueError:
                print("Error: Ingrese un número entero.")

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