"""
염색체 class (Chromosome)
"""

import random
from utils import load_csv

class Chromosome:
    # dist_table 슬라이싱
    dist_table = load_csv('distance.csv')[0:20] # 행 슬라이싱
    dist_table = [row[0:20] for row in dist_table] # 열 슬라이싱

    def __init__(self, g = [],  size = 998):
        self.genes = g
        self.fitness = 0		
        if self.genes.__len__()==0:	
            # 랜덤 초기화
            temp_list = list(range(1, size))
            random.shuffle(temp_list)
            self.genes = temp_list.copy()
        
    def cal_fitness(self, MAX_VAL):		# 적합도를 계산
        self.fitness = 0
        value = 0
        
        # 실제 cost를 적합도로 사용
        prev_node = 0
        for i in range(len(self)):
            node = self.genes[i]
            value += float(self.dist_table[prev_node][node]) # 각 거리의 연계
            prev_node = node
        value += float(self.dist_table[self.genes[-1]][0]) # 맨 마지막과 맨 앞을 연계

        # 목표 cost가 MAX_VAL 이상이면 MAX_VAL
        self.fitness = value if value < MAX_VAL else MAX_VAL
        return self.fitness
    
    def __len__(self):
        return len(self.genes)