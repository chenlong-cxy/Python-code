# def add(x, y, debug=False):
#     if debug:
#         print(f'x = {x}, y = {y}')
#     return x + y
#
#
# result = add(10, 20, True)
# print(result)

# def test(x, y):
#     print(f'x = {x}')
#     print(f'y = {y}')
#
#
# # test(10, 20)
# # test(x=10, y=20)
# # test(y=10, x=20)
# # 混着用的时候要求，位置参数在前，关键字参数在后
# test(10, y=20)
# test(x=10, 20) # error


def test(a, b, c=1, d=2, e=3):
    print(f'a = {a}')
    print(f'b = {b}')
    print(f'c = {c}')
    print(f'd = {d}')
    print(f'e = {e}')


# test(10, 20)
# test(10, c=20, b=30)
test(10, 20, e=100)