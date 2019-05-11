from Propulation import create_population
from problem import func
from config import NP
import numpy as np
from collections import OrderedDict
import bisect


def proportional_selection(*args):
    fun_args = list(map(func, args))
    selection_ls = np.array(fun_args)
    SUM = np.sum(selection_ls)
    return np.array(fun_args / SUM).tolist()


def add_pop(pop_ls, individuals):
    pp_ls = []
    # 累积和概率
    dict_pop = OrderedDict()
    # 有序的累加和字典， key为个体， value为累加的概率， 打印输出观察用
    for item in range(len(individuals)):
        # 初始累加概率
        pp = 0
        for i in range(item + 1):
            pp += pop_ls[i]
        pp_ls.append(pp)
    return pp_ls


def wheel(pop, pp_ls, individuals):
    # 轮旋法
    index = bisect.bisect_left(pp_ls, pop)
    return individuals[index]


if __name__ == '__main__':
    population = create_population()
    pop_ls, individuals = proportional_selection(*population)
    print(pop_ls, individuals)
    pp_ls = add_pop(pop_ls, individuals)
    ret = wheel(0.3, pp_ls, individuals)
    print(ret)
