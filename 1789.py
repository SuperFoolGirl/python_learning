data = list(map(int, input().split()))
n, m, k = data[0], data[1], data[2]
matrix = [[False for _ in range(n)] for _ in range(n)]

def fire(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return
    matrix[x][y] = True

for i in range(m):
    data = list(map(int, input().split()))
    x, y = data[0] - 1, data[1] - 1
    matrix[x][y] = True
    fire(x - 1, y)
    fire(x - 2, y)
    fire(x + 1, y)
    fire(x + 2, y)
    fire(x, y - 1)
    fire(x, y - 2)
    fire(x, y + 1)
    fire(x, y + 2)
    fire(x - 1, y - 1)
    fire(x - 1, y + 1)
    fire(x + 1, y - 1)
    fire(x + 1, y + 1)

for i in range(k):
    data = list(map(int, input().split()))
    x, y = data[0] - 1, data[1] - 1
    for j in range(x - 2, x + 3):
        for l in range(y - 2, y + 3):
            if j >= 0 and j < n and l >= 0 and l < n:
                matrix[j][l] = True

ans = 0
for i in range(n):
    for j in range(n):
        if not matrix[i][j]:
            ans += 1
print(ans)