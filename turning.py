
from numpy.random import seed
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score


data_raw = pd.read_csv("64VAE.csv").dropna(axis=1)
# seed(s)
km_scores = []
for i in range(2, 20, 1):
    # seed(130)
    km = KMeans(n_clusters=i, random_state=0).fit(data_raw)
    # seed(130)
    km_preds = km.predict(data_raw)
    # seed(130)
    silhouette = silhouette_score(data_raw, km_preds, random_state=25)
    print(silhouette)
    km_scores.append(silhouette)

plt.figure(figsize=(250, 80))
plt.title("", fontsize=96)
plt.scatter(x=[i for i in range(2, 20, 1)], y=km_scores, s=60, edgecolor='k', color='blue')
plt.grid(True, linewidth=5)
plt.xlabel("\n\nNumber of clusters", fontsize=20)
plt.ylabel("Silhouette score\n", fontsize=20)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.show()



