control = True
nums = []
bigger = 0
two_five = []

while control and len(nums) <= 150:
    num = int(input("Digite o numero: "))
    if num == 0:
        control = False
    else:
        nums.append(num)

for i in nums[::-1]:
    if len(str(i)) == 2 and i % 5 == 0:
        two_five.append(i)
    if i % 7 != 0 and i > bigger:
        bigger = i

for i in two_five:
    print(i,)
print(bigger)