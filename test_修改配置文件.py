#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
具体实现了如下功能：
     1、输入1，进入backend菜单，查询server信息
     2、输入2，进入backend菜单，添加server条目
     3、输入3，进入backend菜单，选择server条目，进入修改环节
     4、输入4，进入backend菜单，选择server条目，进入删除环节
     5、输入5，退出程序
'''
import sys
if __name__ == "__main__":
	flag = True
	while flag:
		print('''
         1. 查询后端服务
         2. 添加后端服务
         3. 修改后端服务
         4. 删除后端服务
         5. 退出''')
		select = input("选着输入：")
		if select == '1':
			pass
		elif select == '2':
			pass
		elif select == '3':
			pass
		elif select == '4':
			pass
		elif select == '5':
			sys.exit("退出成功！")
			