# 프로젝트 구조 설명

이 프로젝트는 유전 알고리즘(GA) 및 다양한 탐색 및 정렬 기법을 포함하는 다양한 알고리즘을 구현하는 데 사용됩니다. 아래는 프로젝트의 각 폴더와 파일에 대한 설명입니다.

## 1. GA_result (Folder)
GA 알고리즘을 사용한 결과 (matplot을 사용한 시각화 이미지)가 저장되는 폴더입니다.

## 2. genetic_algorithm (Folder)
유전 알고리즘에서 사용되는 연산을 포함하는 폴더입니다.

### 2-1. chromosome.py
- 염색체 Class를 정의하는 파일입니다.
- 초기화, 적합도 계산 등의 작업을 수행합니다.

### 2-2. cycle.py
- cycle 교차 연산을 구현한 파일입니다.

### 2-3. mutation.py
- 돌연변이 연산을 구현한 파일입니다.

### 2-4. order.py
- 순서 교차 연산을 구현한 파일입니다.

### 2-5. PMX.py
- PMX 교차 연산을 구현한 파일입니다.

### 2-6. positon_based.py
- 위치 기반 교차 연산을 구현한 파일입니다.

### 2-7. select.py
- 선택 연산을 구현한 파일입니다. (교차에서 사용됨)

### 2-8. uniform_order_based.py
- 균등 순서 교차 연산을 구현한 파일입니다.

## 3. search_methods (Folder)
Tree 탐색 기법을 포함하는 폴더입니다.

### 3-1. A_star.py
- 휴리스틱을 사용한 A* 알고리즘을 구현한 파일입니다.

### 3-2. greedy.py
- 탐욕 알고리즘을 구현한 파일입니다.

## 4. solutions (Folder)
main이나 GA의 solution csv 파일을 저장하는 폴더입니다.

## 5. chunk_sort.py
chunk 정렬 기법을 구현한 파일입니다.

## 6. GA.py
genetic_algorithm에 구현된 연산을 사용하여 유전 알고리즘을 실행하는 파일입니다.

## 7. main.py
일반적인 탐색을 수행하는 파일입니다. (탐색 방법과 정렬 방법을 조합하여 사용)

## 8. make_dist_table.py
각 도시쌍의 거리 배열 distance.csv (998 x 998)를 생성하는 파일입니다.

## 9. origin_sort.py
원점 기준 정렬 기법을 구현한 파일입니다.

## 10. quadrant_sort.py
사분면 정렬 기법을 구현한 파일입니다.

## 11. test.sh
한 가지 조합에 대해 GA.py를 실행하는 쉘 스크립트입니다.

## 12. training.sh
여러 파라미터 조합을 사용하여 GA.py를 실행하는 쉘 스크립트입니다.

## 13. utils.py
여러 파일에서 사용되는 함수를 구현한 파일입니다. (csv 파일 불러오기 및 저장, 좌표 간의 거리 계산 등)

## 14. visualization.py
solution csv 파일을 불러와서 시각화하는 파일입니다.

## 15. x_sort.py
x 기준 정렬 기법을 구현한 파일입니다.
