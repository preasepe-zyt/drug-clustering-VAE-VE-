from numpy.random import seed
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from matplotlib.ticker import FormatStrFormatter

def kmean(x, name):
    path = r"C:\Users\79403\Desktop\药物筛选"
    colors = ['blue', 'green', 'red', 'purple', 'orange', 'olive', 'cyan', 'pink', 'brown']
    # seed(s)
    km_scores = []
    vae32 = []
    db_score = []
    for i in range(5, 50, 5):
        # seed(130)
        km = KMeans(n_clusters=i, random_state=25).fit(x)
        # seed(130)
        km_preds = km.predict(x)

        # seed(130)
        silhouette = silhouette_score(x, km_preds, random_state=25)
        vae32.append(silhouette)
        print("Silhouette score for number of cluster(s) {}: {}".format(i, silhouette))

    plt.figure(figsize=(12, 6))
    plt.title(name, fontsize=20)
    plt.scatter(x=[i for i in range(5, 50, 5)], y=vae32, s=200, edgecolor='k', color=colors)
    plt.grid(True, linewidth=1)
    plt.xlabel("Number of clusters", fontsize=20)
    plt.ylabel("Silhouette score", fontsize=20)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.legend(loc='upper right', frameon=False)
    plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
    plt.savefig(path+"\\"+name+"_"+"clustering.png", dpi=300)

if __name__ == "__main__":
    nu = [16, 32, 64]
    me = ["AE", "VAE"]
    indicate = ["silhouette", "calinski", "davies"]
    final = pd.DataFrame()
    for i in range(0, 2):
        for i2 in range(0, 3):1
            file_name = str(nu[i2]) + me[i]
            data = pd.read_csv(file_name + ".csv")
            kmean(data, file_name)



