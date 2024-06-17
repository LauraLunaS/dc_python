pessoas = []

codigo = 1
contine = False

while contine == True:
   codigo = int(input('Digite o codigo da pessoa: '))
   if codigo > 0:
    nome = input('Digite o nome da pessoa: ')
    salario = float(input('Digite o salario da pessoa: '))
    pessoa = (codigo, nome, salario)
    pessoas.append(pessoa) 

print(pessoas)

salario_max = float(input('Informe o valor maximo do salário: '))

if salario_max < 0:
  print('Digite seu dados novamente')
  contine = True
else:
  contine = False


