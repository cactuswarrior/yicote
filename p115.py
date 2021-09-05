where = input()
col = where[0]
row = int(where[1])
# print(col, row)
col_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
row_list = [1, 2, 3, 4, 5, 6, 7, 8]

cnt = 0
for i in range(-2, 3):
    if col_list.index(col)+i <= 0 or col_list.index(col)+i > 7 or i == 0:
        continue
    if i < 0:
        i = -i
    if i == 1:
        row_p = row + 2
        row_m = row - 2
        if row_p in row_list:
            cnt += 1
        if row_m in row_list:
            cnt += 1
    elif i == 2:
        row_p = row + 1
        row_m = row - 1
        if row_p in row_list:
            cnt += 1
        if row_m in row_list:
            cnt += 1
    else:
        print(i)
print(cnt)

#책에선 ord를 사용해서 알파벳 좌표도 숫자로 바꾸고
# 움직일 수 있는 경우의 수 8가지를 리스트로 만들어 반복문으로 x, y 값에 넣어보면서 가능하면 카운트하는 형식으로 풀었다