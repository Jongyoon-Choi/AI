import random
import matplotlib.pyplot as plt
import numpy as np
from utils import load_csv, save_csv


POPULATION_SIZE = 16	# 개체 집단의 크기
MUTATION_RATE = 0.2	# 돌연 변이 확률
SIZE = 10			# 하나의 염색체에서 유전자 개수		
dist_table=load_csv('distance.csv')[0:SIZE] # 행 슬라이싱
dist_table=[row[0:SIZE] for row in dist_table] # 열 슬라이싱
TARGET_VAL = 3.38

# 최단 경로 : [0, 9, 4, 3, 8, 2, 7, 1, 6, 5]
# 최단 거리 : 3.38    # 최단 거리 X greedy 값

class Chromosome:
    def __init__(self, g = []):
        self.genes = g
        self.fitness = 0		
        if self.genes.__len__()==0:	
            temp_list = list(range(1, SIZE))
            random.shuffle(temp_list)
            self.genes = temp_list.copy()
        
    def cal_fitness(self):		# 적합도를 계산
        global dist_table
        self.fitness = 0
        value = 0

        prev_node = 0
        for i in range(SIZE - 1):
            node = self.genes[i]
            value += float(dist_table[prev_node][node])
            prev_node = node
        value += float(dist_table[self.genes[-1]][0])

        self.fitness = TARGET_VAL * 2 - value if TARGET_VAL * 2 - value > 0 else 1
        return self.fitness

    def __str__(self):
        return self.genes.__str__()
    
    def to_list(self):
        return self.genes

def print_p(pop):
    i = 0
    for x in pop:
        print("염색체 #", i, "=", x, "적합도=", x.fitness)
        i += 1
    print("")

# 선택 연산
def select(pop):
    max_value  = sum([c.cal_fitness() for c in population])
    pick    = random.uniform(0, max_value)
    current = 0
    
    for c in pop:
        current += c.cal_fitness()
        if current > pick:
            return c

# 교차 연산
def crossover(pop):
    father = select(pop)
    mother = select(pop)
    length = random.randint(1, SIZE - 1)
    idx = random.randint(0, SIZE - length)

    t_child1 = mother.genes[idx:idx + length].copy()
    t_child2 = father.genes[idx:idx + length].copy()

    child1 = list(filter(lambda x: not x in t_child1,father.genes))
    child2 = list(filter(lambda x: not x in t_child2,mother.genes))

    child1 = child1[:idx] + t_child1 + child1[idx:]
    child2 = child2[:idx] + t_child2 + child2[idx:]

    return (child1, child2)
    
# 돌연변이 연산
def mutate(c):
    if random.random() < MUTATION_RATE:
        x, y = random.sample(list(range(0,SIZE-1)),2)
        c.genes[y], c.genes[x] = c.genes[x], c.genes[y]

# 메인 프로그램
population = []
i=0
fitness_list = []

# 초기 염색체를 생성하여 객체 집단에 추가한다. 
while i<POPULATION_SIZE:
    population.append(Chromosome())
    i += 1

count=0
population.sort(key=lambda x: x.cal_fitness(),reverse=True)
print("세대 번호=", count)
print_p(population)
count=1

max_fitness = 0

while population[0].fitness < TARGET_VAL:
    if population[0].fitness > max_fitness:
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
    population.sort(key=lambda x: x.cal_fitness(),reverse=True)
    fitness_list.append(population[0].fitness)
    print("세대 번호=", count)
    print_p(population)
    count += 1
    if count > 1000 : break

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