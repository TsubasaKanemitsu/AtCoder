n, m = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

cur_a = 0
cur_b = 0
res = 10 ** 9 + 1
while cur_a < len(A) and cur_b < len(B):
    res = min(res, abs(A[cur_a] - B[cur_b]))

    if A[cur_a] > B[cur_b]:
        cur_b += 1
    else:
        cur_a += 1
print(res)