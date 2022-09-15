import random
import sys
import time

# 人生重开模拟器
print('+-------------------------------------------+')
print('|                                           |')
print('|            花有重开日，人无再少年              |')
print('|                                           |')
print('|            欢迎来到，人生重开模拟器            |')
print('|                                           |')
print('+-------------------------------------------+')

# 设置初始属性
# 颜值、体质、智力、家境（总和不能超过20，每一项取值在1-10之间）
while True:
    print('请设置初始属性(可用点数总数为20)')
    face = int(input('请输入颜值(1-10): '))
    strong = int(input('请输入体制(1-10): '))
    iq = int(input('请输入智力(1-10): '))
    home = int(input('请输入家境(1-10): '))

    if face < 1 or face > 10:
        print('颜值设置有误!')
        continue
    if strong < 1 or strong > 10:
        print('体制设置有误!')
        continue
    if iq < 1 or iq > 10:
        print('智力设置有误!')
        continue
    if home < 1 or home > 10:
        print('家境设置有误!')
        continue
    if face + strong + iq + home > 20:
        print('属性总和超过了20，设置有误!')
        continue

    print('初始属性输入完毕!')
    print(f'颜值: {face}, 体制: {strong}, 智力: {iq}, 家境: {home}')
    break

# 生成角色的性别
# random.randint(begin, end)->生成[begin, end]之间的随机整数
point = random.randint(1, 6)
# print(f'point = {point}')
if point % 2 == 1:
    gender = 'boy'
    print('你是个男孩')
else:
    gender = 'girl'
    print('你是个女孩')

# 设定角色的出生点
point = random.randint(1, 3)
if home == 10:
    # 第一档
    print('你出生在帝都, 你的父母是高官政要')
    home += 1
    iq += 1
    face += 1
elif 7 <= home <= 9:
    # 第二档
    if point == 1:
        print('你出生在大城市，父母是公务员')
        face += 2
    elif point == 2:
        print('你出生在大城市，父母是企业高管')
        home += 2
    else:
        print('你出生在大城市，父母是大学教授')
        iq += 2
elif 4 <= home <= 6:
    # 第三档
    if point == 1:
        print('你出生在三线城市，你的父母是医生')
        strong += 1
    elif point == 2:
        print('你出生在镇上，你的父母是老师')
        iq += 1
    else:
        print('你出生在镇上，你的父母是个体户')
        home += 1
else:
    # 第四档
    if point == 1:
        print('你出生在农村，父母是辛苦劳作的农民')
        strong += 1
        face -= 2
    elif point == 2:
        print('你出生在穷乡僻壤，你的父母是无业游民')
        home -= 1
    else:
        print('你出生在镇上，你的父母感情不和')
        strong -= 1
print(f'颜值: {face}, 体制: {strong}, 智力: {iq}, 家境: {home}')

# 幼年阶段
for age in range(1, 11):
    info = f'你今年{age}岁, '
    point = random.randint(1, 3)
    # 性别触发的事件
    if gender == 'girl' and home <= 3 and point == 1:
        info += '你的家里人重男轻女思想非常严重, 你被遗弃了!'
        print(info)
        print('游戏结束!')
        sys.exit(0)
    # 体制触发的事件
    elif strong < 6 and point < 3:
        info += '你生了一场病, '
        if home >= 5:
            info += '在父母的细心照料下, 你康复了'
            strong += 1
            home -= 1
        else:
            info += '你的父母每精力管你, 你的身体状况更遭了'
            strong -= 1
    # 颜值触发的事件
    elif face <= 4 and age >= 7:
        info += '你长得太丑了, 别的小朋友不喜欢你, '
        if iq > 5:
            info += '你决定用学习填充自己!'
            iq += 1
        else:
            if gender == 'boy':
                info += '你和别的小朋友经常打架!'
                strong += 1
                iq -= 1
            else:
                info += '你经常被别的小朋友欺负'
                strong -= 1
    # 智力触发的事件
    elif iq < 5:
        info += '你看起来傻傻的, '
        if home >= 8 and age >= 6:
            info += '你的父母把你送到更好的学校学习'
            iq += 1
        elif 4 <= home <= 7:
            if gender == 'boy':
                info += '你的父母鼓励你多运动, 争取成为运动员'
                strong += 1
            else:
                info += '你的父母鼓励你多打扮自己'
                face += 1
        else:
            info += '你的父母为此经常吵架'
            if point == 1:
                strong -= 1
            elif point == 2:
                iq -= 1
            else:
                pass
    # 健康成长事件
    else:
        info += '你健康成长, '
        if point == 1:
            info += '你看起来更结实了'
            strong += 1
        elif point == 2:
            info += '你看起来更好看了'
            face += 1
        else:
            pass
    # 打印这一年发生的事情
    print(info)
    print(f'颜值: {face}, 体制: {strong}, 智力: {iq}, 家境: {home}')
    print('---------------------------------------------')
    # 为了方便观察, 加一个sleep
    time.sleep(2)