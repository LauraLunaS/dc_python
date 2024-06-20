pessoas = []

codigo = 1
contine = False

while codigo > 0:
   codigo = int(input('Digite o codigo da pessoa: '))
   if codigo > 0:
    nome = input('Digite o nome da pessoa: ')
    salario = float(input('Digite o salario da pessoa: '))
    pessoa = (codigo, nome, salario)
    pessoas.append(pessoa) 

print(pessoas)

salario_max = -1

while salario_max < 0:
    salario_max = float(input('Informe o valor máximo do salário: '))
    if salario_max > 0:
      print(f'Valor válido. {salario_max}')


for pessoa in pessoas: 
  if salario <= salario_max:
    print(f'A pessoa {pessoa} recebe o salario {salario} e o seu salário máximo é de {salario_max}')

