# 写一个函数来求n的阶乘
# def factor(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result

def factor(n):
    if n == 1:
        return 1
    return n * factor(n - 1)


print(factor(3))  # 6
ret = factor(3)


def Add(data, val=1):
    return data + val


print(Add(10))     # 11
print(Add(10, 2))  # 12


def Func(*arg):
    n = len(arg)
    for i in range(n):
        print(arg[i])


Func(1)
Func(1, 2, 3)


def getPoint():
    x = 10
    y = 20
    return x, y


x, y = getPoint()


x = 10

def Func():
    # global x
    x = 20
    print(f'函数内部: x = {x}')

Func()
print(f'函数外部: x = {x}')

for i in range(10):
    print(f'函数内部: i = {i}')

print(f'函数外部: i = {i}')  # i = 9
