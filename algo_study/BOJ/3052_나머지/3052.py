import sys
sys.stdin = open('input.txt')


new_Num = []
for i in range(10):
    numbers = int(input())
    # print(numbers)
    # for j in range(10):
    new_Num.append(numbers % 42)
print(len(set(new_Num)))
