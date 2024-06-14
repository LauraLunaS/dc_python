n1 = float(input('Digite o primeiro número 1: '))
n2 = float(input('Digite o primeiro número 2: '))
n3 = float(input('Digite o primeiro número 3: '))


def ler_numero():
    if isinstance(n1, float) and isinstance(n2, float) and isinstance(n3, float) == False:
        media = (n1 + n2 + n3 / 3)
        print(f'a média dos números {n1}, {n2} e {n3} é igual a {media}')
    else: 
        print('Tente novamente mais tarde')


ler_numero()