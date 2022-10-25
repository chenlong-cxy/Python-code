# 1.使用append往列表末尾新增一个元素
a = [1, 2, 3, 4]
a.append(2021)
a.append('dragon')
print(a)  # [1, 2, 3, 4, 2021, 'dragon']

# 2.使用insert方法往列表任意位置新增元素
a = [1, 2, 3, 4]
a.insert(1, 5)
a.insert(100, 'dragon')
print(a)  # [1, 5, 2, 3, 4, 'dragon']
