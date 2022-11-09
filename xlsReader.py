import openpyxl
import os

def readExcel() -> openpyxl.Workbook:
    try:
        wb = openpyxl.load_workbook(os.getcwd()+"/dryou.xlsx")
        #print(type(sheet[0]))
        return wb
    except:
        print("No such file: "+os.getcwd())

if __name__ == "__main__":
    wb = readExcel()
    print(wb)