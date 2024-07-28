num = 0
nums = []
nums2 = []
contador = 0

while num != -9 and contador <= 3:
    num = int(input('Digite um num inteiro negativo: ')) 
    nums.append(num)
    
    contador += 1

    qtd = 0

    for i in nums:
        qtd += 1 
        print('qtd de nums lidos: ', qtd)
        
    if num > 99 and num < 9999:
        nums2.append(num)

    

print(f'Negativos com dois dígitos significativos e múltiplos de 5: {nums2}')


menor = None
for i in nums:
    if i % 7 == 0:
        if maior is None or i > maior:
            maior = i

if maior is not None:
    print(f'O maior número múltiplo de 7 é: {maior}')
else:
    print('Nenhum número múltiplo de 7 foi encontrado.')


