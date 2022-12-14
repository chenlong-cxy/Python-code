# 1.使用+针对两个列表进行拼接
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(a)  # [1, 2, 3]
print(b)  # [4, 5, 6]
print(c)  # [1, 2, 3, 4, 5, 6]

# 2.使用extend来进行拼接
a = [1, 2, 3]
b = [4, 5, 6]
c = a.extend(b)
print(a)  # [1, 2, 3, 4, 5, 6]
print(b)  # [4, 5, 6]
print(c) # None:这是一个特殊的变量值, 表示“啥都没有”, 因为extend其实是没有返回值的

# 3.使用+=来进行拼接
a = [1, 2, 3]
b = [4, 5, 6]
a += b  # extend更高效
print(a)  # [1, 2, 3, 4, 5, 6]
print(b)  # [4, 5, 6]

a = [1, 2, 3]
a.extend(range(3))
print(a)