import sys
sys.stdin = open("../p118.txt", "r")


# N이 세로, M이 가로
N, M = map(int, input().split())
# 다녀온 로그 찍을 배열 만들기
arr = [[0]*M for _ in range(N)]
print(arr)
x, y, dir = map(int, input().split())
print(x, y, dir)
site = []
for _ in range(N):
    site.append(list(map(int, input().split())))

# 왼쪽으로 도는 동작 수행할 함수
def turn_left():
    global dir
    dir -= 1
    if dir == -1:
        dir = 3
# 북동서남
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
print(site)
cnt = 0
way = 0
while True:
    turn_left()
    nx = x + dx[dir]
    ny = y + dy[dir]
    # 방문한 적이 없었다면

    ## arr 뿐만 아니라 site도 0이어야함(가본적도 없어야하고 지도에서 갈 수 있는 곳인지 확인해야하는데 놓침)
    if arr[nx][ny] == 0 and site[nx][ny] == 0:

        arr[nx][ny] = 1
        x = nx
        y = ny
        print('site', x, y)
        way += 1
        # 가본 적이 없어서 움직이면 방향탐색 초기화
        cnt = 0
        continue
    else:
        cnt += 1

    # 네 방향 다 방문한적이 있다면
    if cnt == 4:
        nx = x - dx[dir]
        ny = y - dy[dir]
        # 뒤로 갈 수 있는 경우도 생각해야
        if site[x][y] == 0:
            x = nx
            y = ny
        else:
            break
#       # 네 방향 다 방문한 적이 있다면 회전 횟수 초기화 해줘야함
        cnt = 0
print(way)

# -----------------------
# 초기화 시켜주는 부분을 놓치는 경우가 많았고, 방향 탐색의 경우 nx, ny로 따로 변수할당해서 검색 후 이동할 때 비로소 x,y 에 할당할 것
# 다녀온 적이 있는지와 지도 상에서 갈 수 있는 곳인지 확인하기