# Solicitar o valor de n ao usuário
n = int(input('Informe um valor inteiro: '))

# Inicializar a soma
s = 0

# Calcular a soma da série
for i in range(1, n + 1):
    termo = (2 * i - 1) / i
    s += termo

# Exibir o resultado
print('Valor da sequencia: ', s)
