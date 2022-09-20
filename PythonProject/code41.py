# 1.在字典中新增元素, 使用[]来进行
a = {
    'id': 1,
    'name': 'zhangsan'
}
a['score'] = 90
print(a)

# 2.在字典中, 根据key来修改value, 也是使用[]来进行的
a['score'] = 100
print(a)

# 3.使用pop方法, 根据key来删除键值对
a.pop('score')
print(a)