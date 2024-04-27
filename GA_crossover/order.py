"""
순서 교차 (order crossover)
"""

import random
from GA_crossover.select import select

def order_crossover(pop):
    father = select(pop)
    mother = select(pop)
    
    chromosome_size = len(father)

    length = random.randint(1, chromosome_size - 1)    # 교차 길이
    idx = random.randint(0, chromosome_size - length)  #교차 시작 index

    t_child1 = mother.genes[idx:idx + length].copy() # idx에서 length 만큼 추가적으로 계산한다.
    t_child2 = father.genes[idx:idx + length].copy()

    child1 = list(filter(lambda x: not x in t_child1,father.genes)) # t_child에서 없는 수 만큼을 선택한다.
    child2 = list(filter(lambda x: not x in t_child2,mother.genes))
    
    child1 = child1[:idx] + t_child1 + child1[idx:]
    child2 = child2[:idx] + t_child2 + child2[idx:]

    return (child1, child2)