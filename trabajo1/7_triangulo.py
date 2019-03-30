import math

a = int(input('Lado a: '))
b = int(input('Lado b: '))
c = int(input('Lado c: '))

A = int(math.acos((b**2 + c**2 - a**2) / (2*b*c)) * (180 / math.pi))
B = int(math.acos((a**2 + c**2 - b**2) / (2*a*c)) * (180 / math.pi))
C = int(math.acos((a**2 + b**2 - c**2) / (2*a*b)) * (180 / math.pi))

if A < 90 and B < 90 and C < 90:
    print('ACUTANGULO')
elif A == 90 or B == 90 or C == 90:
    print('RECTANGULO')
elif A > 90 or B > 90 or C > 90:
    print('OBTUSANGULO')
