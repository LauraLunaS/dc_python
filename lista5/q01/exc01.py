try:
    arqEnt = open('lista5/discip.txt', 'r')
except IOError:
    print("Arquivo 'lista5/discip.txt' não encontrado.")

linhas = arqEnt.readlines()

arqEnt.close()

print("Conteúdo do arquivo:")

novas_linhas = []
disciplinas_originais = 0
disciplinas_com_credito_alterado = 0

for linha in linhas:
    codigo = linha[0:5]
    nome = linha[6:35]
    credito = linha[42:44]
    codigo_com = linha[0:2]

    disciplinas_originais += 1
    
    if codigo == 'IF125' or codigo == 'IF380':
        linhas.remove(linha)

    if codigo_com == 'MA':
        credito = '5'
        disciplinas_com_credito_alterado += 1
    
    carga_horaria = int(credito) * 15  

    nova_linha = f"{codigo} / {nome} / {credito} / {carga_horaria}\n"
    novas_linhas.append(nova_linha)


arqSai = open('dicip.new', 'w')
arqSai.writelines(novas_linhas)


print(f"Número de disciplinas no arquivo original: {disciplinas_originais}")
print(f"Número de disciplinas com crédito alterado para '5': {disciplinas_com_credito_alterado}")


