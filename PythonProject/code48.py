# 使用上下文管理器, 避免忘记关闭文件
# def func():
#     with open('d:/Python环境/test.txt', 'r', encoding='utf8') as f:
#         result = f.read(2)
#         print(result)
#
#
# func()

with open('d:/Python环境/test.txt', 'r', encoding='utf-8') as f:
    line = f.readline()
    print(line)

