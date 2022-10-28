# # 使用write来实现写文件操作
# f = open('d:/Python环境/test.txt', 'w')
# f.write('hello')
# f.close()

# # 写文件的时候需要使用w方式打开文件, 如果使用r方式打开则会抛异常
# f = open('d:/Python环境/test.txt', 'r')
# f.write('world')
# f.close()

# # 写方式打开有两种, 分别是直接写打开和追加写打开
# f = open('d:/Python环境/test.txt', 'w')
# f.write('1111\n')
# f.close()
#
# f = open('d:/Python环境/test.txt', 'w', encoding='utf8')
# f.write('2222')
# f.write('床前明月光')
# f.close()

# 如果文件对象已经被关闭, 那么意味着系统中和该文件相关的内存资源已经释放了, 强行去写就会出异常
# f = open('d:/Python环境/test.txt', 'x')
# f.write('hello')
# f.close()

# 床前明月光
# 疑是地上霜
# 举头望明月
# 低头思故乡

# # 第一次写入
# f = open('d:/Python环境/test.txt', 'w', encoding='utf8')
# f.write('2021')
# f.close()
# # 第二次写入
# f = open('d:/Python环境/test.txt', 'w', encoding='utf8')
# f.write('dragon')
# f.close()
# # 读取
# f = open('d:/Python环境/test.txt', 'r', encoding='utf8')
# print(f.read())  # dragon
# f.close()

# 第一次写入
f = open('d:/Python环境/test.txt', 'a', encoding='utf8')
f.write('2021')
f.close()
# 第二次写入
f = open('d:/Python环境/test.txt', 'a', encoding='utf8')
f.write('dragon')
f.close()
# 读取
f = open('d:/Python环境/test.txt', 'r', encoding='utf8')
print(f.read())  # 2021dragon
f.close()