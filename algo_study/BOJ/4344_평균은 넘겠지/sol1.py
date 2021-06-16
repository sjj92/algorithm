import sys

sys.stdin = open('input.txt')

for _ in range(int(input())):
    scores = list(map(int, input().split()))
    avg = float(sum(scores[1:]) / scores[0])
    avg_over = 0

    for s in scores[1:]:
        if s > avg:
            avg_over += 1

    print(f"{avg_over / scores[0] * 100:.3f}%")
