menor = int(input())
maior = int(input())

if maior < menor:
    maior, menor = menor, maior
if maior == menor:
    if maior %2==0:
        print(0)
    else:
        print(maior)

i = menor
S = 0
while i<maior+1:
    if i%2 ==1:
        S+=i
    i+=1
print(S)
