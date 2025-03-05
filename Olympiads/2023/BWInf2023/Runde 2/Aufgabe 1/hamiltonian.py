import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

def read_coordinates(file):
    with open(file, "r") as f:
        lines = f.readlines()
        coordinates = []
        for line in lines:
            x, y = map(float, line.strip().split())
            coordinates.append((x, y))
    return coordinates

def k_means_clustering(points):
    # Ermittle das optimale K
    k_values = range(2, 11)
    inertia_values = []
    silhouette_scores = []

    for k in k_values:
        kmeans = KMeans(n_clusters=k)
        kmeans.fit(points)
        inertia_values.append(kmeans.inertia_)
        silhouette_scores.append(silhouette_score(points, kmeans.labels_))

    elbow_point = np.argmin(np.gradient(inertia_values))

    # Führe K-Means-Clustering mit optimalem K durch
    k_optimal = k_values[elbow_point]
    kmeans_optimal = KMeans(n_clusters=k_optimal)
    kmeans_optimal.fit(points)
    labels = kmeans_optimal.labels_

    # Plotte die Ergebnisse
    plt.figure(figsize=(10, 6))
    plt.scatter(points[:, 0], points[:, 1], c=labels, cmap='viridis', s=100, alpha=0.8)
    plt.scatter(kmeans_optimal.cluster_centers_[:, 0], kmeans_optimal.cluster_centers_[:, 1], s=200, alpha=0.9)
    plt.title(f'K-Means Clustering mit K = {k_optimal}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

# Liste aus Tupeln als Koordinaten von Punkten
file = 'X:\wenigerkrumm7.txt'
coordinates = read_coordinates(file)
points_array = np.array(coordinates)

k_means_clustering(points_array)
