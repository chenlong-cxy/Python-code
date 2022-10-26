# # 1.创建元组
# a = ()
# b = tuple()
# print(a)  # ()
# print(b)  # ()
#
# # 2.创建元组的时候, 指定初始值
# a = (1, 2, 3, 4, 5)
# print(a)  # (1, 2, 3, 4, 5)
#
# # 3.元组中的元素也可以是任意类型的
# a = (1, 'hello', True, [4, 5, 6])
# print(a)  # (1, 'hello', True, [4, 5, 6])
#
# a = (1, 2, 3, 4)
# print(1 in a)       # True
# print(10 in a)      # False
# print(1 not in a)   # False
# print(10 not in a)  # True

# a = (1, 2, 3, 4)
# print(a.index(3))  # 2
# print(a.index(10))  # 不存在,抛异常

# # 4.通过下标访问元组中的元素
# a = (1, 2, 3, 4)
# print(a[2])  # 3
#
# print(a[-1])  # 4
# print(a[100])  # error
#
# # 5.通过切片来获取元组中的一个部分
# a = (1, 2, 3, 4)
# print(a[1:3])  # (2, 3)
# print(a[1:])   # (2, 3, 4)
# print(a[:2])   # (1, 2)
# print(a[:-1])  # (1, 2, 3)
# print(a[::])   # (1, 2, 3, 4)
# print(a[::-1])
# print(a[::-2])
# a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
# print(a[::1])     # (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
# print(a[::2])     # (1, 3, 5, 7, 9)
# print(a[::3])     # (1, 4, 7, 0)
# print(a[1:-1:2])  # (2, 4, 6, 8)
# print(a[::-1])  # (0, 9, 8, 7, 6, 5, 4, 3, 2, 1)
# print(a[::-2])  # (0, 8, 6, 4, 2)
# print(a[1:100])  # (2, 3, 4, 5, 6, 7, 8, 9, 0)

# # 6.使用for循环等方式遍历元组元素
# a = (1, 2, 3, 4)
# # 方式一
# for elem in a:
#     print(elem)
#
# # 方式二
# for i in range(len(a)):
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

# 8.使用+来拼接两个元组
# a = (1, 2, 3)
# b = (4, 5, 6)
# c = a + b
# print(a)  # (1, 2, 3)
# print(b)  # (4, 5, 6)
# print(c)  # (1, 2, 3, 4, 5, 6)
# a.extend(b)  # 不存在
# a = (1, 2, 3)
# b = (4, 5, 6)
# a += b
# print(a)  # (1, 2, 3, 4, 5, 6)
# print(b)  # (4, 5, 6)

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
print(type(a))
print(type(b))
print(type(getPoint()))
c = getPoint()
print(type(c))

# a = (1, 2, 3, 4, 1)
# print(a.count(1))
# print(a)

# a = (1, 2, 3, 4)
# tmp = list(a)   # 将元组转换成列表
# tmp[0] = 10     # 更改列表
# a = tuple(tmp)  # 将列表转换回元组
# print(a)        # (10, 2, 3, 4)
