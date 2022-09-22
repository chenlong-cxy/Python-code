# 打开文件个数的上限
flist = []
count = 0
while True:
    f = open('d:/Python环境/test.txt', 'r')
    flist.append(f)
    # f.close()
    count += 1
    print(f'打开文件的个数: {count}')