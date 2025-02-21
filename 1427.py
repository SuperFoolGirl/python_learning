input = input().split()
cnt = 0
for i in range(len(input)):
    if input[i] == '0':
        break
    cnt += 1
for i in range(cnt - 1, -1, -1): # 倒序遍历
    print(input[i], end=' ')