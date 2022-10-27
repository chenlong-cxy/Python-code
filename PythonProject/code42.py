# 直接使用for循环来遍历字典
a = {
    'name': 'dragon',
    'id': 1,
    'sex': 'male'
}
# for key in a:
#     print(key, a[key])  # 打印顺序与插入顺序一致
for key in a.keys():
    print(key)
print(a.keys())  # dict_keys(['name', 'id', 'sex'])
# print(type(a.keys()))
for value in a.values():
    print(value)
print(a.values())  # dict_values(['dragon', 1, 'male'])
# print(type(a.values()))
for key, value in a.items():
    print(key, value)
print(a.items())  # dict_items([('name', 'dragon'), ('id', 1), ('sex', 'male')])
# print(type(a.items()))
# for key, value in a.items():
#     print(key, value)