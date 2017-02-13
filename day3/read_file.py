#!usr/bin/env python
# -*- coding:utf-8 -*-
# f = open('flag.log','w',encoding='utf-8')
# print(f.tell())
# f.write('我afgsfa')
# f.close()

f = open('flag.log','r',encoding='utf-8')
print(f.tell())
ret = f.read(4)
print(ret)
print(f.tell())

f.close()