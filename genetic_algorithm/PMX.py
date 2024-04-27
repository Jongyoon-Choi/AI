"""
부분 사상 교차 (partially mapped crossover, PMX)
"""

import random
from genetic_algorithm.select import select

def pmx_crossover(pop):
  
    father = select(pop)
    mother = select(pop)

    chromosome_size = len(father)
    
    length = random.randint(1, chromosome_size - 1)    #교차 길이
    idx = random.randint(0, chromosome_size - length)  #교차 시작 index

    child1 = [-1] * (chromosome_size)
    child2 = [-1] * (chromosome_size)

    child1[idx : idx + length] = mother.genes[idx : idx + length]
    child2[idx : idx + length] = father.genes[idx : idx + length]

    for i in range(chromosome_size):
        
        if i < idx or i >= idx + length:
            
            gene = father.genes[i]
            
            while gene in child1[idx : idx + length]:
                
                index = mother.genes.index(gene)
                gene = father.genes[index]
                
            child1[i] = gene

            gene = mother.genes[i]
            
            while gene in child2[idx : idx + length]:
                
                index = father.genes.index(gene)
                gene = mother.genes[index]
                
            child2[i] = gene

    return (child1, child2) 
