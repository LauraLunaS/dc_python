num = 0
contador = 0
soma = 0
nums = []
positivos = []

while num != -999999 and contador < 3:
    num = int(input('Número: '))
    if num != -999999:
        contador = contador + 1
        nums.append(num)

if contador > 0:
    print('Qtd de lidos: ', contador)

    for i in nums:                     
        if i < -99 and i > -1000:                                                    
            print('negativos com 3 digitos: -', i)

    for i in nums:
        if i > 99 and i < 1000:
            print('positivos com 3 digitos: ', i)
            soma += i

    print('Soma dos positivos com 3 dígitos: ', soma)

    for i in nums:
        if i > 0:
            positivos.append(i)

    if positivos:
        menor = positivos[0]
        for i in positivos:
            if i < menor:
                menor = i

        print('Menor número: ', menor)
