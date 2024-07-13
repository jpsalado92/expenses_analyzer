import xlrd  # type: ignore

book = xlrd.open_workbook("myfile.xls")
print(f"The number of worksheets is {book.nsheets}")
print(f"Worksheet name(s): {book.sheet_names()}")
sh = book.sheet_by_index(0)
print(f"{sh.name} {sh.nrows} {sh.ncols}")
print(f"Cell D30 is {sh.cell_value(rowx=29, colx=3)}")
for rx in range(sh.nrows):
    print(sh.row(rx))
