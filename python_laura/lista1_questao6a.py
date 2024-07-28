S = 0
N = int(input())

while N >= 51:
    N = int(input('A série só vai até o quinquagésimo termo. Tente outro.'))

for i in range(1,N+1):
    if i%2 == 1:
        a_i = 2
    else:
        a_i = -5
    b_i = 500 - (i-1) * 10 
    c_i = a_i / b_i 
    S+=c_i
    print(S)