c0 = int(input('Enter a non- negative, non-zero integer: '))
step = 0
while c0 != 1:
    if c0 % 2 == 0:
        c0 //= 2
        if c0 != 1:
            step += 1
            print(c0)
            continue
        elif c0 == 1:
            step += 1
            print(c0)
            break
    elif c0 % 2 == 1:
        c0 = c0 * 3 + 1
        if c0 != 1:
            step += 1
            print(c0)
            continue

print('Total Steps: ', step)