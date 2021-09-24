import openpyxl, os

os.chdir('C:\\Users\\ranan\\main\\code\\Py')

wb = openpyxl.Workbook()
sheet = wb.get_sheet_by_name('Sheet')

sheet['A1'] = 42

wb.save('example2.xlsx')

