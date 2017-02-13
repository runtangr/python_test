#!usr/bin/env python
# -*- coding:utf-8 -*-
a=[1,2,4,2,4,5,7,10,5,5,7,0,1,8,9,0,3]
a.sort()
last=a[-1]
for i in range(len(a)-2,-1,-1):
    if last==a[i]:
        del a[i]
    else:last=a[i]
    print(a)

list_a = [1,2,3,"hello",["python","C++"]]
list_b = list_a
for x in list_a, list_b:
    print(id(x))
list_b = [each for each in list_a]
print(id(list_b))
print(id(list_a))

for x in list_a:
    print(id(x))
for x in list_b:
    print(id(x))