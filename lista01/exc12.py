n1 = int(input('n1: '))
n2 = int(input('n2: '))

while n1 < 1:
    n1 = int(input('n1: '))

while n2 < 1:
    n2 = int(input('n2: '))


mdc = n1
if n2 < mdc:
    mdc = n2

while ((n1 % mdc) != 0) or ((n2 % mdc) != 0):
    mdc = mdc - 1


print('MDC: ', mdc)
