import sys
sys.stdin = open('input.txt')


new_number = []
for i in range(9):
    new_number.append(int(input()))

print(max(new_number))
print(new_number.index(max(new_number)) + 1)
    
