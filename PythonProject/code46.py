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
# f = open('d:/Python环境/test.txt', 'a')
# f.write('2222')
# f.close()

# 如果文件对象已经被关闭, 那么意味着系统中和该文件相关的内存资源已经释放了, 强行去写就会出异常
f = open('d:/Python环境/test.txt', 'w')
f.close()
f.write('hello')