from Selection import wheel
from Propulation import create_population
import random


def crossing(x, y):
    # 单切点交叉
    x = int(x * 10000)
    y = int(y * 10000)
    P = 0.9
    p = random.random()
    if p <= P:
        x = '{:019b}'.format(x)
        y = '{:019b}'.format(y)
        slc = random.choice(range(19))
        # 切割点
        bound = random.choice(range(0, 5))
        # 切割区间
        x = list(x)
        # string 拆成列表
        if bound <= 0 or slc+bound > 19:
            x[slc] = y[slc]
            # 点切割
        else:
            for i in range(slc, slc+bound):
                x[i] = y[i]
            # 片切割
        x = ''.join(x)
        return int(x, 2) / 10000
    return x / 10000


def variation(x):
    # 变异
    x = int(x * 10000)
    P = 0.02
    p = random.random()
    if p <= P:
        x = '{:019b}'.format(x)
        slc = random.choice(range(19))
        x = list(x)
        x[slc] = '0' if x[slc] == '1' else '1'
        x = ''.join(x)
        return int(x, 2) / 10000
    return x / 10000


if __name__ == '__main__':
    x = 21.2356
    y = 10.3668
    print(variation(x))

