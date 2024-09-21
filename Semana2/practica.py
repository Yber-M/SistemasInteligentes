# 1.-Hacer un algoritmo que imprima los numeros del 1 al 100
print('\n# Ejercicio 1')
for i in range(1, 101):
    print(i)
    
# 2.-Hacer un algoritmo que imprima los numeros del 100 al 0, en orden decreciente.
print('\n# Ejercicio 2')
for i in range(0, 101):
    print(100 - i)

# 3.-Hacer un algoritmo que imprima los numeros pares entre 0 y 100. 
print('\n# Ejercicio 3')
for i in range (2, 100):
    if i % 2 == 0:
        print(i)
# 4.-Hacer un programa que imprima la suma de los 100 primeros numeros.
print('\n# Ejercicio 4')
suma = 0;
for i in range (1, 101):
    suma += i
    print(suma)

# 5.-Hacer un programa que imprima los numeros impares hasta el 100 y que imprima cuantos impares hay.
print('\n# Ejercicio 5')
cont = 0
for i in range (1, 100, 2):
    print(i)
    cont += 1
print("El total de números impares es:", cont)

# 6.-Introducir un numero por teclado. Que nos diga si es par o impar.
print('\n# Ejercicio 6')
num = int(input('Ingrese un número:\n'))

if num % 2 == 0:
    print('El número ', num, ' es PAR')
else:
    print('El número ', num, ' es IMPAR')
# 7.-Imprimir y contar los multiplos de 3 desde la unidad hasta un numero que introducimos por teclado.
print('\n# Ejercicio 7')
contador = 0;
limitador = int(input('Ingrese hasta el número que desea imprimir :'))
for i in range(1, limitador):
    if i % 3 == 0:
        print(i)
        contador += 1
print('Los números de 1 a', limitador, '. Tienen un TOTAL de', contador, 'multiplos de tres.');
# 8.-Hacer un programa que imprima los numeros del 1 al 100. Que calcule la suma de todos los numeros pares por un lado, y por otro, la de todos los impares.
print('\n# Ejercicio 8')
sumPar = 0
sumImpar = 0

for i in range(1, 101):
    if i % 2 == 0:
        sumPar += i
    else:
        sumImpar += i
print(sumPar)
print(sumImpar)

# 9.-Hacer un programa que imprima el mayor y el menor de una serie de cinco numeros que vamos introduciendo por teclado. 

# 10.-Imprimir diez veces la serie de numeros del 1 al 10.

# 11.-Hacer un programa que cuente las veces que aparece una determinada letra en una frase que introduciremos por teclado.

# 12.-Crear un algoritmo que calcule la raíz cuadrada del número que introduzca el usuario. Si se introduce un número negativo, debe mostrar un mensaje de error y volver a pedirlo (tantas veces como sea necesario).

# 13.-Escribir un algoritmo que, para cualquier número de segundos inferior a un millón, calcule su equivalente en días, horas, minutos y segundos.

# 14.-Escribir un algoritmo que imprima el mínimo, el máximo y la media de tres números.

# 15.-Escribir un algoritmo que encuentre las raices de una ecuación de segundo grado, si el discriminante es cero que diga que la solución es única y si es menor a cero que diga que el sistema no tiene solución.