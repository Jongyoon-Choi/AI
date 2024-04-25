import random
import matplotlib.pyplot as plt
import numpy as np
from utils import load_csv, save_csv

# 랜덤 시드 설정
random.seed(42)

POPULATION_SIZE = 40	# 개체 집단의 크기
# 돌연변이 확률을 낮출수록 더 성능이 좋아진다 (노드가 많을수록 돌연변이로 좋은 해가 탄생하기 힘들기 때문? or local optimal에 도달하지도 못해서??)
MUTATION_RATE = 0.2	# 돌연 변이 확률
SIZE = 1000			# 하나의 염색체에서 유전자 개수		
TARGET_VAL = 30

# dist_table 슬라이싱
dist_table = load_csv('distance.csv')[0:SIZE] # 행 슬라이싱
dist_table = [row[0:SIZE] for row in dist_table] # 열 슬라이싱

greedy_solution = load_csv('solutions\greedy_1000.csv')

class Chromosome:
    def __init__(self, g = []):
        self.genes = g
        self.fitness = 0		
        if self.genes.__len__()==0:	
            # 랜덤 초기화
            temp_list = list(range(1, SIZE))
            random.shuffle(temp_list)
            self.genes = temp_list.copy()
            # # greedy_solution으로 초기화
            # temp_list = [int(element) for row in greedy_solution for element in row]
            # self.genes = temp_list[1:].copy() # 시작점 생략
        
    def cal_fitness(self):		# 적합도를 계산
        global dist_table
        self.fitness = 0
        value = 0
        
        # 실제 cost를 적합도로 사용
        prev_node = 0
        for i in range(SIZE - 1):
            node = self.genes[i]
            value += float(dist_table[prev_node][node]) # 각 거리의 연계
            prev_node = node
        value += float(dist_table[self.genes[-1]][0]) # 맨 마지막과 맨 앞을 연계

        # 목표 cost의 제곱 이상이면 TARGET_VAL * TARGET_VAL
        self.fitness = value if value < TARGET_VAL ** 2 else TARGET_VAL ** 2
        return self.fitness

    def __str__(self):
        return self.genes.__str__()
    
    def to_list(self):
        return self.genes

def print_p(pop):
    i = 0
    for x in pop:
        # print(f"염색체 #{i} = {x} 적합도={x.fitness:.2f}")
        print(f"염색체 #{i} 적합도={x.fitness:.2f}")
        i += 1
    print("")

# 선택 연산
def select(pop):
    max_value  = sum([TARGET_VAL ** 2 - c.cal_fitness() + 0.001 for c in population]) #우리는 적합도가 낮아질수록 유리해지기 때문에 해당 방식을 사용하였다.
    pick    = random.uniform(0, max_value)
    current = 0
    
    for c in pop:
        current += (TARGET_VAL ** 2 - c.cal_fitness() + 0.001)
        if current > pick:
            return c

# 교차 연산 (ordered crossover?)
# def crossover(pop):
#     father = select(pop)
#     mother = select(pop)
#     length = random.randint(1, SIZE - 2)    #교차 길이
#     idx = random.randint(0, SIZE - length -1)  #교차 시작 index

#     t_child1 = mother.genes[idx:idx + length].copy() # idx에서 length 만큼 추가적으로 계산한다.
#     t_child2 = father.genes[idx:idx + length].copy()

#     child1 = list(filter(lambda x: not x in t_child1,father.genes)) #t_child에서 없는 수 만큼을 선택한다.
#     child2 = list(filter(lambda x: not x in t_child2,mother.genes))
    
#     child1 = child1[:idx] + t_child1 + child1[idx:]
#     child2 = child2[:idx] + t_child2 + child2[idx:]

#     return (child1, child2)

