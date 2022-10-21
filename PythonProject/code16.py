# # 链式赋值
# a = b = 10
# print(a)
# print(b)
#
# # 多元赋值(交换变量，一个函数返回多个值)
# a, b = 10, 20
# print(a)
# print(b)

# 交换a和b
a = 10
b = 20

# tmp = a
# a = b
# b = tmp
# print(a)
# print(b)

a, b = b, a
print(a, b)
x = y = 10
print(x)
print(y)
a, b = 10, 20
print(a)  # 10
print(b)  # 20

a, b = 10, 20
a, b = b, a
print(a)  # 20
print(b)  # 10
