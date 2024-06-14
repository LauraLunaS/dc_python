string1 = input('busca: ')
string2 = input('texto: ')

cont = 0

res = string2.find(string1)

while res != -1:
    cont += 1
    res = string2.find(string1, res + 1)
print('Res = ', cont)

