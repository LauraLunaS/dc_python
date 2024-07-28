def calcular_serie(n):
    if n <= 0:
        return 0
    n = 37
    n2 = 38
    numerador = n * n2
    denominador = 1
    soma = 0
    
    for i in range(1, n + 1):
        numerador = (38 - i) * (39 - i)
        denominador = i
        soma += numerador / denominador

    return soma

def main():
    qtd = int(input("Quantas vezes deseja calcular o valor da série? "))
    
    for _ in range(qtd):
        n = int(input("Digite o número de termos desejado: "))
        resultado = calcular_serie(n)
        print(f"O valor da série com {n} termos é {resultado:.4f}")

if __name__ == "__main__":
    main()

