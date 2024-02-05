from numpy.random import seed
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans, AffinityPropagation, MeanShift, \
    SpectralClustering, Birch, AgglomerativeClustering, DBSCAN, OPTICS
from sklearn.metrics import silhouette_score, calinski_harabasz_score, davies_bouldin_score

minsample = 30
ncluster = 5
def silhouette(x, file_name):

    km = KMeans(n_clusters=ncluster, random_state=0).fit(x)
    # seed(130)
    km_preds = km.predict(x)
    silhouette_km = silhouette_score(x, km_preds, metric='euclidean')

    # ap = AffinityPropagation().fit(x)
    # ap_preds = ap.predict(x)
    # silhouette_ap = silhouette_score(x, ap_preds, metric='euclidean')

    ms = MeanShift(bandwidth=0.5).fit(x)
    ms_preds = ms.predict(x)
    silhouette_ms = silhouette_score(x, ms_preds, metric='euclidean')

    sc = SpectralClustering(n_clusters=ncluster, assign_labels='discretize',
                            random_state=0).fit(x)
    sc_preds = sc.labels_
    silhouette_sc = silhouette_score(x, sc_preds, metric='euclidean')

    bi = Birch(n_clusters=ncluster).fit(x)
    bi_preds = bi.predict(x)
    silhouette_bi = silhouette_score(x, bi_preds, metric='euclidean')

    hc = AgglomerativeClustering(n_clusters=ncluster).fit(x)
    hc_preds = hc.labels_
    silhouette_hc = silhouette_score(x, hc_preds, metric='euclidean')

    db = DBSCAN(eps=1, min_samples=minsample).fit(x)
    db_preds = db.labels_
    silhouette_db = silhouette_score(x, db_preds, metric='euclidean')

    op = OPTICS(min_samples=10).fit(x)
    op_preds = op.labels_
    silhouette_op = silhouette_score(x, op_preds, metric='euclidean')

    score = [silhouette_km,  silhouette_ms, silhouette_sc,
             silhouette_bi, silhouette_hc, silhouette_db, silhouette_op]#silhouette_ap,
    name = ["K-Means", "Mean-shift", "Spectral clustering",
            "BIRCH", "Agglomerative clustering",  "DBSCAN", "OPTICS"] #, "Affinity propagation"
    final_silhouette = pd.DataFrame([score], columns=name, index=[file_name])
    # plt.figure(figsize=(25, 7))
    # plt.title("silhouette", fontsize=20)
    # for i in range(0, len(name)):
    #     plt.scatter(x=name[i], y=score[i], s=100, edgecolor='k', label=name[i]+"-"+file_name)
    # plt.grid(True, linewidth=1)
    # plt.xlabel("\n\nNumber of clusters", fontsize=20)
    # plt.ylabel("Silhouette score" + "\n", fontsize=20)
    # plt.xticks(fontsize=20)
    # plt.yticks(fontsize=20)
    # plt.legend(loc='upper right', frameon=False)
    # #plt.show()
    return final_silhouette

def calinski(x, file_name):

    km = KMeans(n_clusters=ncluster, random_state=0).fit(x)
    # seed(130)
    km_preds = km.predict(x)
    calinski_km = calinski_harabasz_score(x, km_preds)

    # ap = AffinityPropagation().fit(x)
    # ap_preds = ap.predict(x)
    # calinski_ap = calinski_harabasz_score(x, km_preds)

    ms = MeanShift(bandwidth=0.5).fit(x)
    ms_preds = ms.predict(x)
    calinski_ms = calinski_harabasz_score(x, ms_preds)

    sc = SpectralClustering(n_clusters=ncluster, assign_labels='discretize',
                            random_state=0).fit(x)
    sc_preds = sc.labels_
    calinski_sc = calinski_harabasz_score(x, sc_preds)

    bi = Birch(n_clusters=ncluster).fit(x)
    bi_preds = bi.predict(x)
    calinski_bi = calinski_harabasz_score(x, bi_preds)

    hc = AgglomerativeClustering(n_clusters=ncluster).fit(x)
    hc_preds = hc.labels_
    calinski_hc = calinski_harabasz_score(x, hc_preds)

    db = DBSCAN(eps=1, min_samples=minsample).fit(x)
    db_preds = db.labels_
    calinski_db = calinski_harabasz_score(x, db_preds)

    op = OPTICS(min_samples=10).fit(x)
    op_preds = op.labels_
    calinski_op = calinski_harabasz_score(x, op_preds)

    score = [calinski_km, calinski_ms, calinski_sc,
             calinski_bi, calinski_hc, calinski_db, calinski_op] #, calinski_ap
    name = ["K-Means", "Mean-shift", "Spectral clustering",
            "BIRCH", "Agglomerative clustering",  "DBSCAN", "OPTICS"] #, "Affinity propagation"
    final_calinski = pd.DataFrame([score], columns=name, index=[file_name])
    # plt.figure(figsize=(25, 7))
    # plt.title("calinski", fontsize=20)
    # for i in range(0, len(name)):
    #     plt.scatter(x=name[i], y=score[i], s=100, edgecolor='k', label=name[i]+"-"+file_name)
    # plt.grid(True, linewidth=1)
    # plt.xlabel("\n\nNumber of clusters", fontsize=20)
    # plt.ylabel("Calinski score" + "\n", fontsize=20)
    # plt.xticks(fontsize=20)
    # plt.yticks(fontsize=20)
    # plt.legend(loc='upper right', frameon=False)
    # #plt.show()
    return final_calinski



