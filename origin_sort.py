# 원점 기준 정렬 방식
from utils import load_csv,distance

def origin_sort_function():
    # 좌표를 불러와서 리스트로 저장
    cities = load_csv('2024_AI_TSP.csv')

    # 각 좌표를 실수형으로 변환
    cities = [[float(coord) for coord in city] for city in cities]

    # 각 csv 라인에 index 추가
    for i in range(len(cities)):
        cities[i].append(i)
    
    # 도시를 원점과의 거리를 기준으로 정렬
    cities.sort(key=lambda city: distance(city[:2], [0, 0]))

    # 도시를 index만 저장
    sorted_cities= [row[2] for row in cities]

    # 도시 리스트에서 시작점 찾기
    index = sorted_cities.index(0)

    # 찾은 도시를 맨 앞으로 이동시키기
    sorted_cities.insert(0, sorted_cities.pop(index))


    return sorted_cities