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


print(factor(5))