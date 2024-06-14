import math

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

while n2 == 0:
    n2 = int(input('Digite o segundo número: '))
else:
    resto = n1 % n2 

    if resto == 0:
        print(n1)
    else: 
        quadrado = math.sqrt(resto)
        print(quadrado)
