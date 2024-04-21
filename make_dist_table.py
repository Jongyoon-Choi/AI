import pandas as pd
from utils import load_csv, save_csv,  distance, get_pos

# 좌표를 불러와서 리스트로 저장
cities = load_csv('2024_AI_TSP.csv')

# 거리 테이블 초기화
distance_table = []

# 도시 수
num_cities = len(cities)

# 모든 도시 쌍에 대한 거리 계산
for i in range(num_cities):
    row = []
    for j in range(num_cities):
        if i == j:
            row.append(0)  # 같은 도시일 경우 거리는 0
        else:
            # 좌표를 가져와서 거리 계산
            pos1 = get_pos(cities, i)
            pos2 = get_pos(cities, j)
            dist = distance(pos1, pos2)
            row.append(dist)
    distance_table.append(row)

save_csv(distance_table, 'distance.csv')