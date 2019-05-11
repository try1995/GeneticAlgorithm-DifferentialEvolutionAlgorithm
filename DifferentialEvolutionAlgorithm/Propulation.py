import random
from config import bound_x, NP


def create_population():
    population = []
    while len(population) <= NP:
        individual = round(random.uniform(bound_x[0], bound_x[1]), 4)
        if individual not in population:
            population.append(individual)
    return population


if __name__ == '__main__':
    print(create_population())
