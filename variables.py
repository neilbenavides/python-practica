numero_decimal = 3.1416
parte_entera = 3
nombre = "Pi"
booleano = True

print(nombre, "es un número que relaciona la longitud de una circunferencia y su diámetro")
print("El valor de pi es", numero_decimal)
print("La parte entera de pi es", parte_entera)

# En Python no hay un límite en los valore enteros que se puede representar.
""" El límite estándar para los flotantes en Python es aproximadamente ±1.7976931348623157 x 10^308, 
pero depende básicamente de la arquitectura de la máquina.""" 

#Fórmula de la suma de los primeros n números pares.

print("ingrese un número par")
n = int(input())
n_adicion = n + 1
contador = 0

for n_adicion in range(2,n_adicion,2):
      contador = contador + n_adicion
      print("el resultado es", contador)