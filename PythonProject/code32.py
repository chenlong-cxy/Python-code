# 1.切片操作的基本使用
# a = [1, 2, 3, 4]
# print(a[1:3])  # [2, 3]

# 2.使用切片的时候省略边界
# a = [1, 2, 3, 4]
# print(a[1:])   # [2, 3, 4]
# print(a[:2])   # [1, 2]
# print(a[:-1])  # [1, 2, 3]
# print(a[:])    # [1, 2, 3, 4]
# 切片中的下标可以写成负数
# 注意: 切片操作底层无需拷贝, 非常高效

# 3.带有步长的切片操作
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# print(a[::1])  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# print(a[::2])     # [1, 3, 5, 7, 9]
# print(a[::3])     # [1, 4, 7, 0]
# print(a[1:-1:2])  # [2, 4, 6, 8]
#
# # 4.步长的数值可以是负数, 此时表示从后往前取数字
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# print(a[::-1])  # [0, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# print(a[::-2])  # [0, 8, 6, 4, 2]
#
# # 5.当切片中的下标超出有效范围后不会出现异常, 而是尽可能的把符合要求的元素给获取到
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(a[1:100])  # [2, 3, 4, 5, 6, 7, 8, 9, 0]
