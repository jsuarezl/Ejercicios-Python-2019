# Calculo del perimetro de un triangulo con 3 puntos en el plano

import math

print('Triangulo de ejemplo: ')
print(' a = (1, 1)')
print(' b = (3, 5)')
print(' c = (4, 2)')

xy1 = [1, 1]
xy2 = [3, 5]
xy3 = [4, 2]

l1 = math.sqrt((xy2[0] - xy1[0])**2 + (xy2[1] - xy1[1])**2)
l2 = math.sqrt((xy3[0] - xy1[0])**2 + (xy3[1] - xy1[1])**2)
l3 = math.sqrt((xy3[0] - xy2[0])**2 + (xy3[1] - xy2[1])**2)

print('Perimetro:', l1 + l2 + l3)

xy1[0] = int(input('Ingrese el x de a: '))
xy1[1] = int(input('Ingrese el y de a: '))
xy2[0] = int(input('Ingrese el x de b: '))
xy2[1] = int(input('Ingrese el y de b: '))
xy3[0] = int(input('Ingrese el x de c: '))
xy3[1] = int(input('Ingrese el y de c: '))

print('Triangulo ingresado: ')
print(' a =', xy1)
print(' b =', xy2)
print(' c =', xy3)

l1 = math.sqrt((xy2[0] - xy1[0])**2 + (xy2[1] - xy1[1])**2)
l2 = math.sqrt((xy3[0] - xy1[0])**2 + (xy3[1] - xy1[1])**2)
l3 = math.sqrt((xy3[0] - xy2[0])**2 + (xy3[1] - xy2[1])**2)

print('Perimetro:', l1 + l2 + l3)
