#!usr/bin/env python
# -*- coding:utf-8 -*-

import pickle
dic = {'k1':'v1','k2':'v2'}
f = open('str_to_dict.txt','wb')

f.write(pickle.dumps(dic))
f.close()
print(dic)

