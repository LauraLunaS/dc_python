#para padrao de leitura q pare com o 0
# num = 1
# nums = []

# while num != 0:
#     num = int(input('N: '))
#     if num != 0:  
#         nums.append(num)
    
# print(nums)

#parar com nao ser positivo 
# while num > 0:
#     num = int(input('N: '))
#     if num > 0:  
#         nums.append(num)
    
# print(nums)

#parar com numero diferente de 0 e ate determinada contagem
num = 0
contador = 0
nums = []

while num != -999999 and contador < 3:
    num = int(input('Número: '))
    contador = contador + 1
    if num != -999999:
        nums.append(num)

print(nums)