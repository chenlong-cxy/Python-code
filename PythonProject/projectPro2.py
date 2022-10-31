# 操作excel

import xlrd

# 1.打开xlsx文件
xlsx = xlrd.open_workbook('d:/Python环境/test.xlsx')
# 2.获取到指定的标签页
# table = xlsx.sheets()[0]
# table = xlsx.sheet_by_index(0)
table = xlsx.sheet_by_name('Sheet1')
# table = xlsx.sheet_names()[0]  # 'str' object has no attribute 'nrows'
# 3.获取到表格中有多少行
nrows = table.nrows
# print(f'nrows = {nrows}')
# 4.进行循环统计操作
for i in range(0, nrows):
    print(table.cell_value(i, 0), sep='\t', end=' ')
    print(table.cell_value(i, 1), sep='\t', end=' ')
    print(table.cell_value(i, 2), sep='\t', end=' ')
    print(table.cell_value(i, 3), sep='\t', end=' ')
    print(table.cell_value(i, 4), sep='\t', end=' ')
    print()
# total = 0
# count = 0
# for i in range(1, nrows):
#     classId = table.cell_value(i, 1)
#     if classId == 100:
#         total += table.cell_value(i, 2)
#         count += 1
# print(f'平均分: {total / count}')

import xlrd
import os

# data = xlrd.open_workbook('D:/Python环境/test.xlsx')

# file_path = os.path.dirname(os.path.abspath(__file__))
# base_path = os.path.join(file_path, 'test.xlsx')
# data = xlrd.open_workbook(base_path)

# data = xlrd.open_workbook('D:/Python环境/test.xlsx')
#
# table = data.sheets()[0]
# table = data.sheet_by_index(0)
# table = data.sheet_by_name('Sheet1')

# print(data.sheet_names())  # ['Sheet1', 'Sheet2', 'Sheet3']
# print(data.sheet_loaded(0))
# print(data.sheet_loaded('Sheet1'))