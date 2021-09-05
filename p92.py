# 큰 수의 법칙
# 풀이법을 예전에 한번 읽었던 터라 쉽게 풀 수 있을 듯

N, M, K = map(int, input().split())
arr = list(map(int, input().split()))

max = 0
for i in arr:
    if i > max:
        max = i

idx = arr.index(max)
max1 = arr.pop(idx)

max = 0
for i in arr:
    if i > max:
        max = i

idx = arr.index(max)
max2 = arr.pop(idx)

res = 0
cnt = 0
for i in range(M):
    if cnt == 2:
        cnt = 0
        res += max2
    else:
        res += max1
        cnt += 1

print(res)

# 책에선 sort를 썼다
# 3-2 풀이에선 아예 나누기로 큰 수가 들어가는 횟수를 구하고 큰수를 그 횟수만큼 곱하기
# 작은 수도 같은 수만큼 곱해서 구했다

