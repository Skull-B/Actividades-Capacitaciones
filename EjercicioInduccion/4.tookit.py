# 1. Factorial
def factorial(n):
    if n < 0:
        raise ValueError("El número debe ser no negativo.")
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado


# 2. Es primo
def es_primo(n):
    if n < 2:
        raise ValueError("El número debe ser mayor o igual a 2.")
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


# 3. Conversión de unidades
def convertir(valor, unidad_origen="m", **destinos):
    if not destinos:
        raise ValueError("Debes proporcionar al menos una unidad de destino.")
    resultados = {}
    for unidad, factor in destinos.items():
        if not isinstance(factor, (int, float)):
            raise ValueError(f"El factor para '{unidad}' debe ser numérico.")
        resultados[unidad] = valor * factor
    return resultados


# 4. Generador de IDs
def generador_ids(prefijo="ID"):
    contador = 0
    def generar():
        nonlocal contador
        contador += 1
        return f"{prefijo}_{contador}"
    return generar


# 5. Menú interactivo (CLI)
def menu():
    generador = None  # se declara fuera del bucle para conservar el estado
    while True:
        print("\nMenú:")
        print("1) Factorial")
        print("2) Primo")
        print("3) Conversión")
        print("4) Nuevo ID")
        print("0) Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "0":
            print("¡Hasta luego!")
            break

        elif opcion == "1":
            try:
                n = int(input("Ingrese un número entero: "))
                resultado = factorial(n)
                print(f"El factorial de {n} es: {resultado}")
            except ValueError as e:
                print(f"Error: {e}")

        elif opcion == "2":
            try:
                n = int(input("Ingrese un número entero: "))
                if es_primo(n):
                    print(f"{n} es un número primo.")
                else:
                    print(f"{n} no es primo.")
            except ValueError as e:
                print(f"Error: {e}")

        elif opcion == "3":
            try:
                valor = float(input("Ingrese el valor a convertir: "))
                unidad_origen = input("Ingrese la unidad de origen (m, km, cm): ")
                destinos = {
                    "m": 1,
                    "km": 0.001,
                    "cm": 100
                }
                resultados = convertir(valor, unidad_origen=unidad_origen, **destinos)
                for unidad, resultado in resultados.items():
                    print(f"{valor} {unidad_origen} son {resultado} {unidad}.")
            except ValueError as e:
                print(f"Error: {e}")

        elif opcion == "4":
            prefijo = input("Ingrese el prefijo del ID (por defecto 'ID'): ").strip()
            if not prefijo:
                prefijo = "ID"
            if generador is None:
                generador = generador_ids(prefijo)
            print(f"Nuevo ID generado: {generador()}")


# Ejecutar el menú si se llama directamente
if __name__ == "__main__":
    menu()
