#!/usr/bin/env python
# _*_coding:utf-8_*_

'''
@Time :    2021/1/13 14:07
@Author:  user
'''

a,b=10,10
print(a==b) #判断value
print(a is b) #判断地址

print(id(a),id(b))

list1 = [1,2,3]

list2 = [1,2,3]

print(list1==list2)
print(list1 is list2)
print(list1 is not list2)

