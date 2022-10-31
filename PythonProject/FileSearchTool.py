# 实现文件查找工具
# 输入要查找的路径, 输入要搜索的文件名(一部分)
# 自动在指定的路径中进行查找
# import os

# inputPath = input('请输入要搜索的路径: ')
# pattern = input('请输入要搜索的关键字: ')

# for dirpath, _, filenames in os.walk(inputPath):
#     for f in filenames:
#         if pattern in f:
#             print(f'{dirpath}\\{f}')
#             # print(os.path.join(dirpath, f))

# for dirpath, dirnames, filenames in os.walk(inputPath):
#     print('-----------------------')
#     # 打印当前正在遍历的路径
#     print(f'所在路径: {dirpath}')
#     # 打印当前遍历路径下的目录名
#     print(f'目录: {dirnames}')
#     # 打印当前遍历路径下的文件名
#     print(f'文件: {filenames}')

# for i in os.walk(inputPath):
#     print(i)

import os

# print(os.path.join('xxx', 'yyy', 'zzz'))  # xxx\yyy\zzz

while True:
    inputPath = input('请输入要搜索的路径: ')
    pattern = input('请输入要搜索的关键字: ')

    for dirpath, dirnames, filenames in os.walk(inputPath):
        # 打印当前遍历路径下包含关键字的目录名
        for d in dirnames:
            if pattern in d:
                # print(f'{dirpath}\\{d}')
                print(os.path.join(dirpath, d))
        # 打印当前遍历路径下包含关键字的文件名
        for f in filenames:
            if pattern in f:
                # print(f'{dirpath}\\{f}')
                print(os.path.join(dirpath, f))


