"""
crossover에 사용되는 select 연산
"""
import random

def select(pop):
    max_value  = sum([c.max_val - c.cal_fitness() + 0.001 for c in pop]) # 우리는 적합도가 낮아질수록 유리해지기 때문에 해당 방식을 사용하였다.
    pick    = random.uniform(0, max_value)
    current = 0
    
    for c in pop:
        current += (c.max_val - c.cal_fitness() + 0.001)
        if current > pick:
            return c