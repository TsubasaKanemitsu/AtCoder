S, T = list(map(int, input().split()))

cnt = 0
for a in range(S + 1):
    for b in range(S + 1 - a):
        for c  in range(S + 1 - a - b):
            if S >= (a + b + c) and a * b * c <= T:
                cnt += 1
print(cnt)