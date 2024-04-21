def greedy(dist_table, search_idx, start = 0):  # search_idx에 존재하는 index들을 탐색
    # 탐색 도시 수
    num_cities = len(search_idx)
    
    # 시작 도시
    start_city = start

    # dist_table 슬라이싱
    sliced_dist_table=[dist_table[city] for city in search_idx] # 행 슬라이싱
    sliced_dist_table=[[row[city] for city in search_idx] for row in sliced_dist_table] # 열 슬라이싱

    # 방문 여부
    visited = [False] * num_cities
    visited[start_city] = True
    
    # 방문 순서
    sol=[start_city]
    
    current_city = start_city
    
    for _ in range(num_cities - 1):
        min_dist = float('inf')
        next_city = None
        
        for i in range(num_cities):
            if not visited[i]:
                dist = float(sliced_dist_table[current_city][i])
                if dist < min_dist:
                    min_dist = dist
                    next_city = i
        
        sol.append(next_city)
        visited[next_city] = True
        current_city = next_city
    
    return sol