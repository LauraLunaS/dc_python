def carregar_profissoes(arquivo):
    profissoes = {}
    f = open(arquivo, 'r')
    linhas = f.readlines()
    for linha in linhas:
        codigo = int(linha[0:3])
        nome_area = linha[4:27]
        area = linha[30:37]
        profissoes[codigo] = nome_area
    f.close()
    return profissoes

def main():
    profissoes = carregar_profissoes('lista5/q03/profissoes.txt')
    codigos_inexistentes = []

    codigo = int(input("Digite o código da profissão (negativo ou zero para sair): "))
    while codigo > 0:
        if codigo in profissoes:
            print(f"Profissão: {profissoes[codigo]}")
        else:
            print("Profissão Inexistente")
            codigos_inexistentes.append(codigo)
        codigo = int(input("Digite o código da profissão (negativo ou zero para sair): "))

    f = open('lista5/q03/codigos_inexistentes.txt', 'w')
    for codigo in codigos_inexistentes:
        f.write(f"{codigo}\n")
    f.close()

    print("Programa encerrado.")

if __name__ == "__main__":
    main()
