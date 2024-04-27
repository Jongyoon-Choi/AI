"""
사이클 교차 (cycle crossover)
"""

import random
from GA_crossover.select import select

def cycle_crossover(pop):

    father = select(pop)
    mother = select(pop)

    chromosome_size = len(father)

    child1=mother.genes.copy()
    child2=father.genes.copy()

    cycle_start = random.randint(0, chromosome_size -1)

    visited = [-1] * chromosome_size

    point=cycle_start

    while visited[point] == -1:
        child1[point] = father.genes[point]
        child2[point] =  mother.genes[point]
        point = mother.genes.index(father.genes[point])

    return (child1, child2)