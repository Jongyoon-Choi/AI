"""
염색체 class (Chromosome)
"""

import random
from utils import load_csv
from chunk_sort import chunk_sort_function
from search_methods.A_star import A_star

class Chromosome:
    # dist_table 슬라이싱
    dist_table = load_csv('distance.csv')[0:998] # 행 슬라이싱
    dist_table = [row[0:998] for row in dist_table] # 열 슬라이싱

    def __init__(self, g = [], num_chunk = -1, size = 998, MAX_VAL = 420):
        self.genes = g
        self.fitness = 0
        self.max_val = MAX_VAL

        if self.genes.__len__()==0:	
            if num_chunk == -1:
                # 랜덤 초기화
                temp_list = list(range(1, size))
                random.shuffle(temp_list)
                self.genes = temp_list.copy()

            else:
                # chunk_sort_function를 사용한 A*
                temp_list=[]
                sorted_cities = chunk_sort_function(num_chunk)
                subtree_list = []
                subtree_size = 10

                for i in range(0, size, subtree_size):
                    subtree =  sorted_cities[i:i+subtree_size if i+subtree_size<size else size]
                    subtree_list.append(subtree)

                # 각 subtree 탐색
                for subtree in subtree_list:
                    temp_list += A_star(self.dist_table, subtree)
                self.genes = temp_list[1:].copy() # 시작점 생략

            
        
    def cal_fitness(self):		# 적합도를 계산
        self.fitness = 0
        value = 0
        
        # 실제 cost를 적합도로 사용
        prev_node = 0
        for i in range(len(self)):
            node = self.genes[i]
            value += float(self.dist_table[prev_node][node]) # 각 거리의 연계
            prev_node = node
        value += float(self.dist_table[self.genes[-1]][0]) # 맨 마지막과 맨 앞을 연계

        # 목표 cost가 max_val 이상이면 max_val
        self.fitness = value if value < self.max_val else self.max_val
        return self.fitness
    
    def __len__(self):
        return len(self.genes)