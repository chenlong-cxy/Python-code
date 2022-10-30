# import datetime
# # 先构造datetime变量
#
# date1 = datetime.datetime(year=2021, month=1, day=10)
# date2 = datetime.datetime(2022, 9, 22)
# print(date2 - date1)

# from datetime import datetime
# # 先构造datetime变量
#
# date1 = datetime(year=2021, month=1, day=10)
# date2 = datetime(2022, 9, 22)
# print(date2 - date1)

import datetime as dt
# 先构造datetime变量

date1 = dt.datetime(year=2021, month=1, day=10)
date2 = dt.datetime(2022, 10, 30)
print(date2 - date1)  # 658 days, 0:00:00
