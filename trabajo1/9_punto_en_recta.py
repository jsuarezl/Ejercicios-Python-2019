# ejemplo funcional
p1 = [2, 2]  # punto 1
p2 = [14, 10]  # punto 2

m = (p2[1] - p1[1]) / (p2[0] - p1[0])  # pendiente

p3 = [8, 6]  # punto 3

y = p3[1]  # x del punto 3
x = p3[0]  # y del punto 3

e = (y - p1[1]) == m * (x - p1[0])
print('Ejemplo funcional:')
print('  Punto 1: (2, 2)')
print('  Punto 2: (14, 10)')
print('Punto en la recta:')
print('  Punto 3: (8, 6)')
print(' ')
print('Se intersecta:', e)

for i in range(0, 3):
    print(' ')

# ejemplo no funcional
p1 = [2, 2]  # punto 1
p2 = [14, 10]  # punto 2

m = (p2[1] - p1[1]) / (p2[0] - p1[0])  # pendiente

p3 = [8, 7]  # punto 3

y = p3[1]  # x del punto 3
x = p3[0]  # y del punto 3

e = (y - p1[1]) == m * (x - p1[0])
print('Ejemplo no funcional:')
print('  Punto 1: (2, 2)')
print('  Punto 2: (14, 10)')
print('Punto en la recta:')
print('  Punto 3: (8, 7)')
print(' ')
print('Se intersecta:', e)

for i in range(0, 3):
    print(' ')


p1[0] = int(input('Ingrese un valor para x en el punto 1: '))
p1[1] = int(input('Ingrese un valor para y en el punto 1: '))
p2[0] = int(input('Ingrese un valor para x en el punto 2: '))
p2[1] = int(input('Ingrese un valor para y en el punto 2: '))
p3[0] = int(input('Ingrese un valor para x en el punto 3: '))
p3[1] = int(input('Ingrese un valor para y en el punto 3: '))

m = (p2[1] - p1[1]) / (p2[0] - p1[0])  # pendiente
y = p3[1]  # x del punto 3
x = p3[0]  # y del punto 3
e = (y - p1[1]) == m * (x - p1[0])

print('Datos ingresados: ')
print('  Punto 1: (' + str(p1[0]) + ',' + str(p1[1]) + ')')
print('  Punto 2: (' + str(p2[0]) + ',' + str(p2[1]) + ')')
print('  Punto 3: (' + str(p3[0]) + ',' + str(p3[1]) + ')')
print('Se intersecta:', e)
