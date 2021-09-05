N = 1260
cnt = 0
while N > 500:
    N -= 500
    cnt += 1

while N > 100:
    N-= 100
    cnt+= 1

while N > 50:
    N -= 50
    cnt += 1

while N >= 10:
    N-= 10
    cnt+= 1

print(cnt)

# 숫자가 커질수록 연산이 많아진다
# 책의 풀이법에 비해 너무 연산량 많다
