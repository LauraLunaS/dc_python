nums = []
num = 1

while num > 0:
    num = int(input('Digite um número inteiro positivo de até 5 dígitos (ou um número 0 ou negativo para encerrar): '))
    if num > 0 and num <= 99999:
        nums.append(num)

def desmembrar_numero(numero):
    #separar cada digito do numero
    digitos = []
    while numero > 0:
        #obtendo o ultimo digito (o resto da divisao do numero por 10 resultara no ultimo digito)
        digito = numero % 10
        digitos.insert(0, digito)
        numero //= 10
        print(digitos)
    return digitos

def contar_digito(numero, algarismo):
    digitos = desmembrar_numero(numero)
    contagem = 0
    for digito in digitos:
        if digito == algarismo:
            contagem += 1
    return contagem


for numero in nums:
        contagem = contar_digito(numero, 9)
        print(f"O número {numero} contém o dígito 9 {contagem} vez(es).")

