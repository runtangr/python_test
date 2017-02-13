#/usr/bin/env python
# -*- coding:utf-8 -*-
def main():
	state = input("1:登陆 2：注册 ")
	if state == '1':
		user = input("输入用户名：")
		passwd = input("输入密码：")
		login(user, passwd)
	if state == '2':
		user = input("输入用户名：")
		passwd = input("输入密码：")
		value = register(user, passwd)
		while value == -1:
			user = input("输入用户名：")
			passwd = input("输入密码：")
			value = register(user, passwd)
			
#用户名重复，重新注册
def register(user, passwd):
	with open("db","r+") as f:
		data = f.read()
		have = int(data.find(user))#有没有相同用户名
		if have == -1:
			temp = '\n' + user + '|' + passwd
			f.write(temp)
			print("注册成功！")
			
		elif have != -1:
			print("有相同用户名，请重新注册！")
			return -1

def login(user, passwd):
	with open("db","r+") as f:
		for i in f:
			line_list = i.strip().split('|')
			#print(f)
			#print(i)
			#print(line_list)
			if line_list[0] == user and line_list[1] == passwd:
				print("登陆成功")
				return True
			else:
				continue
		print("登录失败！")
		return False
		
				
					
		
	
	
	
	
main()