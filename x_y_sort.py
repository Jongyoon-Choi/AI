# x좌표로 우선 정렬한 후 n개의 구역으로 나누어 y정렬을 하는 방식

import matplotlib.pyplot as plt
from utils import load_csv, save_csv

# 좌표를 불러와서 리스트로 저장
cities = load_csv('2024_AI_TSP.csv')

# 각 csv 라인에 index 추가
for i in range(len(cities)):
    cities[i].append(i)

# 분할 횟수
num_chunk=10

# 도시를 x로 정렬
cities.sort(key=lambda city: float(city[0]))

# num_chunk개의 구역 분할 후 y로 정렬
sorted_cities = []
chunk_size=len(cities)//num_chunk
for i in range(num_chunk):
        start_idx = i * chunk_size
        end_idx = (i + 1) * chunk_size
        chunk = cities[start_idx : end_idx]
        chunk.sort(key=lambda city: float(city[1]), reverse= True if i % 2 == 0 else False)  # y 좌표를 기준으로 정렬 (지그재그로)
        # chunk.sort(key=lambda city: float(city[1])) # 수동 정렬에서는 이 방식
        sorted_cities.extend(chunk)

# # 수동 정렬
# res=[]
# res.extend(sorted_cities[660:700])
# res.extend(sorted_cities[790:800])
# res.extend(sorted_cities[890:900])
# res.extend(sorted_cities[999:899:-1])
# res.extend(sorted_cities[800:810])
# res.extend(sorted_cities[700:710])
# res.extend(sorted_cities[600:610])
# res.extend(sorted_cities[500:510])
# res.extend(sorted_cities[400:410])
# res.extend(sorted_cities[300:310])
# res.extend(sorted_cities[200:210])
# res.extend(sorted_cities[100:110])
# res.extend(sorted_cities[0:100])
# res.extend(sorted_cities[199:109:-1])
# res.extend(sorted_cities[210:300])
# res.extend(sorted_cities[399:309:-1])
# res.extend(sorted_cities[410:500])
# res.extend(sorted_cities[599:509:-1])
# res.extend(sorted_cities[610:620])
# res.extend(sorted_cities[710:720])
# res.extend(sorted_cities[810:890])
# res.extend(sorted_cities[789:719:-1])
# res.extend(sorted_cities[620:660])

# 도시 리스트에서 시작점 찾기
index = sorted_cities.index(['-0.0','0.0',0])

# 찾은 도시를 맨 앞으로 이동시키기
sorted_cities.insert(0, sorted_cities.pop(index))

# csv 파일로 저장
save_csv(sorted_cities, 'x_y_sorted_TSP.csv')

# 시각화
# x 좌표와 y 좌표를 따로 추출
x_coords = [float(city[0]) for city in sorted_cities]
y_coords = [float(city[1]) for city in sorted_cities]

# 10개씩 나누어서 시각화
for i in range(num_chunk):
    start_idx = i * chunk_size
    end_idx = (i + 1) * chunk_size
    plt.scatter(x_coords[start_idx:end_idx], y_coords[start_idx:end_idx], label=f'Chunk {i+1}')

# 그래프에 레이블과 제목 추가
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.title(f'Sorted Cities (Divided into {num_chunk} Chunks)')
plt.legend()  # 범례 표시

# 그래프 표시
plt.show()