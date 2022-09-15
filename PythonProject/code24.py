# 函数的定义
def calcSum(begin, end):
    theSum = 0
    for i in range(begin, end + 1):
        theSum += i
    print(theSum)


# 函数的调用
calcSum(1, 100)
calcSum(300, 400)
calcSum(1, 1000)


def test():
    print('hello')
    print('hello')
    print('hello')


test()
test()


def add(x, y):
    return x + y


print(add(10, 20))
print(add(1.0, 2.0))
print(add('hello', 'world'))
