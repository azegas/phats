import pandas as pd

# exportas to .txt
# https://www.youtube.com/watch?v=M5b669dAm2g
xl = pd.ExcelFile('output/3043210_s3_merge.xlsx')
xl.sheet_names

for sheet in xl.sheet_names:
    file = pd.read_excel(xl, sheet_name=sheet)
    file.to_csv('output/3043210_s4_totxt.txt', header=True, index=False)
