decimal = 3.1416
entero = 3
cadena = "Pi"
booleano = True
nulo = None

resultado = cadena + " es un número que relaciona la longitud de una circunferencia y su diámetro, cuyo valor es " + str(decimal) + " y su parte entera es " + str(entero)

print(resultado)

# En Python no hay un límite en los valore enteros que se puede representar.
""" El límite estándar para los flotantes en Python es aproximadamente ±1.7976931348623157 x 10^308, 
pero depende básicamente de la arquitectura de la máquina.""" 

#Fórmula de la suma de los primeros n números pares.

print("ingrese un número par")
n = int(input())
suma = 0
for i in range(2, n + 1, 2):
      suma+= i

print("el resultado es", suma)