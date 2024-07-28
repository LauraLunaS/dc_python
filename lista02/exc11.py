
M = int(input("Digite o valor de M (<= 4): "))
N = int(input("Digite o valor de N (<= 8): "))


matriz = []


for i in range(M):
    linha = []
    for j in range(N):
        valor = int(input(f"Digite o elemento [{i+1}][{j+1}]: "))
        linha.append(valor)
    matriz.append(linha)

multiplos_de_6 = []

for j in range(N):
    for i in range(M):
        if matriz[i][j] % 6 == 0:
            multiplos_de_6.append(matriz[i][j])

print("\nMatriz:")
for i in range(M):
    for j in range(N):
        print(matriz[i][j], end=" ")
    print()

print("\nMúltiplos de 6:")
print(multiplos_de_6)
