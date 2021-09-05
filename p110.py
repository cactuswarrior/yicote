N = int(input())
route = list(input().split())

i, j = 1, 1

for k in route:
    if k == 'R':
        j += 1
        if j > N:
            j -= 1
            continue
    elif k == 'L':
        j -= 1
        if j < 1:
            j += 1
            continue
    elif k == 'U':
        i -= 1
        if i < 1:
            i += 1
            continue
    else:
        i += 1
        if i > N:
            i -= 1
            continue

print(i, j)

# 책에서는 방향을 리스트에 담고
# 각 방향당 좌표를 정해두고, x축은 이런 식으로 [0, 0, -1, 1]
# 해당 방향에 맞는 경우, 그에 맞는 값을 더하도록 해두었다

