print('Conversion de rut a la menor cantidad de billetes y monedas chilenas, se usan los siguientes billetes y monedas')
print(' Billetes:')
print(' - $20000')
print(' - $10000')
print(' - $5000')
print(' - $2000')
print(' - $1000')
print(' Monedas:')
print(' - $500')
print(' - $100')
print(' - $50')
print(' - $10')
rut = int(input('Ingresa tu rut sin punto ni guion: '))
billete20 = 0
billete10 = 0
billete5 = 0
billete2 = 0
billete1 = 0
moneda500 = 0
moneda100 = 0
moneda50 = 0
moneda10 = 0

while rut >= 20000:
    billete20 = billete20 + 1
    rut = rut - 20000

while rut >= 10000:
    billete10 = billete10 + 1
    rut = rut - 10000

while rut >= 5000:
    billete5 = billete5 + 1
    rut = rut - 5000

while rut >= 2000:
    billete2 = billete2 + 1
    rut = rut - 2000

while rut >= 1000:
    billete1 = billete1 + 1
    rut = rut - 1000

while rut >= 500:
    moneda500 = moneda500 + 1
    rut = rut - 500

while rut >= 100:
    moneda100 = moneda100 + 1
    rut = rut - 100

while rut >= 50:
    moneda50 = moneda50 + 1
    rut = rut - 50

while rut >= 10:
    moneda10 = moneda10 + 1
    rut = rut - 10

print('Billetes de $20000:', billete20)
print('Billetes de $10000:', billete10)
print('Billetes de $5000:', billete5)
print('Billetes de $2000:', billete2)
print('Billetes de $1000:', billete1)
print('Monedas de $500:', moneda500)
print('Monedas de $100:', moneda100)
print('Monedas de $50:', moneda50)
print('Monedas de $10:', moneda10)
print('Dinero sobrante: $' + str(rut))
# conversion de billetes y monedas al valor original para validar que sea igual al rut ingresado
print('Total:', billete20 * 20000 + billete10 * 10000 + billete5 * 5000 + billete2 * 2000 + billete1 * 1000 + moneda500 * 500 + moneda100 * 100 + moneda50 * 50 + moneda10 * 10 + rut)
