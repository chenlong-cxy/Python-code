# # 打印1-10
# for i in range(1, 11):
#     print(i)
# # range(begin, end)->[begin, end)前闭后开

# 打印2，4，6，8，10
# for i in range(2, 12, 2):
#     print(i)
# # range(begin, end, len)->len表示步长，默认的步长为1

# 打印10-1
# for i in range(10, 0, -1):
#     print(i)

# 求1-100的和
theSum = 0
for i in range(1, 101):
    theSum += i
print(f'sum = {theSum}')
# 有一个内建函数叫做sum，我们定义的变量名与内建函数名冲突了
# 虽然不影响程序运行，但是后面就无法使用内建函数sum了