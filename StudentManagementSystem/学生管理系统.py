# 命令行版本的学生管理系统
import os
import sys

# 使用字典来管理所有的学生信息
students = {}
# students = {
#     '202021150201': {'name': '张三',
#                      'gender': '男',
#                      'className': '2'},
#     '202021150304': {'name': '李四',
#                      'gender': '女',
#                      'className': '3'},
# }


# 存档
def save():
    with open('record.txt', 'w', encoding='utf8') as f:
        for sId in students:
            sInfo = students[sId]  # 学号为sId的同学的信息
            f.write(f"{sId}\t{sInfo['name']}\t{sInfo['gender']}\t{sInfo['className']}\n")
        print(f'[存档完毕] 共存储了 {len(students)} 条记录!')


# 读档
def load():
    # 如果存档文件不存在则直接跳过读档流程(避免导致异常)
    if not os.path.exists('record.txt'):
        return
    # 读档之前把旧的数据清理干净
    global students
    students = {}
    with open('record.txt', 'r', encoding='utf8') as f:
        for line in f:
            line = line.strip()  # 去掉字符串首位的空白符(\n,\r,\t)
            tokens = line.split('\t')  # 对每一行数据进行切分,以\t作为分隔符
            if len(tokens) != 4:
                print(f'当前行格式存在问题! line = {line}')
                continue
            studentId = tokens[0]
            studentInfo = {
                'name': tokens[1],
                'gender': tokens[2],
                'className': tokens[3]
            }
            # 将该行学生信息插入到students中
            students[studentId] = studentInfo
        print(f'[读档完毕] 共读取了 {len(students)} 条记录!')


# 打印菜单
def menu():
    print('         >>欢迎来到学生管理系统<<         ')
    print('         |   1.新增学生信息   |         ')
    print('         |   2.显示学生信息   |         ')
    print('         |   3.查找学生信息   |         ')
    print('         |   4.删除学生信息   |         ')
    print('         |   5.学生信息存档   |         ')
    print('         |   0.退出管理系统   |         ')
    choice = input('请输入你的选择: ')
    return choice


# 新增
def insert():
    print('[新增学生] 开始!')
    studentId = input('请输入学生的学号: ')
    name = input('请输入学生的姓名: ')
    gender = input('请输入学生的性别: ')
    if gender not in ('男', '女'):
        print('性别输入有误,新增失败!')
        return
    className = input('请输入学生的班级: ')
    # 使用字典将上述信息聚合起来
    studentInfo = {
        'name': name,
        'gender': gender,
        'className': className
    }
    if studentId in students:
        choice = input('已存在该学号的同学,是否对其信息进行覆盖(是/否): ')
        if choice == '否':
            return
    # 将该学生信息插入到students中
    students[studentId] = studentInfo
    print('[新增学生] 完毕!')


# 显示
def show():
    print('[显示学生] 开始!')
    # 遍历全局字典students,把所有学生的信息打印出来
    for sId in students:
        sInfo = students[sId]  # 学号为sId的同学的信息
        print(f"{sId}\t{sInfo['name']}\t{sInfo['gender']}\t{sInfo['className']}")
    print(f'[显示学生] 完毕! 共显示了 {len(students)} 条数据!')


# 查找
def find():
    print('[查找学生] 开始!')
    studentId = input('请输入要查找的同学学号: ')
    flag = False  # 记录是否找到该学号的同学
    for sId in students:
        if sId == studentId:
            sInfo = students[sId]  # 学号为sId的同学的信息
            print(f"[{sId}\t{sInfo['name']}\t{sInfo['gender']}\t{sInfo['className']}]")
            flag = True  # 找到了
            break
    if not flag:
        print('没有找到该学号的同学!')
    print(f'[查找学生] 完毕!')


# 删除
def delete():
    print('[删除学生] 开始!')
    studentId = input('请输入要删除的学生学号: ')
    for sId in list(students.keys()):
        if sId == studentId:
            sInfo = students[sId]  # 学号为sId的同学的信息
            print(f"删除 {sInfo['name']} 同学的信息!")
            students.pop(sId)  # 将该学生信息从students中删除
    print('[删除学生] 完毕!')


# 入口函数
def main():
    load()  # 先进行读档
    while True:
        # 打印菜单
        choice = menu()
        if choice == '1':
            # 新增学生信息
            insert()
        elif choice == '2':
            # 显示学生信息
            show()
        elif choice == '3':
            # 查找学生信息
            find()
        elif choice == '4':
            # 删除学生信息
            delete()
        elif choice == '5':
            # 学生信息存档
            save()
        elif choice == '0':
            # 退出程序
            print('goodbye!')
            sys.exit(0)
        else:
            print('您的输入有误!')

        x = input('按下任意按键继续操作...')
        os.system('cls')  # 清空控制台输出


main()

# f = open('record.txt', 'r')
# for line in f:
#     line = line.strip()
#     print(f'line = {line}')
# f.close()