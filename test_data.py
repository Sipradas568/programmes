from openpyxl import load_workbook
import pytest
def load_excel(file,sheet):
    dictn = {}
   

    wb = load_workbook(file)
    lst = []
    sheet = wb[sheet]
    rows = sheet.max_row
    cols = sheet.max_column
    for i in range(1,rows+1):
        name = sheet.cell(i,1).value
        gender = sheet.cell(i,2).value
        dictn = {"name":name, "gender":gender}
        lst.append(dictn)



    return lst

file = r"C:\Users\10744603\OneDrive - LTIMindtree\Documents\testexcel.xlsx"
data = load_excel(file,"Sheet1")
@pytest.mark.parametrize("data,expected",[data,{}"sonia":"girl","rahul":"boy","sania":"girl"])
def test_excel(data,expected):
    assert data["name"] == expected[data["name"]]
q