import heapq
from utils import load_csv, distance, get_pos

def A_star(cities, start = 0, end = 1000): # cities[start,end-1]을 탐색
    num_cities = end-start

    new_cities=cities[start:end]
    
    # 시작 도시
    start_city = 0
    
    # 초기화 (총 비용 (비용 + 휴리스틱), 비용, 도시, 방문 여부, 방문 순서)
    pq = [(0, 0, start_city, [i == start_city for i in range(num_cities)], [start_city])]
    
    sol=None
    count=0
    dist_table=load_csv('distance.csv')[start:end] # 행 슬라이싱
    dist_table=[row[start:end] for row in dist_table] # 열 슬라이싱

    while pq:
        # 가장 우선순위가 높은 노드
        total_cost, cost, current_city, visited, path = heapq.heappop(pq)
        
        # 현재 도시의 좌표
        pos_current_city = get_pos(new_cities, current_city)
        
        # 출력
        # print(path, total_cost)
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
                
                pos_next_city=get_pos(new_cities, next_city)
                new_cost = cost + distance(pos_current_city, pos_next_city)
                heuristic = heuristic_function(dist_table, new_visited)
                total_cost = new_cost + heuristic
                
                heapq.heappush(pq, (total_cost, new_cost, next_city, new_visited, new_path))

    return [x + start for x in sol]

# 휴리스틱 함수
def heuristic_function(dist_table, new_visited):
    num_cities = len(dist_table)
    min_distances = []

    for i in range(num_cities):
        if not new_visited[i]:
            # 자기 자신을 제외한 최소 거리 찾기
            min_distance = min((float(dist_table[i][j]) for j in range(num_cities) if j != i and not new_visited[j]), default=0)
            min_distances.append(min_distance)

    # 방문하지 않은 노드 중 자신을 제외한 최소 거리의 합
    return sum(min_distances)
