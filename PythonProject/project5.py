import random
import sys
import os
from pynput import keyboard
from playsound import playsound
from threading import Thread


#生成资源文件目录访问路径
def resource_path(relative_path):
    if getattr(sys, 'frozen', False):  # 是否Bundle Resource
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


# 访问res文件夹下a.txt的内容
filename1 = resource_path(os.path.join("sound", "1.mp3"))
filename2 = resource_path(os.path.join("sound", "2.mp3"))
filename3 = resource_path(os.path.join("sound", "3.mp3"))
# print(filename1)
# print(filename2)
# print(filename3)


count = 0
# soundList = ['sound/1.mp3', 'sound/2.mp3', 'sound/3.mp3']
soundList = [filename1, filename2, filename3]


def onRelease(key):
    """
    这个函数就是在用户释放键盘按键的时候, 就会被调用到
    这个函数不是咱们主动调用的, 而是把这个函数交给了listener
    由listener在用户释放按键的时候自动调用
    :param key: 用户按下了哪个按键
    """
    print(key)
    global count
    count += 1
    if count % 10 == 0:
        # 播放音频
        i = random.randint(0, len(soundList) - 1)
        # 此处的播放音频, 消耗的时间比较多, 可能会引起输入的卡顿(不流畅)
        # 可以创建一个线程, 在线程里播放音频
        # playsound(soundList[i])
        t = Thread(target=playsound, args=(soundList[i], ))
        t.start()


# 当我们创建好listener之后, 用户的键盘案件动作就会被捕获到
# 还希望在捕获到后能够执行一段代码
listener = keyboard.Listener(on_release=onRelease)
listener.start()
listener.join()

