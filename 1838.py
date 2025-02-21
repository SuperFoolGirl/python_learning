# 不知为何洛谷一直RE 但是在本地测试是正确的
# 洛谷写的cpp过的

# 注意输入 数字之间没有空格
s = input()
order = [int(x) for x in s] # 推导式列表

# -1处理后才能用除模将一维化为二维 
# 而且必须用下标来访问 不能用for i in order,这里的i是临时变量
for i in range(len(order)):
    order[i] -= 1

board = [[0 for _ in range(3)] for _ in range(3)]

def checkWin(x, y):
    # 两条直线
    if board[x][0] == board[x][1] == board[x][2]:
        return True
    if board[0][y] == board[1][y] == board[2][y]:
        return True
    # 两条对角线
    if x == y and board[0][0] == board[1][1] == board[2][2]:
        return True
    if x + y == 2 and board[0][2] == board[1][1] == board[2][0]:
        return True
    return False

for i in range(len(order)):
    if i % 2 == 0:
        board[order[i] // 3][order[i] % 3] = 1
        if checkWin(order[i] // 3, order[i] % 3):
            print("xiaoa wins.")
            
    else:
        board[order[i] // 3][order[i] % 3] = 2
        if checkWin(order[i] // 3, order[i] % 3):
            print("uim wins.")
            exit()

print("drew.")