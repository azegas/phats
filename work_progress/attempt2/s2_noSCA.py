import pandas as pd

df = pd.read_excel('output/3043210_s1_delete.xlsx', sheet_name='Sheet1')
# print(df)

# Replace sub string
df = df.replace('SCA', '', regex=True)
# print(df)

datatoexcel = pd.ExcelWriter('output/3043210_s2_noSCA.xlsx')

df.to_excel(datatoexcel)

datatoexcel.save()
