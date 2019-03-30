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
if cono:
    volumen = (1/3) * math.pi * r ** 2 * h
    print('Datos ingresados para el cono:')
    print('  Radio:', r)
    print('  Altura:', h)
    print('Volumen del cono:', volumen)
elif cilindro:
    volumen = math.pi * r ** 2 * h
    print('Datos ingresados para el cilindro:')
    print('  Radio:', r)
    print('  Altura:', h)
    print('Volumen del cilindro:', volumen)
elif piramide:
    volumen = (1/3) * r ** 2 * h
    print('Datos ingresados para la piramide:')
    print('  Radio:', r)
    print('  Altura:', h)
    print('Volumen de la piramide:', volumen)
