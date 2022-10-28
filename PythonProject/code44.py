# 使用open打开一个文件
# f = open(file, mode, encoding)
f = open('d:/Python环境/test.txt', 'r', encoding='utf-8')
print(f)
print(type(f))

f.close()

