import openpyxl


def excelread(name):
    wb = openpyxl.load_workbook(name)
    sheet = wb.active
    tormv = []
    i = 1
    while i <= sheet.max_row:
        rb = 'B' + str(i)
        ra = 'A' + str(i)
        if sheet[rb].value in ["Remove", "remove"]:
            tormv.append(sheet[ra].value)
        i += 1
    return tormv
