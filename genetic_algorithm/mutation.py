"""
돌연변이 연산
"""

import random

def mutate(c, MUTATION_RATE):
    chromosome_size = len(c)
    if random.random() < MUTATION_RATE:
        # (chromosome_size // 5) 개의 겹치지 않는 리스트 생성
        mutate_idx = random.sample(range(0, chromosome_size - 1), chromosome_size // 5)
        
        # mutate_idx에 해당하는 원소들을 한 칸씩 앞으로 이동
        temp = c.genes[mutate_idx[0]]
        for i in range(len(mutate_idx)-1):
            c.genes[mutate_idx[i]]=c.genes[mutate_idx[i+1]]
        c.genes[mutate_idx[-1]] = temp
        