input_data = input().split()
n = int(input_data[0])
m = int(input_data[1])
num_of_square = 0
num_of_rectangle = 0

for i in range(n):
    for j in range(m):
        for k in range(i, n):
            for l in range(j, m):
                if k - i == l - j:
                    num_of_square += 1
                else:
                    num_of_rectangle += 1
print(num_of_square, num_of_rectangle) # 默认以空格分隔
        