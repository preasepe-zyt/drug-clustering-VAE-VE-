from pre import descriptors, lipinski
from localfeature import mol2local
import pandas as pd
from similarity import similarity_pic, similarity_list

data_qu = pd.read_csv("data_qu.csv")
Smiles = data_qu["Smiles"].values.tolist()
#local features
res, t = mol2local(Smiles, onehot=True, pca=True)
f_atoms_pca = pd.DataFrame(res.f_atoms_pca)
f_bonds_pca = pd.DataFrame(res.f_bonds_pca)
f_atoms_pca.to_csv('atom_features_PCA.csv', index=False)
f_bonds_pca.to_csv('bond_features_PCA.csv', index=False)
pd.DataFrame({"exception": t}).to_csv('exception.csv', index=False)
#global features
data, exception, Smiles = descriptors("data_qu.csv")
data.to_csv('global_features.csv', index=False)

# cluster_24 = pd.read_csv("cluster_24.csv")
# for i in range(cluster_24.shape[0]):
#     similarity_pic(cluster_24["smiles"][i], Atropine, cluster_24['Product Name'][i])
# data = similarity_list(path, Atropine)
# similarity_pic(mol, refmol)
# sim = similarity(path, Atropine).sort_values(by='similarity', ascending=False)

