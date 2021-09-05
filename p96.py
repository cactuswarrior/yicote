N, M = map(int, input().split())

arr = []
for a in range(N):
    arr.append(list(map(int, input().split())))

min = 10000
min_list = []
for i in range(N):
    for j in range(M):
       if arr[i][j] < min:
        min = arr[i][j]
    min_list.append(min)
    min = 10000  #min 초기화를 안해줬다

max = 0
for i in min_list:
    if i > max:
        max = i

print(max)