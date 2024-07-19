n = int(input())
LA = [list(input().split()) for _ in range(n)]

numseq = set()

for i in range(n):
    numseq.add(' '.join(LA[i][1:]))

print(len(numseq))    
