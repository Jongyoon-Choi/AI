import matplotlib.pyplot as plt
from utils import load_csv

# 원본 csv 파일
cities = load_csv('2024_AI_TSP.csv')

# solutions 폴더에 있는 파일명 적어주세요.(e.g. 'A_star_10')
file_name='greedy_998'    
solution = load_csv(f'solutions/{file_name}.csv')

# 방문한 도시의 좌표를 저장할 리스트
visited_order = []

# 방문한 도시의 좌표를 추출하여 리스트에 저장
for idx in solution:
    x, y = cities[int(idx[0])]
    visited_order.append((x, y))

# X와 Y 좌표를 따로 저장
x_coords = [float(city[0]) for city in visited_order]
y_coords = [float(city[1]) for city in visited_order]

# 도시의 좌표를 점으로 표시
plt.figure(figsize=(8, 6))
plt.scatter(x_coords, y_coords, color='red', label='city', s=10)  # 도시 좌표를 빨간색으로 표시하고, 점의 크기를 작게 조절

# 도시를 순서대로 연결하는 선을 파란색으로 표시 (점과 점 사이만 선으로 연결)
for i in range(len(x_coords) - 1):
    plt.plot(x_coords[i:i+2], y_coords[i:i+2], linestyle='-', color='blue')

plt.xlabel('X')
plt.ylabel('Y')
plt.title(file_name)
plt.legend()  # 범례 표시
plt.grid(True)
plt.show()
