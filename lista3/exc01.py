cursos = []

print(cursos)

codigo = 1

while codigo > 0:
   codigo = int(input('Digite o codigo do curso: '))
   if codigo > 0:
    nome = input('Digite o nome do curso: ')
    centro = int(input('Digite o centro do curso: '))
    curso = (codigo, nome, centro)
    cursos.append(curso) 

print(cursos)


## PARA BUSCAR OS CODIGOS 
list_codigo = []
digit_codigo = 1

while digit_codigo > 0:
    digit_codigo = int(input('Informe o digito do codigo que voce deseja buscar: '))
    if digit_codigo > 0:
     list_codigo.append(digit_codigo)
     
print(list_codigo)

codigos = [curso[0] for curso in cursos]


for codigo in list_codigo:
    encontrado = False
    for curso in cursos:
        if curso[0] == codigo:
            print(f'O código {codigo} foi encontrado no curso {curso[1]}')
            encontrado = True
    if not encontrado:
        print(f'O código {codigo} não foi encontrado em nenhum curso')