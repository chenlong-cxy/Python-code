# # 1.使用read读取文件内容, 指定读几个字符
# f = open('d:/Python环境/test.txt', 'r', encoding='utf8')
# result = f.read(2)
# print(result)
# f.close()

# # 2.更常见的需求是按行进行读取
# f = open('d:/Python环境/test.txt', 'r', encoding='utf8')
# for line in f:
#     print(f'line = {line}', end='')
# f.close()

# 3.使用readlines方法直接把整个文件所有内容都读取出来, 按照行组织到一个列表里
f = open('d:/Python环境/test.txt', 'r', encoding='utf8')
lines = f.readlines()
print(lines)
f.close()