alunos = []

cpf = 1
contine = False

while (cpf > 0) and (cpf <= 3):
   cpf = int(input('Digite o cpf do aluno: '))
   if cpf > 0:
    nome = input('Digite o nome do aluno: ')
    idade = int(input('Digite a idade do aluno: '))
    aluno = (cpf, nome, idade)
    alunos.append(aluno) 

print(alunos)