# pip install xlrd3
import xlrd3 as xlrd

my_dict = {}
book = xlrd.open_workbook("Test.xls")
# print("The number of worksheets is {0}".format(book.nsheets))
# print("Worksheet name(s): {0}".format(book.sheet_names()))
sh = book.sheet_by_index(0)
# print("{0} {1} {2}".format(sh.name, sh.nrows, sh.ncols))
# print("Cell D30 is {0}".format(sh.cell_value(rowx=7, colx=1)))
for rx in range(sh.nrows):
    # print(sh.row(rx))
    if sh.row_values(rx)[1]:
        if isinstance(sh.row_values(rx)[1], float) and sh.row_values(rx)[0] != "Итого:":
            # print(sh.row_values(rx))
            my_dict[sh.row_values(rx)[0]] = sh.row_values(rx)[1]

print(my_dict)
min_val = min(my_dict.values())
max_val = max(my_dict.values())

max_val_dict = [i for i in my_dict if my_dict[i] == max_val]
min_val_dict = [i for i in my_dict if my_dict[i] == min_val]

print(f"Max dict {max_val_dict[0]}: {my_dict[max_val_dict[0]]}")
print(f"Min dict {min_val_dict[0]}: {my_dict[min_val_dict[0]]}")