# 读取输入的一行数据
input_data = input().split()
# 获取 N 的值，并转换为整数
n = int(input_data[0]) # input默认返回字符串 要强转
# 从第二个元素开始获取压缩码列表
compressed_codes = [int(num) for num in input_data[1:]] # 列表推导式 [表达式 for 变量 in 可迭代对象]，根据给定的表达式和循环条件生成一个新的列表

# 当前要打印的字符（0 或 1）
current_char = 0
# 记录当前行已经打印的字符数量
current_row_count = 0

# 遍历压缩码列表
for code in compressed_codes:
    for _ in range(code):
        print(current_char, end = '') # end = '' 表示不换行，接了个空字符串。默认是换行
        current_row_count += 1
        # 如果当前行已经打印了 N 个字符，换行并重置计数器
        if current_row_count == n:
            print()
            current_row_count = 0
    # 切换要打印的字符（0 变 1，1 变 0）
    # 这个写法很巧妙
    current_char = 1 - current_char