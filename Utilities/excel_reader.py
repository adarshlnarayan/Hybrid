import openpyxl

def read_login_data(file_path,sheetno):
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook[sheetno]
    rows = sheet.max_row
    data = []
    for r in range(2,rows+1):
        un = sheet.cell(r,1).value
        pwd = sheet.cell(r,2).value
        data.append([un,pwd])
    return data
