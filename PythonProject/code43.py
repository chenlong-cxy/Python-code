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