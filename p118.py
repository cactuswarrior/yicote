import sys
sys.stdin = open('p118.txt', 'r')

n, m = map(int, input().split())
# n이 세로 m이 가로
row, col, dir = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))


print(arr)
dx = [-1, 0, 1, 0] # 북동남서
dy = [0, 1, 0, -1]
over = 0
while over == 1:
    for i in range(4):
        if arr[x+dx][y+dy] == 0:
            x = x + dx
            y = y + dy
        else:
            
