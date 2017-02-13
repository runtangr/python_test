#/usr/bin/env python
# -*- coding:utf-8 -*-
#author :tangyui
#显示省市县三级联动的选择
dic = {
	"河北": {
		"石家庄": ["鹿泉", "藁城", "元氏"],
		"邯郸": ["永年", "涉县", "磁县"],
			},
	"湖南": {
		"长沙":['a','b','c'],
		"株洲":['d','e','f']
			},
	"湖北": {
		"武汉":['g','h','i'],
		"黄石":['j','k','l']
			}
	  }
province_index = int(input("输入一个数："))	  
if province_index in dic.keys():         ###如果输入为数字编号，则从字典中获取具体省份或直辖市名称###
    print(dic[province_index])
for k in dic.keys():
	print(k)