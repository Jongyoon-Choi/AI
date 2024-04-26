from utils import load_csv, save_csv

# 좌표를 불러와서 리스트로 저장
cities = load_csv('2024_AI_TSP.csv')

# 각 csv 라인에 index 추가
for i in range(len(cities)):
    cities[i].append(i)

# 도시를 x, y 순으로 정렬
cities.sort(key=lambda city: float(city[0]))

# 도시 리스트에서 시작점 찾기
index = cities.index(['0','0',0])

# 찾은 도시를 맨 앞으로 이동시키기
cities.insert(0, cities.pop(index))

# csv 파일로 저장
save_csv(cities, 'x_sorted_TSP.csv')