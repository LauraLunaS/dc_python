try: 
    arqin = open('discip.old')
    arqout = open('discip.new' ,'w')
    for line in arqin:
        codigo = line[0:5]
        nome = line[6:41]
        creditos = line[42:44]
        if codigo != 'IF125' and codigo != 'IF380':
            creditos_int = int(creditos)
            carga_horaria = str((creditos_int)*15)
            if codigo[0:2] == 'MA':
                creditos = 5
                arqout.write(f'{codigo} {nome} {creditos} {carga_horaria}\n')
            else:
                arqout.write(f'{codigo} {nome} {creditos} {carga_horaria}\n')
    arqin.close()
    arqout.close()
except IOError as mens:
    print('ERRO em arquivo -', mens)
except:
    print('ERRO - Outros')


    
