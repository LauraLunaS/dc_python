def melhores_cliente(nome, base):
    qtd = 0
    med = 0.0

    try:
        arqE = open(nome + '.txt', 'r')
        arqS = open(nome + 'Melhores.txt', 'w')
        for cli in arqE:
            mat = cli[0:5]
            sexo = cli[6]
            numPon = cli[8:15]
            nomCli = cli[16:51]
            if int(numPon) > base:
                arqS.write('%s %s' % (mat, numPon))
                qtd = qtd + 1
                med = med + int(numPon)
        arqE.close()
        arqS.close()
        print('Gravando arquivo da empresa', nome)

        if qtd == 0:
            print('Nenhum cliente selecionado')
        else:
            med = med / qtd
            print(f'Gravados, {qtd}, cliente com média ,{med}')
    except IOError:
        print('Erro no arquivo da empresa: ', nome)


n = int(input('Número de empresas: '))

while n < 1:
    n = int(input('Número de empresas: '))

for i in range(n):
    nomEmp = input('Nome; ')
    pontos  = int(input('Base de pontos: '))
    while pontos < 0:
        pontos  = int(input('Base de pontos: '))
    melhores_cliente (nomEmp, pontos)