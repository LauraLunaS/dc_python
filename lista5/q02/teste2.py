def gerar_tabela(file_path):
    TB = {}
    try:
        file = open(file_path)
        for line in file:
            codigo = line[0:2]
            centro = line[3:27]
            TB[codigo] = centro
        return TB
    except IOError as mes:
        print('Erro na leitura do arquivo -: ',mes)

try:
    TB = gerar_tabela('lista5/q02/centros.txt')
    dsc = open('lista5/q02/discip.txt') 
    dscComp = open('discipCompleto.arq' ,'w')
    for line in dsc:
        codigo = line[0:5]
        nome = line[5:40]
        creditos = line[42:44]
        cod_centro = line[45:47]
        nome_centro = TB[cod_centro]
        dscComp.write(f'{codigo} {nome} {creditos} {cod_centro} {nome_centro}\n')
except IOError as mes:
    print('Erro na leitura do arquivo -: ',mes)