import random
from config import *
from problem import func


def select(population, count):
    select_ls = []
    while count:
        ret = random.choice(population)
        if ret not in select_ls:
            select_ls.append(ret)
            count -= 1
    return select_ls


def mutation(x, y, z):
    v = x + F * (y-z)
    return x, v


def selection(x, v):
    if bound_x[0] <= v <= bound_x[1]:
        ret = v if func(v) >= func(x) else x
        return ret
    else:
        return x

