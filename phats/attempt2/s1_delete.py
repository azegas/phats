from openpyxl import Workbook, load_workbook

wb = load_workbook('sourcefiles/3043210.xlsx')
ws = wb['Sheet1']
# print_rows()
ws.delete_cols(1, 1)
ws.delete_rows(1, 5)
# print_rows()

wb.save('output/3043210_s1_delete.xlsx')
