import random
def get_0_or_1():
    a = str(random.random())[2]
    if int(a)%2:
        return 0
    else:
        return 1

def random_(max):
    res = 0
    start = 1
    cnt0 = 0
    cnt1 = 0
    arr = list(range(0, max))
    rand_list = [657, 239]

    for _ in range(max):
        a = 0
        a = get_0_or_1()
        if a:
            cnt1 += 1
            start *= rand_list[0]
        else:
            cnt0 += 1
            start %= rand_list[1]

    start = str(start)
    l = len(str(max))
    if int(start[0:max]) > max:
        res = int(start[0:l])
        if res > max:
            res %= max
    else:
        res = arr[int(start[0:l])]

    # print(res)
    return res

print([random_(3) for i in range(0, 10)])
print([random_(5) for i in range(0, 10)])
print([random_(100) for i in range(0, 10)])
print([random_(2000) for i in range(0, 10)])
print([random_(40000) for i in range(0, 10)])