from comtypes.client import CreateObject


def test_microsoft_excel():
    xl = CreateObject("Excel.Application")
    xl.Visible = True
    wb = xl.Workbooks.Add()
    sheet = wb.ActiveSheet
    sheet.Range["A1"].Value2 = "Test passed"
    wb.Close(SaveChanges = False)
    xl.Quit()
