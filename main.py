from utils import load_csv, save_csv, distance, get_pos
from search_methods.greedy import greedy
from search_methods.UCS import UCS
from search_methods.A_star import A_star

# 좌표를 불러와서 리스트로 저장
cities = load_csv('2024_AI_TSP.csv')

# 결과 초기화
sol = []

# 방문할 도시 수
num_cities=15

# 탐색 방법
search_method='A_star'

# Search
if search_method=='UCS':
    sol += UCS(cities[:num_cities])
elif search_method=='greedy':
    sol += greedy(cities[:num_cities])
elif search_method=='A_star':
    sol += A_star(0, num_cities)

# subgraph 반복 탐색
# start=0

# for i in range(100):
#     sol += A_star(start=start, end= start+num_cities)
#     start += num_cities

# save as csv
save_csv(sol, f'solutions/{search_method}_{num_cities}.csv')

total_cost = 0

# 탐색 비용 계산
for idx in range(len(sol)-1):

    pos_city_1 = get_pos(cities, sol[idx])
    pos_city_2 = get_pos(cities, sol[idx+1])

    dist = distance(pos_city_1, pos_city_2)
    total_cost += dist

# 출력
print(f'final cost: {total_cost:.2f}')