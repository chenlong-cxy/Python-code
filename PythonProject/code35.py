# 1.使用in判定某个元素是否在列表中存在
a = [1, 2, 3, 4]
print(1 in a)
print(10 in a)
print(1 not in a)
print(10 not in a)

# 2.使用index方法判定当前元素在列表中的位置，得到一个下标
a = [1, 2, 3, 4]
print(a.index(3))
# print(a.index(10)) # 不存在, 抛异常