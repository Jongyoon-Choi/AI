import heapq
from utils import distance, get_pos

def greedy(cities):
    num_cities = len(cities)
    
    # 시작 도시
    start_city = 0
    
    # 초기화 (휴리스틱, 도시, 방문 여부, 방문 순서)
    pq = [(0, start_city, [i == start_city for i in range(num_cities)], [start_city])]
    
    sol=None
    count=0
    
    while pq:
        # 가장 우선순위가 높은 노드
        heuristic, _, visited, path = heapq.heappop(pq)
        
        # 출력
        # print(path, heuristic)
        count+=1
        
        # 모든 도시를 방문했을 경우 종료
        if len(path) == num_cities:
            sol=path
            print(f'방문 노드 수: {count}')
            break
        
        
        # fringe 추가
        for next_city in range(num_cities):
            if not visited[next_city]:
                new_visited = visited[:]
                new_visited[next_city] = True
                
                new_path = path + [next_city]
                
                new_heuristic = estimate_remaining_cost(cities, new_visited, next_city)
                
                heapq.heappush(pq, (new_heuristic, next_city, new_visited, new_path))
    
    return sol

# 잔여 비용 추정을 위한 휴리스틱 함수
def estimate_remaining_cost(cities, visited, current_city):
    num_cities = len(cities)
    
    # 남은 방문 도시 수
    remaining_cities = num_cities - sum(visited)
    
    # 각 방문하지 않은 도시 중 최소 거리
    min_distance = min((distance(get_pos(cities, current_city), [float(city[0]), float(city[1])]) for city, is_visited in zip(cities, visited) if not is_visited), default=0)
    
    return min_distance * remaining_cities