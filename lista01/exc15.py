n = int(input('Digite um número: '))

lista = []

for i in range(1, n // 2 + 1):
    if (n % i) == 0:
     lista.append(i)

soma = sum(lista)

if n == soma:
   print('Você informou um número perfeito.')