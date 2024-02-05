import os
import pandas as pd
folder_path = r'C:\Users\79403\Desktop\1.郑远腾分析用化合物库'

# 使用 os.listdir() 获取文件夹中的所有文件名
files = os.listdir(folder_path)
final_path = []
for i in files:
     path = folder_path+"\\"+i
     final_path.append(path)
     # print(final_path)


data = pd.DataFrame()
nu = []
col = ["Product Name", "Smiles"]
col2 = ["Product Name", "SMILES"]
smiles_cu = []
for i in final_path:
     data_c = pd.read_excel(i)
     print(i)
     if "Smiles" in data_c.columns:
          data_c = data_c[col].dropna()
          data = pd.concat([data_c, data], axis=0)
          nu.append(data_c.shape[0])
          print(data_c.shape)
     else:
          data_c = data_c[col2]
          data_c["Smiles"] = data_c["SMILES"]
          data = pd.concat([data_c, data], axis=0)
          nu.append(data_c.shape[0])
          print(data_c.shape)
print(nu)
print(data.shape)
summary = pd.DataFrame({"file": final_path,
                        "数量": nu})
len_hua = data.drop_duplicates(subset="Product Name")
print(len_hua)
summary.to_csv("data_14845.csv")
data.to_csv("data_all.csv")
len_hua.to_excel("data_qu.xlsx")
# filter = pd.DataFrame({"文件夹名": files,
#                        "化合物数量": nu})
# print(filter)
