lista = []
n = 1

while n != 0:
    n = int(input('Digite um número inteiro válido: '))
    lista.append(n)


if len(lista) > 1:
    lista.pop()


soma = sum(lista)
media = soma / len(lista)

print(f'Média: {media}')
