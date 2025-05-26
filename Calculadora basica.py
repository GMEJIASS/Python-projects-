# Se le da a conocer al usuario cuales son las operaciones disponibles para ejecutar en la calculadora
print("Calculadora basica")
print("Las operaciones disponibles son: Suma, resta, multiplicacion,division")
# Le solicitamos al cliente los datos 
numero1= float(input("Introduce el primer numero: "))
operacion= input("Que operacion quieres realizar: (suma, resta, multiplicacion,division):")
numero2= float(input("Introduce el segundo numero: "))
# Evaluamos la operacion 
if operacion == "suma":
    resultado= numero1 + numero2
    print ("Resultado:", resultado)
elif operacion== "resta":
    resultado= numero1 - numero2 
    print("Resultado",resultado)
elif operacion== "multiplicacion":
    resultado= numero1 * numero2 
    print("Resultado", resultado)
elif operacion== "division":
    if numero2!= 0:
        resultado= numero1 / numero2
        print("Resultado:", resultado)
    else:
        print("Error: no se puede dividir por cero.")    
else:
    print("Operacion no valida")        

    
    