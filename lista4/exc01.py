def separa (num): 
    l = []
    while num > 0:
        v = num % 10
        num = num // 10
        l.insert(v, 0)
        print('Desmembrando: ')
    return 1

def conta (nu, di):
    li = separa (nu)
    r = 0
    for e in li:
        if e == di:
            r = r + 1
    return r 


n = int(input('N ='))

while n > 99999: 
    n = int(input('N ='))

while n > 0:
    res = conta(n, 9)
    print(n, res)
    n = int(input('N = '))

    while n > 99999:
        n = int(input('N = '))