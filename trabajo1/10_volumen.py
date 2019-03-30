# Calculo del volumen de un cono, cilindro y piramide de base cuadrada usando la base y altura

import math

cono = False
cilindro = False
piramide = False

figura = input('Ingrese el nombre de la figura geometrica, valores permitidos: cono, cilindro, piramide : ')

if figura == 'cono':
    cono = True
elif figura == 'cilindro':
    cilindro = True
elif figura == 'piramide':
    piramide = True
else:
    print('No has ingresado un valor valido.')
    exit()
r = int(input('Ingrese un valor para la base: '))  # base
h = int(input('Ingrese un valor para la altura: '))  # altura
volumen = 0
if cono:  # en el cono la base se usa como radio
    volumen = (1/3) * math.pi * r ** 2 * h
    print('Datos ingresados para el cono:')
    print('  Radio:', r)
    print('  Altura:', h)
    print('Volumen del cono:', volumen)
elif cilindro:  # en el cilindro la base se usa como radio
    volumen = math.pi * r ** 2 * h
    print('Datos ingresados para el cilindro:')
    print('  Radio:', r)
    print('  Altura:', h)
    print('Volumen del cilindro:', volumen)
elif piramide:  # en la piramide la base se usa como un lado del cuadrado que forma la base
    volumen = (1/3) * r ** 2 * h
    print('Datos ingresados para la piramide:')
    print('  Radio:', r)
    print('  Altura:', h)
    print('Volumen de la piramide:', volumen)
