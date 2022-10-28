# 1.在字典中新增元素, 使用[]来进行
a = {
    'id': 1,
    'name': 'dragon'
}
a['sex'] = 'male'
print(a)  # {'id': 1, 'name': 'dragon', 'sex': 'male'}
a = {
    'id': 1,
    'name': 'dragon'
}
a.update({'sex': 'male', 'country': 'China'})
print(a)  # {'id': 1, 'name': 'dragon', 'sex': 'male', 'country': 'China'}
a = {
    'id': 1,
    'name': 'dragon'
}
b = {
    'sex': 'male',
    'country': 'China'
}
a.update(b)
print(a)  # {'id': 1, 'name': 'dragon', 'sex': 'male', 'country': 'China'}
print(b)  # {'sex': 'male', 'country': 'China'}

# 2.在字典中, 根据key来修改value, 也是使用[]来进行的
a = {
    'id': 1,
    'name': 'dragon'
}
a['id'] = 2
print(a)  # {'id': 2, 'name': 'dragon'}

# 3.使用pop方法, 根据key来删除键值对
a = {
    'id': 1,
    'name': 'dragon',
    'sex': 'male'
}
a.pop('sex')
print(a)  # {'id': 1, 'name': 'dragon'}
a = {
    'id': 1,
    'name': 'dragon',
    'sex': 'male'
}
a.popitem()
print(a)  # {'id': 1, 'name': 'dragon'}


keys = ('key1', 'key2', 'key3')
values = 0
a = dict.fromkeys(keys, values)
print(a)

a = {
    'id': 1,
    'name': 'dragon',
}
x = a.setdefault('sex', 'xxx')
print(x)
print(a)
