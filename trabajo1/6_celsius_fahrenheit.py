# Conversion de fahrenheit a celsius y viceversa, obteniendo un sub texto dentro de una cadena de texto

temp = input('Ingrese la temperatura que desee convertir (ej.: 45F, 102C) : ')
ultima = temp[len(temp)-1]

if ultima == 'F':
    c = (float(temp[:-1]) - 32) * 5/9
    print('Celsius:', c)
elif ultima == 'C':
    f = (float(temp[:-1]) * 9 / 5) + 32
    print('Fahrenheit:', f)
else:
    print('No has ingresado un formato de temperatura valido.')
