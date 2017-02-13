#/usr/bin/env python
# -*- coding:utf-8 -*-
alist  = [23,54,2,521,78,55,22,42,56,345,543]

max_list = []
min_list = []
num_tuple = {}
#help(max_list)
for num in alist:
	if num > 100:
		max_list.append(num)
	elif num < 100:
		min_list.append(num)
	else:
		pass
num_tuple['K2'] = min_list
num_tuple['K1'] = max_list

print(num_tuple)
	


	