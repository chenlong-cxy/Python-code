# # 1.使用for循环遍历列表
# a = [1, 2, 3, 4]
# for elem in a:
#     # print(elem)
#     # elem = elem + 10  # 不会影响列表中的元素值
# print(a)

# # 2.使用for循环遍历列表, 使用下标的方式
# a = [1, 2, 3, 4]
# for i in range(len(a)):
#     # print(a[i])
#     a[i] = a[i] + 10
# print(a)

# 3.使用while循环, 通过下标遍历
a = [1, 2, 3, 4]
i = 0
while i < len(a):
    print(a[i])
    i += 1