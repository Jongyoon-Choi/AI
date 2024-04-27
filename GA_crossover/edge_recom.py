"""
인접 인자 교차 (edge_recombination crossover)
인접인자 기준: 가까운 노드
"""
import random
from GA_crossover.select import select

def edge_recom_crossover(pop):
    father = select(pop)
    mother = select(pop)

    chromosome_size = len(father)
    
    child1 = father.genes.copy()
    child2 = mother.genes.copy()
    
    # 중복없는 인덱스를 생성하여 인접한 유전자 선택
    idx = sorted(random.sample(range(2, chromosome_size - 1), 5))  
    
    for i in idx:
        child1[i], child1[i+1] = child1[i+1], child1[i]
        child1[i-2], child1[i-1] = child1[i-1], child1[i-2]
        
        child2[i], child2[i+1] = child2[i+1], child2[i]
        child2[i-2], child2[i-1] = child2[i-1], child2[i-2]
        
    return (child1, child2)