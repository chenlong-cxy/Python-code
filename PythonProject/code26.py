# x = 10
#
#
# def test():
#     x = 20
#     print(f'函数内部: {x}')
#
#
# test()
# print(f'函数外部: {x}')


# x = 10
#
#
# def test():
#     # print(x) # 打印全局变量
#     # x = 20 # 默认被当作在函数中定义局部变量x
#     global x # 声明下面使用的x变量是全局变量
#     x = 20
#
#
# test()
# print(f'x: {x}')


# if、else、for、while等关键字也会引入代码块
# 但这些代码块不会对变量的作用域产生影响
# 在这些代码块内部定义的变量，可以在外面被访问
for i in range(1, 11):
    print(i)

print('---------')
print(i)

# 在Python中只有函数和类才会影响作用域