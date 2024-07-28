TB_cursos = {}
cod = int(input('digite o codigo do curso: '))
while cod!=0:
	nome = input('digite o nome do curso: ')
	centro = int(input('digite o numero do centro: '))
	TB_cursos[cod] = (nome,centro)
	cod = int(input('digite o codigo do curso: '))

lista_centros =[]
for chave in TB_cursos:
    lista_centros.append(TB_cursos[chave][1])

centro = 1
centro = int(input('digite o centro para ser printado: '))
while centro >0:
    if centro in lista_centros:
        for chave in TB_cursos:
            if TB_cursos[chave][1] == centro:
                      print(chave, TB_cursos[chave][0])
    else:
        print("Nenhum curso encontrado")
    centro = int(input('digite o centro para ser printado: '))