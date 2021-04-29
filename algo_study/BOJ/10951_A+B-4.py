import sys
sys.stdin = open('input.txt')

# try, except 해야됨
while True:
    try:
        a, b = map(int, input().split())
    except:
        break
    print(a + b)