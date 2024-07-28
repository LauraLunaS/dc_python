
def MelhoresClientes(empresa, valor):
    with open(f"Simulado/{empresa}.txt", 'r') as arq:
        melhores = []
        soma = 0
        for i in arq:
            if int(i[8:15]) > 100:
                dado = i[0:5] + " " + i[8:15]
                soma += int(i[8:15])
                melhores.append(dado)
    
    with open(f"Simulado/{empresa}Melhores.txt", 'w') as arq:
        for i in melhores:
            arq.write(i + "\n")
    
    print("Empresa:", empresa)
    print("Número de registros: ", len(melhores))
    print("Média de pontuação: ", soma/len(melhores))

n = int(input("Quantas empresas? "))

for i in range(n):
    try:
        nome = input("Digite o nome da empresa: ")
        valor = input("Digite o valor: ")

        MelhoresClientes(nome, valor)
    except:
        print("Erro!!")