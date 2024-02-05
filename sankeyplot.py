from numpy.random import seed
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans, AffinityPropagation, MeanShift, \
    SpectralClustering, Birch, AgglomerativeClustering, DBSCAN, OPTICS
from sklearn.metrics import silhouette_score, calinski_harabasz_score, davies_bouldin_score
from keras.models import load_model
import numpy as np
import pandas as pd
from numpy.random import seed
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
import seaborn as sns
from pre import descriptors, lipinski

data = pd.read_csv("cleaned.csv")
data = data.dropna(axis=1)
ap = AffinityPropagation().fit(data)
ap_preds = ap.predict(data)
# data = pd.read_csv("cleaned.csv")
data["cluster"] = ap_preds
#data = data.sort_values(by="cluster")

# data = data.dropna(axis=1)

# 2. t-SNE plot
tsne_comp = TSNE(n_components=2, perplexity=30, random_state=30, n_iter=1000).fit_transform(data)

tsne_df = pd.DataFrame(data=tsne_comp, columns=['t-SNE1', 't-SNE2'])
tsne_df.head()

tsne_df = pd.concat([tsne_df, pd.DataFrame({'cluster': ap_preds})], axis=1)
tsne_df['cluster']+=1
tsne_df["high-logp"] = ["yes" if x in [23, 24, 38, 30, 32, 8, 18, 34] else "not" for x in tsne_df['cluster']]
tsne_df.head()

text = []
for i in range (1, 31):
  text.append(str(i))
len(text)

plt.figure(figsize=(15, 15))
sns.set(font_scale=3)
z = sns.color_palette("coolwarm", as_cmap=True)
ax = sns.scatterplot(x="t-SNE1", y="t-SNE2", hue="high-logp", data=tsne_df, cmap='coolwarm')
#ax = sns.color_palette("mako", as_cmap=True)
x = tsne_df['t-SNE1']
y = tsne_df['t-SNE2']
# for i in range(0, 30):
#   plt.annotate(text[i], (x[i], y[i]+.7 ), size=10, color='black', weight='bold')
plt.title("Screening based on logP")
plt.legend(loc='upper left', borderaxespad=0, ncol=2)
ax.xaxis.set_label_coords(0.5, -0.1)
ax.yaxis.set_label_coords(-0.1, 0.5)
plt.subplots_adjust(top=0.9)

plt.show()