H, W, X, Y = map(int, input().split())
A = [[0]*W for _ in range(H)]
B = []

for _ in range(H + X):
    B.append(list(map(int, input().split())))
    
for x in range(X):
    for y in range(W):
        A[x][y] = B[x][y]

for y in range(Y):
    for x in range(H):
        A[x][y] = B[x][y]

for x in range(X, H):
    for y in range(Y, W):
        A[x][y] = B[x][y] - A[x - X][y - Y]
        
for row in A:
    print(*row)