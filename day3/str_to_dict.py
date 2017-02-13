#!usr/bin/env python
# -*- coding:utf-8 -*-
import pickle
f = open('str_to_dict.txt','rb')
res = f.read()
print(type(res))
print(pickle.loads(res))