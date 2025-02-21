n = int(input())
time = [False for _ in range(1000)]
cow = [[0 for _ in range(2)] for _ in range(n)] # 先列后行 别忘了内层的[]
ans = [0 for _ in range(n)]

# 只要不需要多次访问 就直接用map 不用再转list
# 多重赋值语句，它将 map(int, input().split()) 迭代器中的元素依次赋值给 cow[i][0] 和 cow[i][1]
for i in range(n):
    cow[i][0], cow[i][1] = map(int, input().split())

for i in range(n):
    time = [False for _ in range(1000)]
    for j in range(n):
        if i == j:
            continue
        for k in range(cow[j][0], cow[j][1]):
            if not time[k]:
                time[k] = True
                ans[i] += 1
print(max(ans))
