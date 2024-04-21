import heapq

def A_star(dist_table, search_idx, start = 0): # search_idx에 존재하는 index들을 탐색
    # 탐색 도시 수
    num_cities = len(search_idx)
    
    # 시작 도시
    start_city = start

    # dist_table 슬라이싱
    sliced_dist_table=[dist_table[city] for city in search_idx] # 행 슬라이싱
    sliced_dist_table=[[row[city] for city in search_idx] for row in sliced_dist_table] # 열 슬라이싱
    
    # 초기화 (총 비용 (누적거리 + 휴리스틱), 누적거리, 현재 도시, 방문 여부, 방문 순서)
    pq = [(0, 0, start_city, [i == start_city for i in range(num_cities)], [start_city])]

    count=0 # 방문 노드 수
    sol=None

    while pq:
        # 가장 우선순위가 높은 노드
        total_cost, cost, current_city, visited, path = heapq.heappop(pq)
        
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
                
                new_cost = cost + float(sliced_dist_table[current_city][next_city])
                heuristic = heuristic_function(sliced_dist_table, new_visited)
                total_cost = new_cost + heuristic
                
                heapq.heappush(pq, (total_cost, new_cost, next_city, new_visited, new_path))

    return [search_idx[x] for x in sol]

# 휴리스틱 함수
def heuristic_function(sliced_dist_table, new_visited):
    num_cities = len(sliced_dist_table)
    min_distances = []

    for i in range(num_cities):
        if not new_visited[i]:
            # 자기 자신을 제외한 최소 거리 찾기
            min_distance = min((float(sliced_dist_table[i][j]) for j in range(num_cities) if j != i and not new_visited[j]), default=0) 
            min_distances.append(min_distance)

    # 방문하지 않은 노드 중 자신을 제외한 최소 거리의 합
    return sum(min_distances)
