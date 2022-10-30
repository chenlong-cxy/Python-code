# 翻转单词顺序
def reverseWords(s: str):
    tokens = s.split(' ')    # 切分字符串
    tokens.reverse()         # 逆序列表
    return ' '.join(tokens)  # 拼接字符串


print(reverseWords('I am a student.'))


# 旋转字符串
def rotateString(s, goal):
    if len(s) != len(goal):
        return False
    return goal in (s + s)


print(rotateString('abcde', 'cdeab'))
print(rotateString('abcde', 'edcba'))


# 统计是给定字符串前缀的字符串数目
def countPrefixes(words: list, s: str):
    count = 0
    for word in words:
        if s.startswith(word):  # 还有endswith
            count += 1
    return count


print(countPrefixes(['a', 'b', 'c', 'ab', 'bc', 'abc'], 'abc'))
