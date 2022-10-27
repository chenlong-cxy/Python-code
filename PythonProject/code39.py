# 1.创建字典
a = {}
print(type(a))  # <class 'dict'>
print(a)        # {}
a = dict()
print(type(a))  # <class 'dict'>
print(a)        # {}

a = {
    'id': 1,
    'name': 'dragon'
}
print(type(a))  # <class 'dict'>
print(a)        # {'id': 1, 'name': 'dragon'}

# 2.创建字典的同时设置初始值
# a = {'id': 1, 'name': 'zhangsan'}
a = {
    'id': 1,
    'name': 'zhangsan'
}
print(a['id'])
