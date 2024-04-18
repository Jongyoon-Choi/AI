import csv
from utils import distance
from utils import get_pos
from utils import save_csv
from search_methods.greedy import greedy
from search_methods.UCS import UCS
from search_methods.A_star import A_star

cities = []
sol = []

with open('TSP.csv', mode='r', newline='') as tsp:

    reader = csv.reader(tsp)
    for row in reader:
        cities.append(row)

# 방문할 도시 수
num_cities=1000

# 탐색 방법
search_method='greedy'

# Search
if search_method=='UCS':
    sol= UCS(cities[:num_cities])
elif search_method=='greedy':
    sol= greedy(cities[:num_cities])
elif search_method=='A_star':
    sol= A_star(cities[:num_cities])

# save as csv
save_csv(sol, f'{search_method}_{num_cities}.csv')

total_cost = 0

# 탐색 비용 계산
for idx in range(len(sol)-1):

    pos_city_1 = get_pos(cities, sol[idx])
    pos_city_2 = get_pos(cities, sol[idx+1])

    dist = distance(pos_city_1, pos_city_2)
    total_cost += dist

# 출력
print(f'final cost: {total_cost:.2f}')