# 命令行版本的学生管理系统
import os
import sys

# 使用这个全局变量来管理所有的学生信息
students = []


def save():
    """
    用于存档
    """
    with open('record.txt', 'w', encoding='utf8') as f:
        for s in students:
            f.write(f"{s['studentId']}\t{s['name']}\t{s['gender']}\t{s['className']}\n")
        print(f'[存档完毕] 共存储了 {len(students)} 条记录!')


def load():
    """
    用于读档
    """
    # 如果存档文件不存在则直接跳过读档流程(避免导致异常)
    if not os.path.exists('record.txt'):
        return
    # 读档的时候要保证把旧的数据清理干净
    global students
    students = []
    with open('record.txt', 'r', encoding='utf8') as f:
        for line in f:
            # 针对这一行数据, 按照 \t 进行切分操作
            # 切分之前要去除末尾的换行
            line = line.strip()  # 去掉字符串首位的空白符
            tokens = line.split('\t')
            if len(tokens) != 4:
                print(f'当前行格式存在问题! line = {line}')
                continue
            student = {
                'studentId': tokens[0],
                'name': tokens[1],
                'gender': tokens[2],
                'className': tokens[3]
            }
            students.append(student)
        print(f'[读档完毕] 共读取了 {len(students)} 条记录!')


def menu():
    print('1.新增学生')
    print('2.显示学生')
    print('3.查找学生')
    print('4.删除学生')
    print('0.退出程序')
    choice = input('请输入你的选择: ')
    return choice


def insert():
    print('[新增学生] 开始!')
    studentId = input('请输入学生的学号: ')
    name = input('请输入学生的姓名: ')
    gender = input('请输入学生的性别: ')
    if gender not in ('男', '女'):
        print('性别输入内容不符合要求, 新增失败!')
        return
    className = input('请输入学生的班级: ')
    # 使用一个字典将上述的信息给聚合起来
    student = {
        'studentId': studentId,
        'name': name,
        'gender': gender,
        'className': className
    }
    global students
    students.append(student)
    # 新增保存操作
    save()
    print('[新增学生] 完毕!')


def show():
    # 遍历全局遍历students列表, 把所有学生的信息打印出来
    print('[显示学生] 开始!')
    for s in students:
        print(f"[{s['studentId']}]\t{s['name']}\t{s['gender']}\t{s['className']}")
    print(f'[显示学生] 完毕! 共显示了 {len(students)} 条数据!')


def find():
    print('[查找学生] 开始!')
    name = input('请输入要查找的同学姓名: ')
    count = 0
    for s in students:
        if s['name'] == name:
            print(f"[{s['studentId']}]\t{s['name']}\t{s['gender']}\t{s['className']}")
            count += 1
    print(f'[查找学生] 完毕! 共找到了 {count} 个匹配的同学')


def delete():
    print('[删除学生] 开始!')
    studentId = input('请输入要删除的学生学号: ')
    count = 0
    for s in students:
        if s['studentId'] == studentId:
            print(f"删除 {s['name']} 同学的信息!")
            students.remove(s)
    # 新增保存操作
    save()
    print('[删除学生] 完毕!')


def main():
    """
    入口函数
    """
    # 通过控制台和用户进行交互
    print('+--------------------------------------+')
    print('|           欢迎来到学生管理系统           |')
    print('+--------------------------------------+')
    # 需要在程序启动的时候读档即可
    load()
    while True:
        # 通过menu函数来打印出菜单项
        choice = menu()
        if choice == '1':
            # 新增学生
            insert()
        elif choice == '2':
            # 显示所有学生
            show()
        elif choice == '3':
            # 查找学生
            find()
        elif choice == '4':
            # 删除学生
            delete()
        elif choice == '0':
            # 退出程序
            print('goodbye!')
            sys.exit(0)
        else:
            print('您的输入有误! 请重新输入!')
            continue



main()
