#!/usr/bin/env python
# _*_coding:utf-8_*_

'''
@Time :    2021/1/13 8:42
@Author:  user
'''

print(520)

print(520+520)

helloworld = 'hello'
print(helloworld)

helloworld = "hello"
print(helloworld)

print(1/5)

print(1.0/5.0)


# 输入到文件当中
fd = open('hello.txt', "a+")
print("hello",file=fd)
fd.close()

#不进行换行输出
print('hello','world','python',fd)
