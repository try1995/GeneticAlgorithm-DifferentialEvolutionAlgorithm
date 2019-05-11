from Operator import *
from Propulation import create_population
from problem import func


def run(population):
    new_individual = []
    for individual in population:
        se_individual = select(population, 2)
        # 选择杂交个体
        mu_individual = mutation(individual, *se_individual)
        # 杂交
        new_individual.append(selection(*mu_individual))
        # 选择
    return new_individual


if __name__ == '__main__':
    population = create_population()
    print(population)
    while NG:
        population = run(population)
        NG -= 1
    flag_i = population[0]
    print(population)
    for i in population[1:]:
        if func(i) > func(flag_i):
            flag_i = i
    print(flag_i)
