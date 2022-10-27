# # 1.使用in来判定某个key是否在字典中存在
a = {
    'id': 1,
    'name': 'dragon'
}
print('id' in a)       # True
print('sex' in a)      # False
print('id' not in a)   # False
print('sex' not in a)  # True
# # in只是判定key是否存在, 和value无关
# print('zhangsan' in a)

a = {
    'id': 1,
    'name': 'dragon'
}
print(a.get('name'))  # dragon
print(a.get('sex'))   # None

# 2.使用[]来根据key获取到value
a = {
    'id': 1,
    'name': 'dargon',
}
print(a['name'])  # dragon
# print(a['sex'])   # 指定key值不存在,抛异常
