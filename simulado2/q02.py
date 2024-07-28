num = 1
contador = 0
nums = []

while num != 0 and contador < 3:
    num = int(input('Informe um número inteiro positivo: '))
    contador = contador + 1
    nums.append(num)

print(nums)

for i in nums:
    if i < 0:
        qtd_negativo = i
        print(f'Números negativos: {qtd_negativo}')
    if (i > 999) and (i < 9999):
        if i < 5100:
            print(f'Digitos signficativos e menores que 5100: ', i)
        elif i > 5100:
            print(f'Digitos signficativos e maiores ou igual a 5100', i)

nums_three = []
contador2 = 0
for i in nums: 
    while i > 99 and i < 999:
        contador2 = contador2 + 1
        nums_three.append(i)

soma = 0
for i in nums_three:
    soma += i

media = soma / contador2
print('Média dos números positivos de 3 digitos: ', media)




nums_negativos = []
for i in nums:
    if i < 0:
        nums_negativos.append(i)
print('Maior número negativo lido: ', max(nums_negativos))
