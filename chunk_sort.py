# x좌표로 우선 정렬한 후 n개의 구역으로 나누어 y정렬을 하는 방식
import math
from utils import load_csv

def chunk_sort_function(num_chunk):

    # 좌표를 불러와서 리스트로 저장
    cities = load_csv('2024_AI_TSP.csv')
    num_cities = len(cities)

    # 각 csv 라인에 index 추가
    for i in range(len(cities)):
        cities[i].append(i)

    # 모든 도시를 x로 정렬
    cities.sort(key=lambda city: float(city[0]))

    # num_chunk개의 구역 분할 후 y로 정렬
    sorted_cities = []
    chunk_size = math.ceil(num_cities/num_chunk)

    for i in range(num_chunk):
            start_idx = i * chunk_size
            end_idx = (i + 1) * chunk_size
            chunk = cities[start_idx : end_idx if end_idx < num_cities else num_cities]
            chunk.sort(key=lambda city: float(city[1]), reverse= True if i % 2 == 0 else False)  # y 좌표를 기준으로 정렬 (지그재그로)
            chunk= [row[2] for row in chunk]
            sorted_cities.extend(chunk)
            
    # 도시 리스트에서 시작점 찾기
    index = sorted_cities.index(0)

    # 찾은 도시를 맨 앞으로 이동시키기
    sorted_cities.insert(0, sorted_cities.pop(index))

        
    return sorted_cities
