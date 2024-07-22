N = int(input())
A = list(map(int, input().split()))

AA = sorted([[i, a] for i, a in enumerate(A)], key=lambda x:x[1], reverse=True)
print(AA[1][0] + 1)