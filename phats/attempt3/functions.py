from openpyxl import Workbook, load_workbook
import pandas as pd
import os


def delete_cols_rows():
    wb = load_workbook('sourcefiles/3043210.xlsx')
    ws = wb['Sheet1']
    # print_rows()
    ws.delete_cols(1, 1)
    ws.delete_rows(1, 5)
    # print_rows()

    wb.save('output/3043210_s1_delete.xlsx')


def no_sca():
    df = pd.read_excel('output/3043210_s1_delete.xlsx', sheet_name='Sheet1')
    # print(df)
    # Replace sub string
    df = df.replace('SCA', '', regex=True)
    # print(df)
    datatoexcel = pd.ExcelWriter('output/3043210_s2_noSCA.xlsx')
    df.to_excel(datatoexcel)
    datatoexcel.save()

    os.remove('output/3043210_s1_delete.xlsx')


def merge():
    wb = load_workbook('output/3043210_s2_noSCA.xlsx')
    ws = wb['Sheet1']
    # print_rows()

    ws.delete_cols(1, 1)
    ws.delete_rows(1, 1)
    # print_rows()

    wb.save('output/3043210_s3_merge.xlsx')
    
    os.remove('output/3043210_s2_noSCA.xlsx')


def convert_to_txt():
    # exportas to .txt
    # https://www.youtube.com/watch?v=M5b669dAm2g
    xl = pd.ExcelFile('output/3043210_s3_merge.xlsx')
    xl.sheet_names

    for sheet in xl.sheet_names:
        file = pd.read_excel(xl, sheet_name=sheet)
        file.to_csv('output/3043210_s4_totxt.txt', header=True, index=False)

    os.remove('output/3043210_s3_merge.xlsx')


def istrink_bruksniukus():
    file = open('output/3043210_s4_totxt.txt')
    contents = file.read()
    # print(contents)
    replaced_contents = contents.replace(',', '_')
    # print(replaced_contents)

    with open('output/3043210_s5_find_replace.txt', "w") as f:
        for i in replaced_contents:
            f.write(i)

    os.remove('output/3043210_s4_totxt.txt')            


def delete_trash():
    # Karina
    # https://www.csnewbs.com/python-10c-remove-edit-lines

    with open("output/3043210_s5_find_replace.txt", "r") as file:
        lines = file.readlines()
    with open('sourcefiles/3043210_siuksles.txt', 'r') as file:
        to_delete = file.read().splitlines()

    file = open("output/3043210_s5_find_replace.txt", "w")
    for line in lines:
        if line.rstrip() not in to_delete:
            file.write(line)
            # print(line, "liko po pravalymo")
    file.close()
