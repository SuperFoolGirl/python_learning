n = int(input())

ans = 0
cnt = 0
for i in range(n):
    list = input().split()
    cnt = cnt + int(list[0]) + int(list[1]) - 8
    ans += cnt
print(ans)