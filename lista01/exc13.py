n1 = int(input('n1: '))
n2 = int(input('n2: '))

while n1 < 1:
    n1 = int(input('n1: '))

while n2 < 1:
    n2 = int(input('n2: '))


mmc = n2
if n1 > mmc:
    mmc = n1

while ((mmc % n1) != 0) or ((mmc % n2) != 0):
    mmc = mmc + 1


print('MDC: ', mmc)
