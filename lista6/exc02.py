def inverter_numero(numero):
    invertido = 0
    num = numero
    while num > 0:
        digito = num % 10
        invertido = invertido * 10 + digito
        num //= 10
    return invertido

def main():
    num = int(input('Informe um numero inteiro (maior que 100): '))

    palindromos = []
    for i in range(100, num + 1):
        invertido = inverter_numero(i)
        if i == invertido:
            palindromos.append(i)

    if palindromos:
        print(f"Números palíndromos entre 100 e {num}:")
        for palindromo in palindromos:
            print(palindromo)
    else:
        print(f"Não há números palíndromos entre 100 e {num}.")

if __name__ == "__main__":
    main()
