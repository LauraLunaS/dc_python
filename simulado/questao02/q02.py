num = -1
numeros = []
numeros_filtrados = []
contador = 0

ultimo_indice = len(numeros) - 1

while contador < 4 and num < 0:
    num = int(input("Digite um número inteiro negativo (ou 0 para parar): "))
    if num < 0:
        numeros.append(num)
        contador += 1

print(numeros)


for num in numeros[::-1]:
    if num >= -99 and num <= -10 or num <= -10 and num >= -99:
        if num % 5 == 0:
            numeros_filtrados.append(num)

print(f"Números com dois dígitos significativos e múltiplos de 5 (na ordem inversa): {numeros_filtrados}")


maior_num = max(numeros)
if not maior_num % 7 == 0:
    print(maior_num)