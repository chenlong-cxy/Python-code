# 1.在字典中新增元素, 使用[]来进行
a = {
    'id': 1,
    'name': 'dragon'
}
a['sex'] = 'male'
print(a)  # {'id': 1, 'name': 'dragon', 'sex': 'male'}

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