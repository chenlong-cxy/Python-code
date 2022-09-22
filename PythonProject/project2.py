# 实现文件查找工具
# 输入要查找的路径, 输入要搜索的文件名(一部分)
# 自动在指定的路径中进行查找
import os

inputPath = input('请输入要搜索的路径: ')
pattern = input('请输入要搜索的关键字: ')

for dirpath, _, filenames in os.walk(inputPath):
    for f in filenames:
        if pattern in f:
            print(f'{dirpath}/{f}')
            # print(os.path.join(dirpath, f))

# for dirpath, dirnames, filenames in os.walk(inputPath):
#     print('-------------------')
#     print(f'dirpath = {dirpath}')
#     print('dirnames:')
#     for dirname in dirnames:
#         print(dirname)
#     print('filenames:')
#     for filename in filenames:
#         print(filename)

# for i in os.walk(inputPath):
#     print(i)
