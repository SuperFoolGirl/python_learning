# 有bug
s, x = map(float, input().split()) # 要用float读
v = 7.0
dist = 0
while True:
    dist += v
    v *= 0.98

    if dist < s - x: # 没到探测范围
        continue
    elif dist > s + x: # 一次直接越过范围
        print('n')
        break
    else: # 到达探测范围
        # 这里要特判一个情况：刚进来就进入范围了，只有第一秒的机会
        if dist == 7.0:
            print('y')
            break

        dist += v
        if dist > s + x:
            print('n')
        else:
            print('y')
        break