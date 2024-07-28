def achar_centro(TB, codigo_centro):
    return TB[codigo_centro]
              
def gerar_tabela(file_path):
    TB = {}
    try:
        arq = open(file_path)
        for line in arq:
            codigo = line[0:2]
            centro = line[3:29]
            TB[codigo] = centro 
        return TB
    except IOError as mes:
        print('Erro no arquivo -', mes)

