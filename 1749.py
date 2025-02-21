t = int(input())
for i in range(t):
    data = list(map(int, input().split()))
    n = data[0]
    k = data[1]
    # //为整除符号, /为浮点数除法
    need = k * (k + 1) / 2
    if n < need:
        print("No")
    else:
        print("Yes")