# # 1.创建元组
# a = ()
# b = tuple()
# print(type(a))
# print(type(b))
#
# # 2.创建元组的时候, 指定初始值
# a = (1, 2, 3, 4)
# print(a)
#
# # 3.元组中的元素也可以是任意类型的
# a = (1, 'hello', True, [])
# print(a)
#
# # 4.通过下标访问元组中的元素
# a = (1, 2, 3, 4)
# print(a[1])
# print(a[-1])
# # print(a[100])  # error
#
# # 5.通过切片来获取元组中的一个部分
# a = (1, 2, 3, 4)
# print(a[1:3])
# print(a[1:])
# print(a[:-1])
# print(a[:])
# print(a[::2])
# print(a[::-1])
# print(a[::-2])

# # 6.使用for循环等方式遍历元组元素
# a = (1, 2, 3, 4)
# for elem in a:
#     print(elem)
# for i in range(0, len(a)):
#     print(a[i])
# i = 0
# while i < len(a):
#     print(a[i])
#     i += 1

# # 7.使用in和in not判定元素是否存在, 使用index查找元素的下标
# a = (1, 2, 3, 4)
# print(1 in a)
# print(10 in a)
# print(1 not in a)
# print(10 not in a)
# print(a.index(2))

# # 8.使用+来拼接两个元组
# a = (1, 2, 3, 4)
# b = (5, 6, 7, 8)
# c = a + b
# print(a)
# print(b)
# print(c)

# # 9.元组只支持“读”操作, 不支持“修改”这类操作
# a = (1, 2, 3, 4)
# b = (5, 6, 7, 8)
# # a[0] = 100
# # a.appen(5)
# # a.pop()
# # a.extend(b)

# 10.当进行多元赋值的时候, 其实本质上是按照元组的方式来进行工作的
def getPoint():
    x = 10
    y = 20
    return x, y


a, b = getPoint()
print(type(getPoint()))
c = getPoint()
print(type(c))