import sys
sys.stdin = open("input.txt")

def count(num1, num2):

    global cnt
    cnt += 1
    childs = tree[node]
    for new_node in childs:
        count(new_node)

T = int(input())

for tc in range(1, T+1):
    # 데이터 입력 방음
    V, E, num1, num2 = map(int, input().split())
    # print(V, E, num1, num2)
    info = list(map(int, input().split()))
    # print(info)

    # 트리를 만들어야 됨 - 트리를 부모, 자식 2개로 각각 만들어야 됨
    tree = [[] for _ in range(E + 2)]
    for i in range(E):
        parent, child = info[i*2: (i*2)+1]
        tree[parent].append(child)

    cnt = 0
    count(num1, num2)


def inorder(n):
    global result

    if 0 < n < (V + 1):

        left_child = n * 2
        inorder(left_child)

        result += node[n]

        right_child = n * 2 + 1
        inorder(right_child)


for tc in range(1, 11):
    V = int(input())

    left = [0] * (V + 1)
    right = [0] * (V + 1)
    node = [0] * (V + 1)

    for i in range(1, V + 1):
        if i < (V / 2):
            p, key, c1, c2 = input().split()
            p = int(p)
            c1 = int(c1)
            c2 = int(c2)

            node[p] = key

            left[p] = c1
            right[p] = c2
        elif i == (V / 2):
            p, key, c1 = input().split()
            p = int(p)
            c1 = int(c1)

            node[p] = key
            left[p] = c1
        else:
            p, key = input().split()
            p = int(p)

            node[p] = key

    result = ""
    inorder(1)

    print('#{} {}'.format(tc, result))