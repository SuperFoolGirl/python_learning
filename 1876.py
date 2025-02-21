n = int(input())
light = [False for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(i, n + 1, i): # 参数三为步长 正好实现了倍数
        light[j] = not light[j] # 直接反转

for i in range(1, n + 1):
    if light[i]:
        print(i, end=' ')