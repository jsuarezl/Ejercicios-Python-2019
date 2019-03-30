import datetime

anionacimiento = int(input('Ingresa tu anio de nacimiento: '))
mesnacimiento = int(input('Ingresa tu mes de nacimiento: '))
dianacimiento = int(input('Ingresa tu dia de nacimiento: '))

hoy = datetime.datetime.now()
anio = hoy.year
mes = hoy.month
dia = hoy.day

edad = 0
if mesnacimiento <= mes and dianacimiento <= dia:
    edad = anio - anionacimiento
else:
    edad = anio - anionacimiento - 1

print('Edad:', edad)
