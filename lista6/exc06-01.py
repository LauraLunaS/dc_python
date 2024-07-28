def calcula_termo(n):
    if n % 2 == 1:  # Termo ímpar
        numerador = 2
    else:  # Termo par
        numerador = 5
    
    denominador = 500 - 10 * (n - 1)
    
    if n % 2 == 1:  # Termo ímpar (positivo)
        sinal = 1
    else:  # Termo par (negativo)
        sinal = -1
        
    return sinal * (numerador / denominador)

def calcula_serie(n):
    if n == 1:
        return calcula_termo(n)
    else:
        return calcula_termo(n) + calcula_serie(n - 1)

# Exemplo de uso
n = 4  # Você pode mudar o valor de n para calcular a série com mais termos
resultado = calcula_serie(n)
print(f"O valor da série com {n} termos é: {resultado}")
