# a = 10
# b = 20
# c = 30
#
# print(a < b < c) # print(a < b and b < c)
# print(a < b and b > c)
# print(a > b > c) # print(a > b and b > c)
#
# print(a < b or b > c)
# print(a > b or b > c)
#
# print(not a > b)
# print(not a < b)

# 短路求值
a = 10
b = 20
print(a > b and 10 / 0)
print(a < b or 10 / 0)