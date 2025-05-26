# Calculadora IMC 
peso = float(input("Ingrese su peso en kilogramos (kg): "))
altura = float(input("Ingrese su altura en metros (m): "))

# Formula de IMC peso / (altura ** altura)
imc = peso / (altura**2)

# Mostrar el IMC con dos decimales  
print (f"\nTu IMC es: {imc:.2f}")

# Clasificar el resultado 
if imc < 18.5:
    print("Tienes bajo peso")
elif imc < 24.9:
    print("Tienes un peso normal")
elif imc < 29.9:
    print("Tienes sobre peso")
else:
    print("Tienes obesidad")
