nombre = str(input("¿Cuál es tu nombre? "))
edad = int(input("¿Cuántos años tienes? "))
altura = float(input("¿Cuál es tu altura en metros? "))
peso = float(input("¿Cuál es tu peso en kg? "))
imc = peso / (altura * altura)

if imc < 18.5:
    Estado = "Peso bajo"
elif 18.5 <= imc < 24.9:
    Estado = "Peso normal"
elif 25.0 <= imc < 29.9:
    Estado = "Sobrepeso"
elif imc  >= 30.0:
    Estado = "Obesidad"

print(
    f"Nombre:{nombre} - edad:{edad}\n"
    f"Altura:{altura:.1f} - Peso: {peso:.1f}\n"
    f"IMC:{imc:.2f}\n"
    f"Estado:{Estado}"
    )
