# N = int(input())
# i = 1
# n = -1
# if N>1:
#     while i<N:
#         if i%2==0:
#             n+=5
#         else:
#             n+=1
#         i+=1
# print(n)

N = int(input())
n = -1
if N>1:
    for i in range(1,N):
        if i%2==0:
            n+=5
        else:
            n+=1
print(n)
