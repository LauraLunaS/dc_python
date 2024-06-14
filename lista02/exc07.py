
alunos = int(input('Digite o número de alunos: '))
notas = []

for i in range(alunos):
    nota = float(input(f'Digite a nota final do aluno {i+1}: '))
    notas.append(nota)

media = sum(notas) / len(notas)
#print(media)

for j in notas:
    print(j)
    if j > media: 
        print(f'Notas maiores que a média {j}')

#print(notas)