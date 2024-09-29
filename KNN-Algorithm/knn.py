import pandas as pd
import math

def classifyAPoint(points, p, k=5):
    distances = []
    for colour in points:
        for feature in points[colour]:
            euclidean_distance = math.sqrt((feature[0] - p[0]) ** 2 + (feature[1] - p[1]) ** 2 + (feature[2] - p[2]) ** 2)
            distances.append((euclidean_distance, colour))

    distances = sorted(distances)[:k]

    r_freq = 0
    g_freq = 0
    b_freq = 0

    for d in distances:
        if d[1] == 'Red':
            r_freq += 1
        elif d[1] == 'Green':
            g_freq += 1
        elif d[1] == 'Blue':
            b_freq += 1

    if r_freq > g_freq and r_freq > b_freq:
        return 'Red'
    elif g_freq > r_freq and g_freq > b_freq:
        return 'Green'
    else:
        return 'Blue'

def main():
    df = pd.read_csv('rgb_dataset.csv')

    points = {'Red': [], 'Green': [], 'Blue': []}

    for _, row in df.iterrows():
        points[row['Colour']].append((row['Red'], row['Green'], row['Blue']))

    p = (24, 112, 22)
    k = 5

    print("The RGB classified to unknown point"+str(p)+" is: {}".format(classifyAPoint(points, p, k)))

if __name__ == '__main__':
    main()