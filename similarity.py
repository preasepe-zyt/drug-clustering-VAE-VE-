from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem import DataStructs
import pandas as pd
from rdkit.Chem import Draw
from rdkit.Chem.Draw import SimilarityMaps
import matplotlib.pyplot as plt
import numpy as np

# 计算Tanimoto相似性
def similarity_list(path, remol):
    mol_Atropine = Chem.MolFromSmiles(remol[0])
    data = pd.read_csv(path)
    col = ['Product Name', 'Smiles']
    # col = ['Product Name', 'Smiles', 'chinese name']
    data_c = data[col]
    final_similarity = pd.DataFrame(columns=['Product Name', "similarity"])
    for smiles in data_c['Smiles']:
        try:
            if isinstance(smiles, str):
                mol = Chem.MolFromSmiles(smiles)
                if mol is not None:
                    fp_1 = AllChem.GetMorganFingerprintAsBitVect(mol, 2)  # 2是半径，可以调整
                    fp_2 = AllChem.GetMorganFingerprintAsBitVect(mol_Atropine, 2)
                    # 计算Tanimoto相似性
                    similarity = DataStructs.TanimotoSimilarity(fp_1, fp_2)
                    name = data_c.loc[data_c['Smiles'] == smiles, 'Product Name'].values[0]
                    row_data = {'Product Name': name +"-"+remol[1], 'similarity': similarity}
                    final_similarity = final_similarity.append(row_data, ignore_index=True)
        except Exception as e:
            print(f"无效的 SMILES 表达式{e}")
    return final_similarity


def similarity_pic(x, remol, name):
    path = r"C:\Users\79403\Desktop\药物筛选\similarity"
    # 创建分子对象
    mol = Chem.MolFromSmiles(x)
    refmol = Chem.MolFromSmiles(remol[0])

    # 获取Morgan指纹
    fp_mol = SimilarityMaps.GetMorganFingerprint(mol, fpType='bv')
    fp_refmol = SimilarityMaps.GetMorganFingerprint(refmol, fpType='bv')
    # 生成相似性图
    fig, maxweight = SimilarityMaps.GetSimilarityMapForFingerprint(refmol, mol,
                                                                   SimilarityMaps.GetMorganFingerprint)
    fig.savefig(path+"\\"+name+".png", dpi=300, bbox_inches='tight')
    # 在PyCharm窗口中显示图片
    # figManager = plt.get_current_fig_manager()
    # figManager.window.move(25, 100)  # 请根据需要调整窗口位置

if __name__ == "__main__":
    name_drug = ["Donepezil", "Galantamine", "Rivastigmine", "Memantine"]
    smiles_drug = ["COC1=C(C=C2C(=C1)CC(C2=O)CC3CCN(CC3)CC4=CC=CC=C4)OC", "CN1CC[C@@]23C=C[C@@H](C[C@@H]2OC4=C(C=CC(=C34)C1)OC)O",
                   "CCN(C)C(=O)OC1=CC=CC(=C1)[C@H](C)N(C)C","CC12CC3CC(C1)(CC(C3)(C2)N)C"]
    path = r"C:\Users\79403\Desktop\可透过中枢神经系统化合物库-HY-L028\data.xlsx"
    # data = similarity_list(path, Carbamazepine)
    # print(data)
    # for i in range(f.shape[0]):
    #     similarity_pic(f["smiles"][i], Carbamazepine)