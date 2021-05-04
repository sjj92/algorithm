import sys
sys.stdin = open('input.txt')

# A = int(input())
# B = int(input())
# C = int(input())
#
# total = A * B * C
# numbers = list(str(total))
# # print(total)




################################

a = int(input())
b = int(input())
c = int(input())

result = list(str(a * b * c))
for i in range(10):
    print(result.count(str(i)))