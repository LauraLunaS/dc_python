menor_numero = None

numero = int(input("Digite um número (0 para parar): "))

while numero != 0:
    if menor_numero is None or numero < menor_numero:
        menor_numero = numero
    numero = int(input("Digite um número (0 para parar): "))
    
if menor_numero is None:
    print("Nenhum número foi fornecido.")
else:
    print("O menor número fornecido foi:", menor_numero)