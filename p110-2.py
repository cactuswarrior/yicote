N = int(input())
route = list(input().split())

i, j = 1, 1

for k in route:
    if k == 'R' and j!=N:
        j += 1
    if k == 'L' and j >1:
        j -= 1
    if k == 'U' and i >1:
        i -= 1
    if k == 'D' and i !=N:
        i += 1
print(i, j)
