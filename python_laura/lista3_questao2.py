tamanho_tabela = int(input('digite o tamanho da tabela: '))

TB_pessoas = [0] * tamanho_tabela

for i in range(tamanho_tabela):
    codigo = input('digite um codigo: ')
    nome = input('digite um nome: ')
    salario = float(input())
    TB_pessoas[i] = (codigo, nome, salario)

salario_max = float(input())

while salario_max < 0:
    salario_max = float(input())


num_pessoas = 0
media_salario = 0
for i in range(len(TB_pessoas)):
    if TB_pessoas[i][2] <= salario_max:
        num_pessoas +=1
        media_salario += TB_pessoas[i][2]
        print(TB_pessoas[i])
media_salario /= num_pessoas
print(num_pessoas)
print(media_salario)
