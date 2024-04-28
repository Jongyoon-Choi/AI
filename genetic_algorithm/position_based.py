"""
위치 기반 교차(positon-based crossover)
"""

import random
from genetic_algorithm.select import select

def positon_based_crossover(pop):
    father = select(pop)
    mother = select(pop)

    chromosome_size = len(father)
    
    idx = sorted(random.sample(range(0, chromosome_size), chromosome_size//20))
    
    child1 = [mother.genes[i] if i in idx else -1 for i in range(chromosome_size)]
    child2 = [father.genes[i] if i in idx else -1 for i in range(chromosome_size)]

    
    missing_child1 = list(filter(lambda x: not x in child1,father.genes)) # child1에서 없는 값들을 선택한다.
    missing_child2 = list(filter(lambda x: not x in child2,mother.genes))
        
    # 나머지 유전자 추가
    for i in range(chromosome_size):
        if child1[i] == -1:
            child1[i] = missing_child1.pop(0)
        if child2[i] == -1:
            child2[i] = missing_child2.pop(0)
            
    return (child1, child2)