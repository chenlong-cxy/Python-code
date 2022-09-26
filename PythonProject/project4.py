# 操作excel

import xlrd

# 1.打开xlsx文件
xlsx = xlrd.open_workbook('d:/Python环境/test.xlsx')
# 2.获取到指定的标签页
table = xlsx.sheet_by_index(0)
# 3.获取到表格中有多少行
nrows = table.nrows
# print(f'nrows = {nrows}')
# 4.进行循环统计操作
# for i in range(1, nrows):
#     print(table.cell_value(i, 0), end=' ')
#     print(table.cell_value(i, 1), end=' ')
#     print(table.cell_value(i, 2), end=' ')
#     print()
total = 0
count = 0
for i in range(1, nrows):
    classId = table.cell_value(i, 1)
    if classId == 100:
        total += table.cell_value(i, 2)
        count += 1
print(f'平均分: {total / count}')
