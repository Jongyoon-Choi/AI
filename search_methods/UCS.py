import heapq
from utils import distance, get_pos

def UCS(cities):
    num_cities = len(cities)
    
    # 시작 도시
    start_city = 0
    
    # 초기화 (비용, 도시, 방문 여부, 방문 순서)
    pq = [(0, start_city, [i == start_city for i in range(num_cities)], [start_city])] 
    
    sol=None
    count=0
    
    while pq:
        # 가장 우선순위가 높은 노드
        cost, current_city, visited, path = heapq.heappop(pq)
        
        # 현재 도시의 좌표
        pos_current_city = get_pos(cities, current_city)
        
        # 출력
        # print(path, cost)
        count+=1
        
        # 모든 도시를 방문했을 경우 종료
        if len(path) == num_cities:
            sol=path
            print(f'방문 노드 수: {count}')
            break
        
        # fringe 추가
        for next_city in range(num_cities):
            if not visited[next_city]:
                pos_next_city=get_pos(cities, next_city)
                new_cost = cost + distance(pos_current_city, pos_next_city)
                
                new_visited = visited[:]
                new_visited[next_city] = True
                
                new_path = path + [next_city]
                
                heapq.heappush(pq, (new_cost, next_city, new_visited, new_path))
        
    return sol

# pq의 size를 제한(일정 크기를 넘어서면 안좋은 노드 삭제)하여 개선의 여지가 있음.