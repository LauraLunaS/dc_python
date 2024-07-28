num = -1
nums = []
nums2 = []

while num != 0:
    num = int(input('Digite um num inteiro negativo: '))
    if num != 0:  
        nums.append(num)
    
    if num > -100 and num < -9 and num % 5 == 0:
        nums2.append(num)

print(f'Negativos com dois dígitos significativos e múltiplos de 5: {nums2}')


maior = None
for i in nums:
    if i % 7 == 0:
        if maior is None or i > maior:
            maior = i

if maior is not None:
    print(f'O maior número múltiplo de 7 é: {maior}')
else:
    print('Nenhum número múltiplo de 7 foi encontrado.')


