from Propulation import create_population
from Selection import proportional_selection,wheel,add_pop
from GeneticOperator import crossing,variation
from problem import func
from config import *
import random
import numpy as np


def find_new_individual(population, num):
    # 如果杂交过程中出现重复个体， 替换掉, 概率pp
    pp = random.random()
    if num/NG < pp:
        diff_population = list(set(population))
        diff = len(population) - len(diff_population)
        new_population = create_population()
        while diff:
            new_individual = new_population[random.randrange(len(new_population))]
            if new_individual not in diff_population:
                diff_population.append(new_individual)
                diff -= 1
    return population


def out_of_bound(population):
    # 越界的舍去， 引入新个体
    for individual in population:
        INDEX = population.index(individual)
        if bound_x[0] <= individual <= bound_x[1]:
            pass
        else:
            while True:
                new_population = create_population()
                new_individual = new_population[random.randrange(len(new_population))]
                if new_individual not in population:
                    population[INDEX] = new_individual
                    # 新个体不在种群，引入
                    break
                else:
                    pass
    return population

def GA(population, num):
    # population = find_new_individual(population, num)
    population = out_of_bound(population)
    pop_ls = proportional_selection(*population)
    pp_ls = add_pop(pop_ls, population)
    individuals_ls = []
    for i in range(len(population)):
        pp = random.random()
        father = wheel(pp, pp_ls, population)
        mother = population[random.randrange(len(population))]
        # 配对的母亲, individual是父亲
        individual_new = variation(crossing(father, mother))
        # 先杂交，再变异，生成新个体
        individuals_ls.append(individual_new)
    return individuals_ls


if __name__ == '__main__':
    population = create_population()
    print(population)
    # 产生初始种群
    NOMG = 0
    # number of max generation, 迭代次数统计
    while True:
        if NOMG >= NG:
            print(population)
            flag = func(population[0])
            optimum = population[0]
            for individual in population[1:]:
                # 求最适值
                Flag = func(individual)
                if Flag > flag:
                    flag = Flag
                    optimum = individual
            print(optimum)
            break
        population = GA(population, NOMG)
        NOMG += 1



