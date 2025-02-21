# 前缀和
data = list(map(int, input().split()))
n = data[0]
m = data[1]
value = [0 for _ in range(n)]
sum = [0 for _ in range(n)]
ans = [0 for _ in range(n - m + 1)]

# 特判
if n == 0:
    print(0)
    exit()

for i in range(n):
    value[i] = int(input())

sum[0] = value[0]
for i in range(1, n):
    sum[i] = sum[i - 1] + value[i]

range_i = range(m, n)
range_j = range(n - m)

ans[0] = sum[m - 1]
for i, j in zip(range_i, range_j):
    ans[j + 1] = sum[i] - sum[j]
print(min(ans))