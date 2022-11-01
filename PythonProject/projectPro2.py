# 操作excel

import xlrd

# # 1.打开xlsx文件
# xlsx = xlrd.open_workbook('d:/Python环境/test.xlsx')
# # 2.获取到指定的标签页
# # table = xlsx.sheets()[0]
# # table = xlsx.sheet_by_index(0)
# table = xlsx.sheet_by_name('Sheet1')
# # table = xlsx.sheet_names()[0]  # 'str' object has no attribute 'nrows'
# # 3.获取到表格中有多少行

# # print(f'nrows = {nrows}')
# # 4.进行循环统计操作
# for i in range(0, nrows):
#     print(table.cell_value(i, 0), sep='\t', end=' ')
#     print(table.cell_value(i, 1), sep='\t', end=' ')
#     print(table.cell_value(i, 2), sep='\t', end=' ')
#     print(table.cell_value(i, 3), sep='\t', end=' ')
#     print(table.cell_value(i, 4), sep='\t', end=' ')
#     print()
# total = 0
# count = 0
# for i in range(1, nrows):
#     classId = table.cell_value(i, 1)
#     if classId == 100:
#         total += table.cell_value(i, 2)
#         count += 1
# print(f'平均分: {total / count}')

# import xlrd
# import os

# 打开Excel文件读取
# data = xlrd.open_workbook('D:/github/Python-code/PythonProject/data.xls', formatting_info=True)
# data = xlrd.open_workbook('D:/github/Python-code/PythonProject/test.xlsx')


# file_path = os.path.dirname(os.path.abspath(__file__))
# base_path = os.path.join(file_path, 'test.xlsx')
# data = xlrd.open_workbook(base_path)
# print(base_path)

# 获取指定工作表
# table = data.sheets()[0]  # 获取Sheet1工作表
# table = data.sheet_by_index(0)  # 获取Sheet1工作表
# table = data.sheet_by_name('Sheet1')  # 获取Sheet1工作表

# print(data.sheet_names())  # ['Sheet1', 'Sheet2', 'Sheet3']
# print(data.sheet_loaded(0))         # 检查Sheet1工作表是否导入完毕
# print(data.sheet_loaded('Sheet1'))  # 检查Sheet1工作表是否导入完毕

# 操作指定行
# nrows = table.nrows  # 获取工作表中的行数
# print(nrows)
# print(table.row(0))  # 获取第0行中所有单元格对象组成的列表
# print(table.row_slice(0, start_colx=0, end_colx=None))  # 获取第0行中所有单元格对象组成的列表
# print(table.row_types(1, start_colx=0, end_colx=None))  # 获取第0行中所有单元格的数据类型组成的列表
# print(table.row_values(0, start_colx=0, end_colx=None))  # 获取第0行中所有单元格的数据组成的列表
# print(table.row_len(0))  # 获取第0行中有效单元格的个数

# 操作指定列
# ncols = table.ncols  # 获取工作表中的列数
# print(ncols)
# print(table.col(0))  # 获取第0列中所有单元格对象组成的列表
# print(table.col_slice(0, start_rowx=0, end_rowx=None))  # 获取第0列中所有单元格对象组成的列表
# print(table.col_types(0, start_rowx=0, end_rowx=None))  # 获取第0列中所有单元格的数据类型组成的列表
# print(table.col_values(0, start_rowx=0, end_rowx=None))  # 获取第0列中所有单元格的数据组成的列表

# 操作指定单元格
# print(table.cell(0, 1))  # 获取第0行第1列的单元格对象
# print(table.cell_type(0, 1))  # 获取第0行第1列单元格的数据类型
# print(table.cell_value(0, 1))  # 获取第0行第1列的单元格中的数据

import xlrd
import os

# 1.打开Excel文件读取
file_path = os.path.dirname(os.path.abspath(__file__))
base_path = os.path.join(file_path, 'test.xlsx')
data = xlrd.open_workbook(base_path)

# 2.获取指定工作表
table = data.sheet_by_index(0)

# 3.求3班数学成绩平均分
nrows = table.nrows  # 获取行数
total = 0
count = 0
for i in range(1, nrows):  # 遍历每一行,统计3班人数和数学成绩总和
    if table.cell_value(i, 1) == 3:
        total += table.cell_value(i, 3)
        count += 1
print(f'3班数学成绩平均分={total/count}')  # 3班数学成绩平均分=118.0
