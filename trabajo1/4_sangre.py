grupo1 = ['AB', 'BA']
grupo2 = ['AA', 'AO']
grupo3 = ['BB', 'BO']
grupo4 = ['OO']

p = input('Ingrese la combinacion genetica del padre: ')
if len(p) != 2:
    print('No has ingresado una combinacion genetica valida.')
    exit()
m = input('Ingrese la combinacion genetica de la madre: ')
if len(m) != 2:
    print('No has ingresado una combinacion genetica valida.')

combinaciones = [p[0] + p[1], m[0] + m[1], p[0] + m[0], p[0] + m[1], p[1] + m[0], p[1] + m[1]]
combinaciones = list(dict.fromkeys(combinaciones))

for combinacion in combinaciones:
    if combinacion in grupo1:
        grupo1 = []
        print('Es posible tener hijo de GRUPO I')
    elif combinacion in grupo2:
        grupo2 = []
        print('Es posible tener hijo de GRUPO II')
    elif combinacion in grupo3:
        grupo3 = []
        print('Es posible tener hijo de GRUPO III')
    elif combinacion in grupo4:
        grupo4 = []
        print('Es posible tener hijo de GRUPO IV')
