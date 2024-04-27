import random
import matplotlib.pyplot as plt
import numpy as np
from utils import load_csv, save_csv
from GA_crossover.order import order_crossover
from GA_crossover.position_based import positon_based_crossover
from GA_crossover.uniform_order_based import uniform_order_based_crossover
from GA_crossover.PMX import pmx_crossover
from GA_crossover.cycle import cycle_crossover
from GA_crossover.edge_recom import edge_recom_crossover

# 랜덤 시드 설정
random.seed(42)

POPULATION_SIZE = 40	# 개체 집단의 크기
MUTATION_RATE = 0.2	# 돌연 변이 확률
SIZE = 20			# 하나의 염색체에서 유전자 개수		
TARGET_VAL = 4
MAX_FITNESS = 7.5

# dist_table 슬라이싱
dist_table = load_csv('distance.csv')[0:SIZE] # 행 슬라이싱
dist_table = [row[0:SIZE] for row in dist_table] # 열 슬라이싱

class Chromosome:
    def __init__(self, g = []):
        self.genes = g
        self.fitness = 0		
        if self.genes.__len__()==0:	
            # 랜덤 초기화
            temp_list = list(range(1, SIZE))
            random.shuffle(temp_list)
            self.genes = temp_list.copy()
        
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

        # 목표 cost가 MAX_FITNESS 이상이면 MAX_FITNESS
        self.fitness = value if value < MAX_FITNESS else MAX_FITNESS
        return self.fitness

    def __str__(self):
        return self.genes.__str__()
    
    def __len__(self):
        return len(self.genes)

def print_p(pop):
    i = 0
    for x in pop:
        print(f"염색체 #{i} = {x} 적합도={x.fitness:.2f}")
        # print(f"염색체 #{i} 적합도={x.fitness:.2f}")
        i += 1
    print("")

# 돌연변이 연산
def mutate(c):
    if random.random() < MUTATION_RATE:
        # (SIZE // 5) 개의 겹치지 않는 리스트 생성
        mutate_idx = random.sample(range(0, SIZE - 2), SIZE // 5)
        
        # mutate_idx에 해당하는 원소들을 한 칸씩 앞으로 이동
        temp = c.genes[mutate_idx[0]]
        for i in range(len(mutate_idx)-1):
            c.genes[mutate_idx[i]]=c.genes[mutate_idx[i+1]]
        c.genes[mutate_idx[-1]] = temp

# 메인 프로그램
population = []
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
        c1, c2 = pmx_crossover(population)
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
    if count > 2000 : break

# save as csv
sol=[0]+population[0].genes
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
plt.text(0.5, 0.9, f'Regression: y = {fit_line[0]:.5f}x + {fit_line[1]:.2f}', 
         horizontalalignment='center', verticalalignment='center', 
         transform=plt.gca().transAxes, fontsize=10, color='red')
plt.xlabel('generation number')
plt.ylabel('fitness')
plt.legend()
plt.show()

# 이미지 파일로 저장
# plt.savefig('fitness_regression_plot.png')