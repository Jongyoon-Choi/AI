import numpy as np 
import csv

def distance(x, y):
    dist = np.linalg.norm(np.array(x)-np.array(y)) 
    return dist

def get_pos(cities,index):
    return [float(cities[index][0]), float(cities[index][1])]

def save_csv(sol,filename):
    filepath=f'solutions/{filename}'
    with open(filepath, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for city in sol:
            writer.writerow([city])