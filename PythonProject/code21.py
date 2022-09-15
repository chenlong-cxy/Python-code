# 打印1-10的数字
# num = 1
# while num <= 10:
#     print(num)
#     # num += 1

# 计算1-100的和
# sum = 0
# num = 1
# while num <= 100:
#     sum += num
#     num += 1
# print(f'sum = {sum}')

# 计算5的阶乘
# result = 1
# num = 5
# while num >= 1:
#     result *= num
#     num -= 1
# print(f'result = {result}')

# 求1!+2!+3!+4!+5!
# result = 0
# n = 1
# while n <= 5:
#     sub = 1
#     num = 1
#     while num <= n:
#         sub *= num
#         num += 1
#     result += sub
#     n += 1
# print(f'result = {result}')

sum = 0
num = 1
while num <= 5:
    factorResult = 1
    i = 1
    while i <= num:
        factorResult *= i
        i += 1
    sum += factorResult
    num += 1
print(f'sum = {sum}')
