"""
균등 순서 기반 교차(uniform order-based crossover)
"""

import random
from genetic_algorithm.select import select

def uniform_order_based_crossover(pop):
    
    father = select(pop)
    mother = select(pop)

    chromosome_size = len(father)
    
    crossover_points = random.sample(range(chromosome_size), chromosome_size//20)
    
    child1 = [father.genes[i] if i in crossover_points else -1 for i in range(chromosome_size)]
    child2 = [mother.genes[i] if i in crossover_points else -1 for i in range(chromosome_size)]
    
    # ?
    idx1 = 0
    idx2 = 0
    
    for i in range(chromosome_size):
        
        if child1[i] == -1:
            while mother.genes[idx2] in child1:
                idx2 += 1
            child1[i] = mother.genes[idx2]
            idx2 += 1
            
        if child2[i] == -1:
            while father.genes[idx1] in child2:
                idx1 += 1
            child2[i] = father.genes[idx1]
            idx1 += 1
    
    return (child1, child2)