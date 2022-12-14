# 1.使用pop删除列表中最末尾的元素
a = [1, 2, 3, 4]
a.pop()
print(a)  # [1, 2, 3]

# 2.使用pop删除任意位置的元素
a = [1, 2, 3, 4]
a.pop(1)
print(a)  # [1, 3, 4]

# 3.使用remove方法按照值进行删除
a = [1, 2, 3, 4]
a.remove(1)
print(a)  # [2, 3, 4]

a = [1, 2, 3, 4, 1]
a.remove(1)
print(a)  # [2, 3, 4, 1]
