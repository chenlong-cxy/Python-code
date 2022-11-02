# import random
# import sys
# import os
# from pynput import keyboard
# from playsound import playsound
# from threading import Thread
#
#
# #生成资源文件目录访问路径
# def resource_path(relative_path):
#     if getattr(sys, 'frozen', False):  # 是否Bundle Resource
#         base_path = sys._MEIPASS
#     else:
#         base_path = os.path.abspath(".")
#     return os.path.join(base_path, relative_path)
#
#
# # 访问res文件夹下a.txt的内容
# filename1 = resource_path(os.path.join("sound", "j.mp3"))
# filename2 = resource_path(os.path.join("sound", "n.mp3"))
# filename3 = resource_path(os.path.join("sound", "t.mp3"))
# filename4 = resource_path(os.path.join("sound", "m.mp3"))
# # print(filename1)
# # print(filename2)
# # print(filename3)
#
#
# # count = 0
# # soundList = ['sound/1.mp3', 'sound/2.mp3', 'sound/3.mp3']
# soundList = [filename1, filename2, filename3, filename4]
#
#
# def onRelease(key):
#     """
#     这个函数就是在用户释放键盘按键的时候, 就会被调用到
#     这个函数不是咱们主动调用的, 而是把这个函数交给了listener
#     由listener在用户释放按键的时候自动调用
#     :param key: 用户按下了哪个按键
#     """
#     print(key)
#     print('xxx')
#     print(type(key))
#     print('yyy')
#     # global count
#     # count += 1
#     # if count % 10 == 0:
#         # 播放音频
#         # i = random.randint(0, len(soundList) - 1)
#         # 此处的播放音频, 消耗的时间比较多, 可能会引起输入的卡顿(不流畅)
#         # 可以创建一个线程, 在线程里播放音频
#         # playsound(soundList[i])
#     i = 0
#     if key.char == 'j':
#         i = 0
#     elif key.char == 'n':
#         i = 1
#     elif key.char == 't':
#         i = 2
#     elif key.char == 'm':
#         i = 3
#     print(f'i={i}')
#     t = Thread(target=playsound, args=(soundList[i], ))
#     t.start()
#
#
# # 当我们创建好listener之后, 用户的键盘案件动作就会被捕获到
# # 还希望在捕获到后能够执行一段代码
# listener = keyboard.Listener(on_release=onRelease)
# listener.start()
# listener.join()


# import sys
# import os
# from pynput import keyboard
# from playsound import playsound
# from threading import Thread
#
#
# #生成资源文件目录访问路径
# def resource_path(relative_path):
#     if getattr(sys, 'frozen', False):  # 是否Bundle Resource
#         base_path = sys._MEIPASS
#     else:
#         base_path = os.path.abspath(".")
#     return os.path.join(base_path, relative_path)
#
#
# # 访问res文件夹下a.txt的内容
# filename1 = resource_path(os.path.join("sound", "j.mp3"))
# filename2 = resource_path(os.path.join("sound", "n.mp3"))
# filename3 = resource_path(os.path.join("sound", "t.mp3"))
# filename4 = resource_path(os.path.join("sound", "m.mp3"))
#
#
# # soundList = ['sound/1.mp3', 'sound/2.mp3', 'sound/3.mp3']
# soundList = [filename1, filename2, filename3, filename4]
#
#
# def onRelease(key):
#     """
#     这个函数就是在用户释放键盘按键的时候, 就会被调用到
#     这个函数不是咱们主动调用的, 而是把这个函数交给了listener
#     由listener在用户释放按键的时候自动调用
#     :param key: 用户按下了哪个按键
#     """
#     print(key)
#     # playsound(soundList[i])
#     i = 0
#     if key.char == 'j':
#         i = 0
#     elif key.char == 'n':
#         i = 1
#     elif key.char == 't':
#         i = 2
#     elif key.char == 'm':
#         i = 3
#     print(f'i={i}')
#     t = Thread(target=playsound, args=(soundList[i], ))
#     t.start()
#
#
# # 当我们创建好listener之后, 用户的键盘案件动作就会被捕获到
# # 还希望在捕获到后能够执行一段代码
# listener = keyboard.Listener(on_release=onRelease)
# listener.start()
# listener.join()

import sys
import os
from pynput import keyboard
from playsound import playsound
from threading import Thread

def resource_path(relative_path):
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


letterToAudio = {
    'j': resource_path(os.path.join('sound', 'j.mp3')),
    'n': resource_path(os.path.join('sound', 'n.mp3')),
    't': resource_path(os.path.join('sound', 't.mp3')),
    'm': resource_path(os.path.join('sound', 'm.mp3')),
    'jntm': resource_path(os.path.join('sound', 'jntm.mp3')),
    'ngm': resource_path(os.path.join('sound', 'ngm.mp3')),
    'esc': resource_path(os.path.join('sound', 'phw.mp3')),
    'space': resource_path(os.path.join('sound', 'xmr.mp3'))
}
# letterToAudio = {
#     'j': 'sound/j.mp3',
#     'n': 'sound/n.mp3',
#     't': 'sound/t.mp3',
#     'm': 'sound/m.mp3',
#     'jntm': 'sound/jntm.mp3',
#     'ngm': 'sound/ngm.mp3'
# }
history = ''


def onRelease(key):
    global history
    audio = ''
    try:
        if len(history) < 4:
            history += key.char
        else:
            history = history[1:] + key.char

        if history == 'jntm':
            audio = letterToAudio[history]
        elif history[-3:] == 'ngm':
            audio = letterToAudio[history[-3:]]
        elif key.char in 'jntm':
            audio = letterToAudio[key.char]
        # print(f'用户输入: {key.char}')
    except AttributeError:
        history = ''
        if key == keyboard.Key.esc:
            audio = letterToAudio['esc']
        elif key == keyboard.Key.space:
            audio = letterToAudio['space']
        # print(f'用户输入: {key.name}')
    if audio != '':
        t = Thread(target=playsound, args=(audio,))
        t.start()
        # playsound(audio)


listener = keyboard.Listener(on_release=onRelease)
listener.start()
listener.join()
