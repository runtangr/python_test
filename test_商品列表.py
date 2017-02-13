#/usr/bin/env python
# -*- coding:utf-8 -*-
# l1=[1,2,3,4]
# l2=["手机", "电脑", '鼠标垫', '游艇']
# d=dict(zip(l1,l2))
# print(d)
# num=input("请输入商品编号：")
# print("你选择的商品为:%s" % d[int(num)])

li = ["手机", "电脑", '鼠标垫', '游艇']
for k, i in enumerate(li):
	print(k,i)
k=input("请输入商品编号：")
print("你选择的商品为 %s" % li[int(k)])

	