def davies(x, file_name):

    km = KMeans(n_clusters=ncluster, random_state=0).fit(x)
    # seed(130)
    km_preds = km.predict(x)
    davies_km = davies_bouldin_score(x, km_preds)

    # ap = AffinityPropagation().fit(x)
    # ap_preds = ap.predict(x)
    # davies_ap = davies_bouldin_score(x, ap_preds)

    ms = MeanShift(bandwidth=0.5).fit(x)
    ms_preds = ms.predict(x)
    davies_ms = davies_bouldin_score(x, ms_preds)

    sc = SpectralClustering(n_clusters=ncluster, assign_labels='discretize',
                            random_state=0).fit(x)
    sc_preds = sc.labels_
    davies_sc = davies_bouldin_score(x, sc_preds)

    bi = Birch(n_clusters=ncluster).fit(x)
    bi_preds = bi.predict(x)
    davies_bi = davies_bouldin_score(x, bi_preds)

    hc = AgglomerativeClustering(n_clusters=ncluster).fit(x)
    hc_preds = hc.labels_
    davies_hc = davies_bouldin_score(x, hc_preds)

    db = DBSCAN(eps=1, min_samples=minsample).fit(x)
    db_preds = db.labels_
    davies_db = davies_bouldin_score(x, db_preds)

    op = OPTICS(min_samples=10).fit(x)
    op_preds = op.labels_
    davies_op = davies_bouldin_score(x, op_preds)

    score = [davies_km, davies_ms, davies_sc,
             davies_bi, davies_hc, davies_db, davies_op] #, davies_ap
    name = ["K-Means", "Mean-shift", "Spectral clustering",
            "BIRCH", "Agglomerative clustering",  "DBSCAN", "OPTICS"] #, "Affinity propagation"
    final_davies = pd.DataFrame([score], columns=name, index=[file_name])
    # plt.figure(figsize=(25, 7))
    # plt.title("davies", fontsize=20)
    # for i in range(0, len(name)):
    #     plt.scatter(x=name[i], y=score[i], s=100, edgecolor='k', label=name[i]+"-"+file_name)
    # plt.grid(True, linewidth=1)
    # plt.xlabel("\n\nNumber of clusters", fontsize=20)
    # plt.ylabel("davies score" + "\n", fontsize=20)
    # plt.xticks(fontsize=20)
    # plt.yticks(fontsize=20)
    # plt.legend(loc='upper right', frameon=False)
    # #plt.show()
    return final_davies


if __name__ == "__main__":
    nu = [16, 32, 64]
    me = ["AE", "VAE"]
    indicate = ["silhouette", "calinski", "davies"]
    final = pd.DataFrame()
    for i in range(0, 2):
        for i2 in range(0, 3):
            file_name = str(nu[i2]) + me[i]
            data = pd.read_csv(file_name+".csv")
            a = silhouette(data, file_name+"-"+indicate[0])
            b = calinski(data, file_name+"-"+indicate[1])
            c = davies(data, file_name+"-"+indicate[2])
            final_cu = pd.concat([a, b, c])
            final = pd.concat([final, final_cu])
    final.to_csv("final.csv")





