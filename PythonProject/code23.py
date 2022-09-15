# # 假设我要吃五个包子
# for i in range(1, 6):
#     if i == 3: # 发现第3个包子有虫子
#         continue
#     print(f'吃第{i}个包子')

# 还是要吃五个包子
# for i in range(1, 6):
#     if i == 3: # 发现第3个包子有半只虫
#         break
#     print(f'吃第{i}个包子')

# 给定若干个数字，求平均值（不知道有多少个数字）
theSum = 0
count = 0
while True:
    num = input('请输入一个数字(分号表示输入结束): ')
    if num == ';': # 假设分号表示输入结束
        break
    num = float(num)
    theSum += num
    count += 1
print(f'平均值为{theSum/count}')