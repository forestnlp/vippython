#!/usr/bin/env python
# _*_coding:utf-8_*_

'''
@Time :    2021/1/13 8:50
@Author:  user
'''


print('hello\nworld')

print('hello\tworld')

#奇怪 覆盖掉了
print('hello\rworld')

print('hello\n\rworld')

print('hello\bworld')

print('hello\\world')

print('hello\'world')

print('hello\\\\world')

#原字符
print(r'hello\\\\world')
print(R'hello\\\\world')
#原字符 不能以\结尾
print(r'hello\\\\world\\')
#这种情况实现不了 print(R'hello\\\\world\')
