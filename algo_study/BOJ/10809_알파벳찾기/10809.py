import sys
sys.stdin = open('input.txt')

S = str(input())
alpabet = [chr(i) for i in range(97,122+1)]

for i in alpabet:
    try:
        print(S.index(i), end= ' ')
    except:
        print(-1, end = ' ')

# 이 문제는 이해가 잘 안되서 다른 사람 코드를 많이 참고했고 다른 분들의 코드도
# 다양해서 나에게 맞는 풀이를 하는게 필요할 듯 딕셔너리 하는것도 이해해보기