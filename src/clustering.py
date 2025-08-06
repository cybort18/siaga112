from sklearn.cluster import DBSCAN
import numpy as np

def detect_clusters(data_file, eps=0.01, min_samples=2):
    with open(data_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    data = [line.strip().split(',') for line in lines]
    texts = [item[0] for item in data]
    coords = np.array([[float(item[1]), float(item[2])] for item in data])

    clustering = DBSCAN(eps=eps, min_samples=min_samples).fit(coords)
    labels = clustering.labels_

    clusters = {}
    for text, label in zip(texts, labels):
        if label != -1:
            if label not in clusters:
                clusters[label] = []
            clusters[label].append(text)

    return clusters

if __name__ == "__main__":
    clusters = detect_clusters("data/cluster_data.txt")
    print("Klaster insiden:")
    for cluster_id, texts in clusters.items():
        print(f"Klaster {cluster_id}: {len(texts)} laporan")
        for text in texts:
            print(f"  - {text}")