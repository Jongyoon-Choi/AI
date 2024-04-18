from utils import distance, get_pos

def greedy(cities):
    num_cities = len(cities)
    
    # 시작 도시
    start_city = 0

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
                dist = distance(get_pos(cities, current_city), get_pos(cities, i))
                if dist < min_dist:
                    min_dist = dist
                    next_city = i
        
        sol.append(next_city)
        visited[next_city] = True
        current_city = next_city
    
    return sol