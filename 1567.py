# 寻找最大递增子序列
n = int(input())
temp = list(map(int, input().split())) # 掌握将输入的以空格分隔元素的字符串直接转换为列表的方法
dp = [0 for _ in range(n)]

dp[0] = 1

for i in range(1, n): # 遍历天数
    if temp[i] > temp[i - 1]:
        dp[i] = dp[i - 1] + 1
    else:
        dp[i] = 1

print(max(dp))