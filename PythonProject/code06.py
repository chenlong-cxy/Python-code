a = 'hello'
b = "hello"
name1 = "My name is 'dragon'"
name2 = 'My name is "dragon"'
name3 = '''My 'name' is "dargon"'''
name4 = """My "name" is'dargon'"""
print(type(a))
print(type(b))
print(type(name1))
print(type(name2))
print(type(name3))
print(type(name4))
print(a)
print(b)
print(name1)
print(name2)
print(name3)
print(name4)
# a = "xxx"yyy"zzz"  # error
# print(a)
a = "dragon"
b = 'dragon'
c = """dragon"""
d = '''dragon'''
print(a)  # dragon
print(b)  # dragon
print(c)  # dragon
print(d)  # dragon
a = "xxx\"yyy\"zzz"
print(a)
