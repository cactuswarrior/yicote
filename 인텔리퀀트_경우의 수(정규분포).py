import random
def get_0_or_1():
    a = str(random.random())[2]
    if int(a)%2:
        return 0
    else:
        return 1

print(get_0_or_1())
print(get_0_or_1())
print(get_0_or_1())
def random_(max):
    res = 0
    arr = list(range(0, max))
    for i in range(0, max):
        res += get_0_or_1()

    # print('ans', ans)
    return res

print([random_(3) for i in range(0, 5)])
print([random_(5) for i in range(0, 5)])
print([random_(100) for i in range(0, 5)])
print([random_(2000) for i in range(0, 5)])
print([random_(40000) for i in range(0, 5)])