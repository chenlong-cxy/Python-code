# 直接使用for循环来遍历字典
a = {
    'name': 'zhangsan',
    'id': 1,
    'socre': 90
}
# for key in a:
#     print(key, a[key])  # 打印顺序与插入顺序一致
# print(a.keys())
# print(type(a.keys()))
# print(a.values())
# print(type(a.values()))
# print(a.items())
# print(type(a.items()))
for key, value in a.items():
    print(key, value)