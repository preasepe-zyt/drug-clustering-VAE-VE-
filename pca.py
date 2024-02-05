import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn import datasets

data = pd.read_excel(r"C:\Users\79403\Desktop\RNA-seq LGY.xlsx", sheet_name="Counts")
data = data.iloc[:, range(10, 36)]
data = data.drop(data.iloc[1,:])


y = np.repeat(["1-3", "4-6", "7-9", "10-12", "1-1", "1-2",
               "1-3", "2-1", "2-2", "2-3", "3-1", "3-2",
               "3-3", "201047A_BAL_4_1", "201047A_BAL_5_1", "201047A_BAL_6_1"], 3)

matplotlib.rcParams['font.family'] = 'Arial'
# 创建PCA对象，指定要保留的主成分数量
pca = PCA(n_components=2)
# 对数据进行PCA转换
X_pca = pca.fit_transform(data.transpose())
# 绘制PCA结果
fig = plt.figure(figsize=(10, 10))
plt.scatter(X_pca[:, 0], X_pca[:, 1], s=80, c=data.columns)
# for i in range(0, 26):
#     plt.text(X_pca[i, 0], X_pca[i, 1], f'{y[i]}', fontsize=11, ha='left', va='bottom', color='black')
plt.title('PCA of RNA-seq LGY', fontsize=20)
plt.xlabel('Principal Component 1', fontsize=20)
plt.ylabel('Principal Component 2', fontsize=20)
plt.tick_params(axis='both', labelsize=20)
# plt.colorbar(label='Class')  # 添加颜色标签
plt.legend(loc='upper right', bbox_to_anchor=(1.05, 1), frameon=False)
plt.show()
fig.savefig("PCA of RNA-seq LGY.png", dpi=300)

