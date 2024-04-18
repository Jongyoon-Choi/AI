import numpy as np 
import csv

def load_csv(filepath):
    res=[]
    with open(filepath, mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            res.append(row)
    return res

def save_csv(sol,filepath):
    with open(filepath, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for city in sol:
            writer.writerow([city])
            
def distance(x, y):
    dist = np.linalg.norm(np.array(x)-np.array(y)) 
    return dist

def get_pos(cities,index):
    return [float(cities[index][0]), float(cities[index][1])]