"""
def crossover(pop):
  
    parent1 = select(pop)
    parent2 = select(pop)
   
    idx1 = random.randint(0, SIZE - 2)
    idx2 = random.randint(0, SIZE - 2)
    
    idx1,idx2 = sorted((idx1, idx2))
    
    if idx2 == idx1:
        idx2 += 1   

    child1 = [-1] * (SIZE - 1)
    child2 = [-1] * (SIZE - 1)
    
    for i in range(idx1, idx2):
        
        child1[i] = parent2.genes[i]
        child2[i] = parent1.genes[i]

    for i in range(SIZE - 1):
        
        if i < idx1 or i >= idx2:
            
            gene = parent1.genes[i]
            
            while gene in child1[idx1:idx2]:
                
                index = parent2.genes.index(gene)
                gene = parent1.genes[index]
                
            child1[i] = gene

            gene = parent2.genes[i]
            
            while gene in child2[idx1:idx2]:
                
                index = parent1.genes.index(gene)
                gene = parent2.genes[index]
                
            child2[i] = gene

    return child1, child2
"""
# 사이클 교차 연산
def crossover(pop):

    father = select(pop)
    mother = select(pop)
    n = SIZE-1
    cycle_start1 = 0
    cycle_start2 = 0
    child1 = [-1] * n
    child2 = [-1] * n

    while True:
        cycle_end1 = cycle_start1
        cycle_end2 = cycle_start2
        while child1[cycle_end1] == -1:
            child1[cycle_end1] = father.genes[cycle_end1]
            cycle_end1 = father.genes.index(mother.genes[cycle_end1])
        while child2[cycle_end2] == -1:
            child2[cycle_end2] =  mother.genes[cycle_end2]
            cycle_end2 = mother.genes.index(father.genes[cycle_end2])
        
        cycle_start1 = (cycle_end1 + 1) % n
        cycle_start2 = (cycle_end2 + 1) % n
        if -1 not in child1 and -1 not in child2:
            break
    return (child1, child2)
    
# 돌연변이 연산
def mutate(c):
    if random.random() < MUTATION_RATE:
        # x, y = random.sample(list(range(0,SIZE-1)),2)
        # c.genes[y], c.genes[x] = c.genes[x], c.genes[y]

        # 겹치지 않는 5개의 정수를 담을 리스트
        mutate_idx = []

        # (SIZE // 5) 개의 겹치지 않는 리스트 생성
        while len(mutate_idx) < SIZE // 5:
            # 0부터 SIZE - 1 사이의 임의의 정수를 생성
            idx = random.randint(0, SIZE - 2)
            # 생성된 정수가 리스트에 없다면 추가
            if idx not in mutate_idx:
                mutate_idx.append(idx)
        # mutate_idx에 해당하는 원소들을 한 칸씩 앞으로 이동
        temp = c.genes[mutate_idx[0]]
        for i in range(len(mutate_idx)-1):
            c.genes[mutate_idx[i]]=c.genes[mutate_idx[i+1]]
        c.genes[mutate_idx[-1]] = temp

# 메인 프로그램
population = []
i=0
fitness_list = []

# 초기 염색체를 생성하여 객체 집단에 추가한다. 
for _ in range(POPULATION_SIZE):
    population.append(Chromosome())

count=0
population.sort(key=lambda x: x.cal_fitness())
print("세대 번호=", count)
print_p(population)
count=1

max_fitness = 0

while population[0].fitness > TARGET_VAL:
    if population[0].fitness < max_fitness:
        MUTATION_RATE = MUTATION_RATE * 0.9
        max_fitness = population[0].fitness
    new_pop = []

    # 선택과 교차 연산
    for _ in range(POPULATION_SIZE//2):
        c1, c2 = crossover(population)
        new_pop.append(Chromosome(c1))
        new_pop.append(Chromosome(c2))

    # 자식 세대가 부모 세대를 대체한다. 
    # 깊은 복사를 수행한다. 
    population = new_pop.copy()
    
    # 돌연변이 연산
    for c in population: mutate(c)

    # 출력을 위한 정렬
    population.sort(key=lambda x: x.cal_fitness())
    fitness_list.append(population[0].fitness)
    print("세대 번호=", count)
    print_p(population)
    count += 1
    if count > 300 : break

# save as csv
sol=[0]+population[0].to_list()
save_csv(sol, f'solutions/GA_{SIZE}.csv')


sol.append(int(0))

total_cost = 0

# 탐색 비용 계산
for idx in range(len(sol)-1):

    dist = float(dist_table[sol[idx]][sol[idx+1]])
    total_cost += dist

# 출력
print(f'final cost: {total_cost:.2f}')


#시각화
x, y = range(len(fitness_list)),fitness_list
fit_line = np.polyfit(x,y,1)
x_minmax = np.array([min(x), max(x)])
fit_y = x_minmax * fit_line[0] + fit_line[1]

plt.plot(fitness_list,label='fitness')
plt.plot(x_minmax, fit_y, color = 'red',label='regression')
plt.xlabel('generation number')
plt.ylabel('fitness')
plt.legend()
plt.show()
