import math

numero1 = float(input('Ingresa el primer numero: '))
if numero1 <= 100:
    print('El numero debe ser mayor a 100')
    exit()
numero2 = float(input('Ingresa el segundo numero: '))
if numero2 <= 100:
    print('El numero debe ser mayor a 100')
    exit()
numero3 = float(input('Ingresa el tercer numero: '))
if numero3 <= 100:
    print('El numero debe ser mayor a 100')
    exit()

promedio = (numero1 + numero2 + numero3) / 3
print('Promedio:', promedio)
decimal, entero = math.modf(promedio)
decimal = round(decimal, 3) * 1000
division = entero/decimal
print('Calculo:', entero, '/', decimal)
print('Division:', division)
decimal = int(math.modf(division)[0] * 1000)
print('Decimal:', decimal)
suma = 0
while decimal > 0:
    b = int(decimal % 10)
    decimal = int(decimal / 10)
    suma = suma + b

print('Suma:', suma)
