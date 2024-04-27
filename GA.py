import random
import matplotlib.pyplot as plt
import numpy as np
from utils import load_csv, save_csv
from argparse import ArgumentParser
from genetic_algorithm.chromosome import Chromosome
from genetic_algorithm.order import order_crossover
from genetic_algorithm.position_based import positon_based_crossover
from genetic_algorithm.uniform_order_based import uniform_order_based_crossover
from genetic_algorithm.PMX import pmx_crossover
from genetic_algorithm.cycle import cycle_crossover
from genetic_algorithm.edge_recom import edge_recom_crossover
from genetic_algorithm.mutation import mutate

def print_p(pop):
    i = 0
    for x in pop:
        print(f"염색체 #{i} = {x.genes} 적합도={x.fitness:.2f}")
        # print(f"염색체 #{i} 적합도={x.fitness:.2f}")
        i += 1
    print("")

def main(): # 메인 프로그램
    parser = ArgumentParser()

    parser.add_argument("--POPULATION_SIZE", type=int, default=40, help="Population size")
    parser.add_argument("--MUTATION_RATE", type=float, default=0.05, help="Mutation rate")
    parser.add_argument("--SIZE", type=int, default=20, help="Number of genes in a chromosome")
    parser.add_argument("--TARGET_VAL", type=int, default=4, help="Target fitness value")
    parser.add_argument("--MAX_VAL", type=float, default=7.5, help="Maximum fitness value")
    parser.add_argument("--max_iter", type=int, default=2000, help="Maximum number of iterations")
    parser.add_argument("--crossover_name", type=str, default="order_crossover", help="Name of crossover function")
    parser.add_argument("--output_path", type=str, default="GA_result/test", help="output path")

    args = parser.parse_args()

    # 랜덤 시드 설정
    random.seed(42)

    POPULATION_SIZE = args.POPULATION_SIZE	# 개체 집단의 크기
    MUTATION_RATE = args.MUTATION_RATE	# 돌연 변이 확률
    SIZE = args.SIZE			# 하나의 염색체에서 유전자 개수		
    TARGET_VAL = args.TARGET_VAL
    MAX_VAL = args.MAX_VAL
    
    crossover_functions = {
        'order_crossover': order_crossover,
        'positon_based_crossover': positon_based_crossover,
        'uniform_order_based_crossover': uniform_order_based_crossover,
        'pmx_crossover': pmx_crossover,
        'cycle_crossover': cycle_crossover,
        'edge_recom_crossover': edge_recom_crossover
    }
    
    population = []
    fitness_list = []

    # 초기 염색체를 생성하여 객체 집단에 추가한다. 
    for _ in range(POPULATION_SIZE):
        population.append(Chromosome(size=SIZE))

    count=0
    population.sort(key=lambda x: x.cal_fitness(MAX_VAL))
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
            c1, c2 = crossover_functions[args.crossover_name](population)
            new_pop.append(Chromosome(c1))
            new_pop.append(Chromosome(c2))

        # 자식 세대가 부모 세대를 대체한다. 
        population = new_pop.copy()
        
        # 돌연변이 연산
        for c in population: mutate(c, MUTATION_RATE)

        # 출력을 위한 정렬
        population.sort(key=lambda x: x.cal_fitness(MAX_VAL))
        fitness_list.append(population[0].fitness)
        print("세대 번호=", count)
        print_p(population)
        count += 1
        if count > args.max_iter : break

    # csv 파일로 저장 (파일명 변경 예정)
    sol=[0]+population[0].genes
    save_csv(sol, f'solutions/GA_{SIZE}.csv')

    # cost 출력
    print(f'final cost: {population[0].fitness:.2f}')


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
    # plt.show()

    # 이미지 파일로 저장
    plt.savefig(f'{args.output_path}.png')

if __name__ == "__main__":
    main()