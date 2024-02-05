import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.feature_selection import VarianceThreshold
from sklearn.preprocessing import StandardScaler
from pre import descriptors


atom_features = pd.read_csv('atom_features_PCA.csv')
bond_features = pd.read_csv('bond_features_PCA.csv')
data = pd.read_csv('global_features.csv')

#deal with global features
del data['descriptors'] #data.drop("", axis=1)

# seed(s)
sheader = []
smilesF = data.dropna(axis=1)

sheader = list(smilesF.columns.values)
scaler = StandardScaler()
data_scale = scaler.fit_transform(smilesF)

data_scale = data_scale.transpose()
scaled_data = pd.DataFrame(data_scale)

#deal with local features
atom_features = atom_features.add_prefix('A_')
bond_features = bond_features.add_prefix('B_')
n_col = bond_features.shape[1]
for i in range(0, n_col):
    i = str(i)
    column = 'B_' + i
    b1 = bond_features[column]

    name = column
    i = int(i)
    atom_features.insert(i, name, b1)

header_smilesf = []
header_smilesf = list(smilesF.columns.values)

# tf.random.set_seed(s)
# seed(s)
second_pca = PCA(n_components=50)
data_atom_pca = second_pca.fit_transform(atom_features)

pcaNames = []
for p in range(0, 50):
    pc = str(p)
    pca = 'PCA' + pc
    pcaNames.append(pca)

data_atom_pca = pd.DataFrame(data=data_atom_pca, columns=pcaNames)

j = 0
for col in pcaNames:
    col_data = data_atom_pca[col]
    scaled_data.insert(j, col, col_data)
    j = j + 1

sel = VarianceThreshold(0)
cleaned = sel.fit_transform(scaled_data)
cleaned = pd.DataFrame(cleaned, index=sheader)
cleaned.to_csv('cleaned.csv', index=False)
cleaned.to_csv('group.csv', index=True)
#cluster
# path_c = r"C:\Users\79403\Desktop\可透过中枢神经系统化合物库-HY-L028\data.xlsx"
# Atropine = "CN1[C@@H]2CC[C@H]1CC(C2)OC(=O)C(CO)C3=CC=CC=C3"
# sim = similarity(path, Atropine).sort_values(by='similarity', ascending=False)
# data, exception, Smiles = descriptors(path_c)
