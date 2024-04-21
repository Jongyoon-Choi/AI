from utils import load_csv, save_csv
from search_methods.greedy import greedy
from search_methods.A_star import A_star

# 2024_AI_TSP.csv 파일을 이용한 dist_table(1000 x 1000)을 사용하였음.
# 도시별 거리 테이블을 불러와서 리스트로 저장
dist_table= load_csv('distance.csv')

# 정렬된 도시 리스트를 저장
sorted_cities = load_csv('sorted_TSP.csv')

# 결과 초기화
sol = []

# 탐색 방법
search_method='sub_A_star'  # greedy, A_star, sub_A_star

# 방문할 도시 수 (subtree에서는 subtree의 size)
num_cities=10

# Search
if search_method=='greedy':
    sol += greedy(dist_table, [i for i in range(num_cities)])   # num_cities개의 도시만 탐색
elif search_method=='A_star':
    sol += A_star(dist_table, [i for i in range(num_cities)])   # num_cities개의 도시만 탐색
elif search_method=='sub_A_star':
    # subtree 반복 탐색 방법 (A*)
    subtree_list = []

    # subtree_size만큼 분할하여 subtree_list 생성
    for i in range(0, len(sorted_cities), num_cities):
        subtree =  [int(row[2]) for row in sorted_cities[i:i+num_cities]]
        subtree_list.append(subtree)

    # 각 subtree 탐색
    for subtree in subtree_list:
        sol += A_star(dist_table, subtree)

# save as csv
save_csv(sol, f'solutions/{search_method}_{num_cities}.csv')

# 시작점을 추가
sol.append(int(0))

# 탐색 비용
total_cost = 0

# 탐색 비용 계산
for idx in range(len(sol)-1):

    dist = float(dist_table[sol[idx]][sol[idx+1]])
    total_cost += dist

# 출력
print(f'final cost: {total_cost:.2f}')