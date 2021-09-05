import random
def zero_one():
    a = str(random.random())[2]
    if int(a)%2:
        return 0
    else:
        return 1

print(zero_one())

def random_(max):
    res = 0
    arr = list(range(0, max))
    for i in range(0, max):
        res += zero_one()

    # print('ans', ans)
    return res

print(random_(7))
print(random_(8))
print(random_(10))
print(random_(200))