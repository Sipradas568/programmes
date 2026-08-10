import openpyxl

def no_rows(file,sheet):

    wb = openpyxl.load_workbook(file)
    sheet = wb[sheet]
    rows = sheet.max_row
    return rows

def no_cols(file,sheet):
    wb = openpyxl.load_workbook(file)
    sheet = wb[sheet]
    cols = sheet.max_column
    return cols



def read_data(file,sheet,r,c):
    wb = openpyxl.load_workbook(file)
    sheet = wb[sheet]
    return sheet.cell(r,c).value