A = int(input())

if A // 4 == 0 and (A // 400 == 0 or A // 100 != 0):
    print(1)
else:
    print(0)
