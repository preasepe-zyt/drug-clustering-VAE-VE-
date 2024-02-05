from numpy.random import seed
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans, AffinityPropagation, MeanShift, \
    SpectralClustering, Birch, AgglomerativeClustering, DBSCAN, OPTICS
from sklearn.metrics import silhouette_score, calinski_harabasz_score, davies_bouldin_score
import numpy as np
import pandas as pd
from similarity import similarity_list, similarity_pic
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
import seaborn as sns
from pre import property
from matplotlib.lines import Line2D
import matplotlib
import numpy
matplotlib.use('TkAgg')

data = pd.read_csv("64AE.csv")
#data = data.dropna(axis=1)
km = KMeans(n_clusters=10, random_state=25).fit(data)
# seed(130)
km_preds = km.predict(data)
# data = pd.read_csv("cleaned.csv")
data["cluster"] = km_preds
#data = data.sort_values(by="cluster")

# data = data.dropna(axis=1)

# 2. t-SNE plot
tsne_comp = TSNE(n_components=2, perplexity=30, random_state=30, n_iter=1000).fit_transform(data)

tsne_df = pd.DataFrame(data=tsne_comp, columns=['t-SNE1', 't-SNE2'])
tsne_df.head()

tsne_df = pd.concat([tsne_df, pd.DataFrame({'cluster': km_preds})], axis=1)
tsne_df['cluster']+=1
#tsne_df["high-logp"] = ["need" if x in [23, 24] else "not" for x in tsne_df['cluster']]
tsne_df = tsne_df.sort_values('cluster')


# text = []
# for i in range(1, 31):
#   text.append(str(i))
# len(text)

plt.figure(figsize=(12, 8))
sns.set(font_scale=3)
z = sns.color_palette("coolwarm", as_cmap=True)
ax = sns.scatterplot(x="t-SNE1", y="t-SNE2", hue='cluster', data=tsne_df, palette=z)
#ax = sns.color_palette("mako", as_cmap=True)
x = tsne_df['t-SNE1']
y = tsne_df['t-SNE2']
# for i in range(0, 30):
#   plt.annotate(text[i], (x[i], y[i]+.7 ), size=10, color='black', weight='bold')


# 调整图例位置，并缩小图例的尺寸
plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.25), borderaxespad=0, title="Cluster", framealpha=0, ncol=10, fontsize=20)

# 显示所有聚类的标签
for i in range(1, 41):
    cluster_data = tsne_df[tsne_df['cluster'] == i]
    plt.text(cluster_data['t-SNE1'].mean(), cluster_data['t-SNE2'].mean(), str(i),
             size=15, color='black', weight='bold', ha='center', va='center')
ax.set_yticks(numpy.arange(-100, 150, 50))
plt.tight_layout()
plt.show()
plt.savefig("clustering.png", dpi=300)

#cluster
path_c = "data_qu.csv"
path_qu = "group.csv"
data_smiles = pd.read_csv(path_c)
lip = property.lipinski(path_c)[0]

data_qu = pd.read_csv(path_qu)
km_preds +=1
data_qu["group"] = km_preds
data_qu["Product Name"] = data_qu.iloc[:,0]
data_qu = data_qu[["group", "Product Name"]]
need = data_qu[data_qu['group'].isin([5, 4, 9, 8])]
need.to_excel("need.xlsx")
final = pd.merge(data_qu, lip, on="Product Name")
final.to_csv("cluster_sim.csv")
final['Hydrogen Bond Donors'] = pd.to_numeric(final['Hydrogen Bond Donors'], errors='coerce')
final['Hydrogen Bond Acceptors'] = pd.to_numeric(final['Hydrogen Bond Acceptors'], errors='coerce')
final = final.groupby("group").mean()
final.to_csv("cluster_logp.csv")

Carbamazepine = ["C1=CC=C2C(=C1)C=CC3=CC=CC=C3N2C(=O)N", "Carbamazepine"]
Sodium_valproate = ["CCCC(CCC)C(=O)[O-].[Na+]", "Sodium_valproat"]
Sertaconazole = ["C1=CC2=C(C(=C1)Cl)SC=C2COC(CN3C=CN=C3)C4=C(C=C(C=C4)Cl)Cl", "Sertaconazole"]
Levetiracetam = ["CC[C@@H](C(=O)N)N1CCCC1=O", "Levetiracetam"]
Zonisamide = ["C1=CC=C2C(=C1)C(=NO2)CS(=O)(=O)N", "Zonisamide"]
Topiramate = ["CC1(O[C@@H]2CO[C@@]3([C@H]([C@@H]2O1)OC(O3)(C)C)COS(=O)(=O)N)C", "Topiramate"]
drug = numpy.array([Carbamazepine, Sodium_valproate, Sertaconazole, Levetiracetam, Zonisamide, Topiramate])
final_si = pd.DataFrame()
for i in drug:
    sim = similarity_list("cluster_sim.csv", i)
    final_si = pd.concat([sim, final_si], axis=1)

# #提取需要的组
# cu = [23, 7, 17]
# cluster_f = pd.DataFrame()
# for i in range(0, 3):
#     cluster = all_d.loc[all_d["cluster"] == cu[i]]
#     cluster_f = pd.concat([cluster_f, cluster])
#
# cluster_f = cluster_f.sort_values("similarity", ascending=False)
#
# logp.to_csv("logp.csv")
# final.to_csv("cluster_name.csv")
# cluster_f.to_csv("cluster_f.csv")