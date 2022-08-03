import random


# 1. (0, x) 的 概率 x**2
def pf_random():
    print(min(random.random(), random.random()))


# 2. 1-5概率 得到 1-7概率
def one_seven():
    def one_five():
        return random.randint(1, 5)

    # 1-5概率 得到 0-1概率
    def zero_one():
        a = one_five()
        while a == 3:
            a = one_five()
        return 0 if a <= 2 else 1

    # 0-1概率 得到 0-7概率
    def zero_seven():
        return (zero_one() << 2) + (zero_one() << 1) + zero_one()

    # 0-7概率 得到 1-7概率
    def _one_seven():
        a = zero_seven()
        while a == 0:
            a = zero_seven()
        return a

    return _one_seven()


# 3. 01不等概率 随机到01对等概率
def one_two_fair():
    def one_two_unfair():
        a = random.randint(1, 3)
        if a == 1:
            return 0
        return 1

    a, b = one_two_unfair(), one_two_unfair()
    while a == b:
        a, b = one_two_unfair(), one_two_unfair()
    return a


if __name__ == '__main__':
    print(one_seven())
    print(one_two_fair())
