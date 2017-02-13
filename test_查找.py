#/usr/bin/env python
# -*- coding:utf-8 -*-
alist = ["aric", "  alec ", "Alex", "Tony", "rain"]
	
atuple = {"  aric", " alec", "Alex", "Tony", "rain"}

for i in alist:
    if i.strip().capitalize().startswith('A') and i.strip().endswith('c'):
	    print(i)
		
for i in atuple:
    if i.strip().capitalize().startswith('A') and i.strip().endswith('c'):
	    print(i)

	
