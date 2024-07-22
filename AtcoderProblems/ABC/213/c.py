H, W, N = map(int, input().split())
A, B = [], []
for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

A_dict = {x: i+1 for i, x in enumerate(sorted(list(set(A))))}
B_dict = {y: i+1 for i, y in enumerate(sorted(list(set(B))))}

for i in range(N):
    print(A_dict[A[i]], B_dict[B[i]])