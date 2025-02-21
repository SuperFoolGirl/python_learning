mod = 47
offset = 1 - ord('A')
comet_value = 1;
group_value = 1;

comet = input()
group = input()

# 遍历字符串
for i in comet: 
    comet_value *= ord(i) + offset

for i in group:
    group_value *= ord(i) + offset

if comet_value % mod == group_value % mod:
    print("GO")
else:
    print("STAY")