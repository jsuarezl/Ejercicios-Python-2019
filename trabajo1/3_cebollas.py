print('Calculo de camiones, sacos, lotes y cebollas en base al rut sin punto ni guion')
print(' - Un lote contiene 4 cebollas')
print(' - Un saco contiene 12 lotes')
print(' - Un camion contiene 150 sacos')
cebollas = int(input('Ingresa tu rut sin punto ni guion: '))
lotes = 0  # 4 cebollas
sacos = 0  # 12 lotes
camiones = 0  # 150 sacos

while cebollas >= 4:
    lotes = lotes + 1
    cebollas = cebollas - 4

while lotes >= 12:
    sacos = sacos + 1
    lotes = lotes - 12

while sacos >= 150:
    camiones = camiones + 1
    sacos = sacos - 150

print('Camiones:', camiones)
print('Sacos:', sacos)
print('Lotes:', lotes)
print('Cebollas:', cebollas)
# conversion de camiones, sacos y lotes a cebollas + cebollas sobrantes para validar que es igual al rut ingresado
print('Total:', camiones * 150 * 12 * 4 + sacos * 12 * 4 + lotes * 4 + cebollas)
