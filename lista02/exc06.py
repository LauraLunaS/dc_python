lista_N = [1, 2, 3]
lista_I = []
lista_P = []

for i in lista_N:
    print(i)
    if (i % 2) == 0:  
        lista_P.append(i) 
    else:
        lista_I.append(i)


print(lista_N)
print(lista_P)
print(lista_I)