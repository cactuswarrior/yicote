N, M = map(int, input().split())
cnt = 0
while N > 1:
    if N%M == 0:
        N /= M
        cnt += 1
    else:
        N -= 1
        cnt += 1
print(cnt)

#연산량이 많다,,
#배수가 될때까지 while로 1을 빼주고 배수가 되면 나눠준다음 몫이 1이 될 때까지 1을 빼주면 된다
