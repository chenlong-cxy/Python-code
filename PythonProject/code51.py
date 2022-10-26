# a = set()
# print(type(a))  # <class 'set'>
# print(a)        # set()
# a = {}
# print(type(a))  # <class 'dict'>
# print(a)        # {}
# a = {1, 2, 3, 4, 5}
# print(type(a))  # <class 'set'>
# print(a)        # {1, 2, 3, 4, 5}
# a = {2021, 'dragon'}
# print(type(a))  # <class 'set'>
# print(a)        # {'dargon', 2021}

# a = {1, 2, 3, 4}
# a.add(5)
# print(a)  # {1, 2, 3, 4, 5}
#
# a = {1, 2, 3, 4}
# # a.update([5, 6, 7, 8])
# a.update('hello')
# a.update({'name': 'Lee'})
# print(a)  # {1, 2, 3, 4, 5, 6, 7, 8}

# a = {1, 2, 3, 4}
# a.remove(2)
# # a.remove(5)  # 不存在,抛异常
# print(a)  # {1, 3, 4}
#
# a = {1, 2, 3, 4}
# a.discard(2)
# a.discard(5)  # 不存在,但不会抛异常
# print(a)  # {1, 3, 4}
#
# a = {1, 2, 3, 4}
# a.pop()
# print(a)  # {2, 3, 4}

# a = {1, 2, 3, 4}
# print(1 in a)       # True
# print(10 in a)      # False
# print(1 not in a)   # False
# print(10 not in a)  # True

# a = {1, 2, 3, 4}
# del a
# print(a)  # 抛异常: name 'a' is not defined

# a = {1, 2, 3, 4}
# for elem in a:
#     print(elem)

# a = {1, 2, 3}
# b = {4, 5, 6}
# c = a.union(b)
# print(a)  # {1, 2, 3}
# print(b)  # {4, 5, 6}
# print(c)  # {1, 2, 3, 4, 5, 6}

# a = {1, 2, 3}
# b = {4, 5, 6}
# a.update(b)
# print(a)  # {1, 2, 3, 4, 5, 6}
# print(b)  # {4, 5, 6}

# a = {1, 2, 3}
# b = {2, 3, 4}
# c = a.difference(b)
# print(a)
# print(b)
# print(c)

# a = {1, 2, 3}
# b = {2, 3, 4}
# a.difference_update(b)
# print(a)
# print(b)

# a = {1, 2, 3}
# b = {2, 3, 4}
# c = a.intersection(b)
# print(a)
# print(b)
# print(c)

# a = {1, 2, 3}
# b = {2, 3, 4}
# c = a.intersection_update(b)
# print(a)
# print(b)

# a = {1, 2, 3}
# b = {2, 3, 4}
# c = a.isdisjoint(b)
# print(a)
# print(b)
# print(c)

# a = {2, 3}
# b = {2, 3, 4}
# c = a.issubset(b)
# print(a)
# print(b)
# print(c)

# a = {1, 2, 3, 4}
# b = {2, 3, 4}
# c = a.issuperset(b)
# print(a)
# print(b)
# print(c)

# a = {1, 2, 3, 5}
# b = {2, 3, 4, 1}
# c = a.symmetric_difference(b)
# print(a)
# print(b)
# print(c)

a = {1, 2, 3}
b = {2, 3, 4}
a.symmetric_difference_update(b)
print(a)
print(b)
