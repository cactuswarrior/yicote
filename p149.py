# 음료수 얼려먹기
import sys
sys.stdin = open('p149.txt', 'r')
# 세로길이 N ,가로길이 M
N, M = map(int, input().split())

arr = []
for _ in range(N):
    arr.append(list(map(int, input()))) # 다닥다닥 붙어들어오는 숫자인풋은 스플릿없이 그냥 map으로 처리하면 되나봄
print(arr)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
# 스택형성
stack = []
def ice_search(x, y):
    stack.append([x, y])
    if arr[x][y]:
        [nx, xy] = stack.pop()
        ice_search(nx, ny)
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dx[i]
            if (nx >= 0 and nx< M) and (nx >= 0 and nx< N):
                ice_search(nx, ny)
            else:
                continue

for x in range(N):
    for y in range(M):
        ice_search(0, 0)