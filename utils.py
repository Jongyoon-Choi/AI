import numpy as np 
import pandas as pd
import csv

def load_csv(filepath):
    res=[]
    with open(filepath, mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            res.append(row)
    return res

def save_csv(sol,filepath):
    # list를 DataFrame으로 변환
    sorted_df = pd.DataFrame(sol)
    
    # Dataframe을 CSV 파일로 저장
    sorted_df.to_csv(filepath, index=False, header=False)
            
def distance(x, y):
    dist = np.linalg.norm(np.array(x)-np.array(y)) 
    return dist

