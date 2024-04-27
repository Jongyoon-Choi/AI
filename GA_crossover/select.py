"""
crossover에 사용되는 select 연산
7.5에 MAX_FITNESS 값 넣어주시면 됩니다.
"""
import random

def select(pop):
    max_value  = sum([7.5 - c.cal_fitness() + 0.001 for c in pop]) # 우리는 적합도가 낮아질수록 유리해지기 때문에 해당 방식을 사용하였다.
    pick    = random.uniform(0, max_value)
    current = 0
    
    for c in pop:
        current += (7.5 - c.cal_fitness() + 0.001)
        if current > pick:
            return c