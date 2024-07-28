try:
    arqDiscip = open('lista5/q02/discip.txt', 'r')
    arqCentro = open('lista5/q02/centros.txt', 'r')
except IOError:
    print("Arquivo não encontrado.")

linhas_d = arqDiscip.readlines()
linhas_c = arqCentro.readlines()

arqDiscip.close()
arqCentro.close()

print("Conteúdo do arquivo:")


for linha in linhas_d:
    codigo = linha[0:5]
    print(codigo)
    nome = linha[6:35]
    print(nome)
    credito = linha[42:44]
    print(credito)
    codigo_centro = linha[45:48]
    print(codigo_centro)


for linha in linhas_c:
    codigo_centro = linha[0:2]
    print(codigo_centro)
    nome_cen = linha[3:6]
    print(nome_cen)


print(linhas_d)
print(linhas_c)
# arqSai = open('dicipCompleto.new', 'w')
# arqSai.writelines(novas_linhas)


