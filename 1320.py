code = []
# 使用try-except来处理未知输入的情况
while True:
    try:
        code.append(input())
    except:
        break

print(len(code), end = ' ')

s = ''.join(code) # '' 是分隔符，表示在连接 code 列表中的元素时，元素之间不插入任何字符

count = 1
if s[0] != '0':
    print(0, end = ' ')
for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        count += 1
    else:
        print(count, end = ' ')
        count = 1
# 处理最后一个字符。如果count不为1，说明最后一个字符和倒数第二个相同
if count != 1: 
    print(count)