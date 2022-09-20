# # 1.使用in来判定某个key是否在字典中存在
# a = {
#     'id': 1,
#     'name': 'zhangsan'
# }
# print('id' in a)
# print('sex' in a)
# # in只是判定key是否存在, 和value无关
# print('zhangsan' in a)

# 2.使用[]来根据key获取到value
a = {
    'id': 1,
    'name': 'zhangsan',
    100: 'lisi'
}
print(a['id'])
print(a['name'])
print(a[100])
print(a['sex'])