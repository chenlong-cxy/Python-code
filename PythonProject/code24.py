# 1.求1-100的和
sum = 0
for i in range(1, 101):
    sum += i
print(f'sum = {sum}')  # 5050

# 2.求300-400的和
sum = 0
for i in range(300, 401):
    sum += i
print(f'sum = {sum}')  # 35350

# 3.求1-1000的和
sum = 0
for i in range(1, 1001):
    sum += i
print(f'sum = {sum}')  # 500500


# 函数的定义
def calcSum(begin, end):
    theSum = 0
    for i in range(begin, end + 1):
        theSum += i
    return theSum


print(calcSum(1, 100))    # 5050
print(calcSum(300, 400))  # 35350
print(calcSum(1, 1000))   # 500500

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
