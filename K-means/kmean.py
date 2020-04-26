# Prabhas Kumra
# CS-458
# Assignment #8

import numpy as np
import random

random.seed(20)

def converged(new_centers, centers):
    return (set([tuple(a) for a in new_centers]) == set([tuple(a) for a in centers]))

def findClusters(points, new_centers):
    clusters = {}
    for x in points:
        min_dist = min([(i[0], np.linalg.norm(x-new_centers[i[0]])) \
                    for i in enumerate(new_centers)], key=lambda t:t[1])[0]
        try:
            clusters[min_dist].append(x)
        except KeyError:
            clusters[min_dist] = [x]

    return clusters

def k_mean(points, k):
    centers = random.sample(list(points), k)
    new_centers = random.sample(list(points), k)

    while not converged(new_centers, centers):
        centers = new_centers
        clusters = findClusters(points, new_centers)

        newPoints = []
        keys = sorted(clusters.keys())
        for k in keys:
            newPoints.append(np.mean(clusters[k], axis = 0))
        new_centers = newPoints

    return(new_centers, clusters)


def main():
    data = np.genfromtxt("data.txt", delimiter=",")

    k = int(data[0][0])
    m = int(data[0][1])

    data = np.delete(data,0,0)

    print("Input Points:")
    print(data)

    new_centers, clusters = k_mean(data, k)

    print("")
    print("Output:")
    print(new_centers[0])
    print(new_centers[1])
    # print(clusters)

if __name__ == "__main__":
    main()