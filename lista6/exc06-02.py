def calcula_termo(n):
    numerador = (38 - n) * (39 - n)
    denominador = n
    return numerador / denominador

def calcula_serie(n):
    if n == 1:
        return calcula_termo(n)
    else:
        return calcula_termo(n) + calcula_serie(n - 1)


# Exemplo de uso
n = 3  # Você pode mudar o valor de n para calcular a série com mais termos
resultado = calcula_serie(n)
print(f"O valor da série com {n} termos é: {resultado}")
