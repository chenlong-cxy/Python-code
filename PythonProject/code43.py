# 使用hash函数能够计算出一个变量的哈希值
print(hash(0))
print(hash(3.14))
print(hash('hello'))
print(hash('a'))
print(hash(True))
print(hash((1, 2, 3)))

# 有的类型是不能计算哈希值的
# print(hash([1, 2, 3]))
# print(hash({}))

a = {
    1: 2,
    'xxx': 'yyy',
    1.1: 2.2
}
print(a)  # {1: 2, 'xxx': 'yyy', 1.1: 2.2}

print(hash(0))         # 0
print(hash(3.14))      # 322818021289917443
print(hash('dragon'))  # -2549621489818607633
print(hash((1, 2)))    # -3550055125485641917
# print(hash([1, 2]))                       # 列表不可哈希,抛异常
# print(hash({1, 2}))                       # 集合不可哈希,抛异常
# print(hash({'id': 1, 'name': 'dargon'}))  # 字典不可哈希,抛异常
