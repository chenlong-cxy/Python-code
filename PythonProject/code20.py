# 输入一个整数，判断是否是奇数
# a = input('请输入一个整数: ')
# a = int(a)
# a = int(input('请输入一个整数: '))
#
# # C++和Java中负数模2等于-1，但Python中可以
# if a % 2 == 1:
#     print('这是一个奇数')
# else:
#     print('这是一个偶数')

# 输入一个整数，判断是正数还是负数
# a = int(input('请输入一个整数: '))
#
# if a > 0:
#     print('正数')
# elif a < 0:
#     print('负数')
# else:
#     print('0')

# 判定年份是否是闰年
# year = int(input('请输入一个年份: '))
#
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print('闰年')
# else:
#     print('平年')

# if year % 100 == 0: # 世纪闰年
#     if year % 400 == 0:
#         print('闰年')
#     else:
#         print('平年')
# else: # 普通闰年
#     if year % 4 == 0:
#         print('闰年')
#     else:
#         print('平年')

# a = int(input('请输入一个数: '))
# if a != 1:
#     pass
# else:
#     print('hello')
#
# a = 10
# b = 20
# if a < b:
#     pass
# while a < b:
#     pass
# for x in range(10):
#     pass
#
#
# def func():
#     pass
#
#
# class MyClass:
#     pass
#

a = 10
b = 20
# 单行if语句
if a < b: print('a is less than b')
# 单行if else语句(一个条件语句)
print('a') if a < b else print('b')
# 单行if else语句(多个条件语句)
print('a') if a < b else print('=') if a == b else print('b')
