ma = 5
qtd = 0
qtd2d = 0
lis = [0]*ma
mai7 = -99999999999999999999

num = int(input('Informe um numero inteiro: '))

while num >= 0:
    num = int(input('Informe um numero inteiro: '))

while (num != 0) and (qtd < ma):
    qtd = qtd + 1
    if ((num % 5 == 0) and (num > -100) and (num < -9)):
        lis[qtd2d] = num
        qtd2d = qtd2d + 1
    if ((num > mai7) and ((num % 7) != 0)):
        mai7 = num


if qtd2d == 0:
    print('Nenhum número de dois digitos multiplo de 5 digitado: ')
else:
    lis = lis[:qtd2d]
    lis.reverse()

if mai7 == -99999999999999999999:
    print('Nenhum não multiplo de 7 digitado')
else:
    print('Maior não multiplo 7 =', mai7)