import pandas as pd
import numpy as np
from rdkit import Chem
from rdkit.Chem import Descriptors
from openbabel import openbabel, pybel
from rdkit.Chem import Draw

def image(smiles, path, data_c):
    mol = Chem.MolFromSmiles(smiles)
    img = Draw.MolToImage(mol)
    file_name = f"{[data_c.loc[data_c['Smiles'] == smiles, 'Product Name'].iloc[0]]}.png"
    print(path + "\\" + file_name)
    img.save(path + "\\" + file_name)

def property(path):
    data = pd.read_excel(path)
    col = ['Product Name', 'Target', 'Smiles', 'Research Area', 'Clinical Information']
    data_c = data[col]
    exceptions_df = pd.DataFrame(columns=['Product Name', 'Smiles'])
    merged_data = pd.DataFrame()
    Smiles = []
    # 转换 RDKit 分子对象为 Open Babel 分子对象
    ob_mol = openbabel.OBMol()
    for smiles in data_c['Smiles']:
        try:
            if isinstance(smiles, str):
                mol = Chem.MolFromSmiles(smiles)
                if mol is not None:
                   Smiles.append(smiles)
                   descriptors = Descriptors.CalcMolDescriptors(mol)
                   val = list(descriptors.values())
                   key = list(descriptors.keys())
                   name = data_c.loc[data_c['Smiles'] == smiles, 'Product Name'].values[0]
                   current = pd.DataFrame({name: val})
                   merged_data = pd.concat([current, merged_data], axis=1)
                   # mw = Descriptors.MolWt(mol)
                   # logp = Descriptors.MolLogP(mol)
                   # hbd = Descriptors.NumHDonors(mol)
                   # hba = Descriptors.NumHAcceptors(mol)
                   # lipinski_df = pd.DataFrame(
                   #      columns=['Smiles', 'Molecular Weight', 'CLogP', 'Hydrogen Bond Donors',
                   #               'Hydrogen Bond Acceptors'])
                   # 将结果添加到 DataFrame 中
                   # lipinski_df = lipinski_df.append({'Smiles': smiles,
                   #                                    'Molecular Weight': mw,
                   #                                    'CLogP': logp,
                   #                                    'Hydrogen Bond Donors': hbd,
                   #                                    'Hydrogen Bond Acceptors': hba}, ignore_index=True)
                   #merged_raw = pd.merge(lipinski_df, data_c[['Product Name', 'Smiles']], on='Smiles', how='inner')
                else:
                    ex_da = pd.DataFrame({'Product Name': [data_c.loc[data_c['Smiles'] == smiles, 'Product Name'].values[0]],
                                          'Smiles': [smiles]})
                    exceptions_df = exceptions_df.append(ex_da, ignore_index=True)
        except Chem.MolSanitizeException as e:
            print("无效的 SMILES 表达式")
    descriptors_name = pd.DataFrame({"descriptors": key})
    merged_data = pd.concat([descriptors_name, merged_data], axis=1)
    return merged_data, exceptions_df, Smiles