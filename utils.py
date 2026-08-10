import openpyxl

def row_count(file,sheetname):

    wb = openpyxl.load_workbook(file)
    sheet = wb[sheetname]
    no_rows = sheet.max_row
    return no_rows


def col_count(file,sheetname):
    wb = openpyxl.load_workbook(file)
    sheet = wb[sheetname]
    no_cols = sheet.max_column
    return no_cols

def read_data(file,sheetname,r,c):
    wb = openpyxl.load_workbook(file)
    sheet = wb[sheetname]
    return sheet.cell(r,c).value
   
def scroll_ele(driver,ele):
    driver.execute_script("arguments[0].scrollIntoView();", ele)
   


