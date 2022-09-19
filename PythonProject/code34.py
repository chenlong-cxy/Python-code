# 1.使用append往列表末尾新增一个元素
a = [1, 2, 3, 4]
a.append(5)
a.append('hello')
print(a)

# 2.使用insert方法往列表任意位置新增元素
a = [1, 2, 3, 4]
a.insert(1, 'hello')
a.insert(100, 'world')
print(a)