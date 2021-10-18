import sys
sys.stdin = open('input.txt')


a, b = map(int, input().split())

# print(a, b)

if a > b:
    print('>')
elif a < b:
    print('<')
else:
    print('==')

