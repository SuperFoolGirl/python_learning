input = input().split()
x = int(input[0])
n = int(input[1])

sum = 0
for i in range(n):
    if x != 6 and x != 7:
        sum += 250
    x += 1
    if x == 8:
        x = 1
print(sum)