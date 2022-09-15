# def test():
#     return 1
#     return 2


# def isOdd(num):
#     """
#     用来判定num是不是奇数，如果是就返回True，否则返回False
#     :param num: 要判定的整数
#     :return: 返回True和False来表示是不是奇数
#     """
#     if num % 2 == 0:
#         return False
#     else:
#         return True
#
#
# print(isOdd(2))
# print(isOdd(3))


# Python函数可以一次返回多个值
def getSumAndDif(x, y):
    return x + y, x - y


a = 10
b = 20
sum, dif = getSumAndDif(a, b)
print(f'{a} + {b} = {sum}, {a} - {b} = {dif}')
# 如果只想使用一部分，不关注其他的，可以用_进行占位
_, dif = getSumAndDif(1, 2)
print(dif)