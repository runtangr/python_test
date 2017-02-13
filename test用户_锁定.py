#/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
i = 0
j = 0 
while i<3:
	user_name = input("输入用户名：")
	
	lock_file = open(".\\用户和锁定\\user_lock.txt", "r+")
	lock_lines = lock_file.readlines()
	#print(lock_lines)
	for line in lock_lines:
		line = line.strip('\n')
		if line == user_name:
			print("%s用户已被锁定,退出！" %user_name)
			sys.exit(-1)
		
		
	user_file = open(".\\用户和锁定\\user.txt", "r+")
	user_lines = user_file.readlines()
	#print(user_lines)
	for line in user_lines:
		(username,pass_word) = line.strip('\n').split('|')
		username = username.strip()
		pass_word = pass_word.strip()
		# print(username)
		# print(user_name)
		if username == user_name:
			while j<3:
				passsword = input("请输入密码：")
				if pass_word!=passsword:
					if j != 2:
						print("用户%s剩余输入密码次数%d" %(user_name ,(2-j)))
						
				else:
					print("密码正确，欢迎%s用户登录！" %user_name)
					sys.exit(0)
				j += 1
			else:
				lock_file.write(user_name + '\n')
				sys.exit("用户 %s 达到最大登录次数，将被锁定并退出" %user_name)
	if i!= 2:
		print("用户名%s不存在，剩余输入次数%d" %(user_name, (2-i)))
			
	i += 1
else:
	sys.exit("用户名%s不存在,退出" %user_name)
	
	