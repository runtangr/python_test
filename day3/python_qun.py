#!usr/bin/env python
# -*- coding:utf-8 -*-
import os
import time
import pickle
class teacher:
    def __init__(self,name,age,admin):
        self.name = name
        self.age = age
        self.assets = 0
        self.admin = admin
        self_creat = time.strftime("%Y-%m-%d %H:%M:%S")

    def agin(self,cost):
        """
        :param cost: 增加的课时费
        :return:
        """
        self.assets += cost

    def decrease(self,cost):
        """
        :param cost:    减少的课时费
        :return:
        """
        self.assets -= cost

class students:
    pass

class Course:
    pass

class Admin:
    def __init__(self):
        self.username = None
        self.password = None
    def login(self,user,pwd):
        """
        :param user: 输入的用户名
        :param pwd: 输入的密码
        :return:返回真假
        """
        self.username = user
        self.password = pwd
        ret = pickle.load(open(user,"rb"))
        if ret.username == user and ret.password == pwd:
            return True
        else:
            return False

    def register(self,user,pwd):
        """
        :param user: 输入的用户名
        :param pwd: 输入的密码
        :return:保存成功返回True保存失败返回False
        """
        self.username = user
        self.password = pwd
        path = self.username
        #会将self中封装的username和password保存在path的文件夹中
        pickle.dump(self,open(path,"xb"))
        return path

def login(user,pwd):
    ret = os.path.exists(user)
    if ret:
        #打开user文件
        Ad_obj = pickle.load(open(user,'rb'))
        Ad = Admin()
        ret = Ad.login(user,pwd)
        if ret:
            print('登录成功\n')
            sel = input("1.创建老师: | 2.创建课程: ")
            if sel == "1":
                ad = pickle.load(open(user,"rb"))
                Admin_obj = ad.username
                print(Admin_obj)
                create_teacher(Admin_obj)
            elif sel == "2":
                pass
        else:
            print("登录失败")
            return False
def register(user,pwd):
    Ad = Admin()
    r = os.path.exists(user)
    if r == False:
        ret = Ad.register(user,pwd)
        if ret:
            print("注册成功")
        else:
            print("注册失败")
    else:
        print("用户名存在")
def create_teacher(admin_obj):
    teacher_list = [123456]
    while True:
        teacher_name = input("请输入老师姓名|q表示退出:")
        if teacher_name == "q":
            break
        teacher_age = input("请输入老师年龄:")
        obj = teacher(teacher_name,teacher_age,admin_obj)
        teacher_list.append(obj)
        print(teacher_list[:])
    if os.path.exists("teacher_list"):
        exists_list = pickle.load(open("teacher_list","rb"))

    pickle.dump(teacher_list,open("teacher_list","wb"))

    # while True:
    #     name = input("请输入老师姓名|Q退出:")
    #     tag = input("请输入老师年龄:")
    #     if name == "q":
    #         break
    #     else:
    #         t = teacher(name,tag,admin)
    #         teacher_list.append(t)
    #
    # if os.path.exists('teacher_list'):
    #      ret = pickle.load(open("teacher_list","rb"))
    #      teacher_list.extend(ret)
    #      print(ret)
    # else:
    #     pickle.dump(teacher_list,open("teacher_list","wb"))
    #     print(123)

def main():
    inp = input("1.管理员登录:| 2.管理员注册:\n>>>")
    user = input("请输入账户:")
    pwd = input("请输入密码:")
    if inp == "1":
        ret = login(user,pwd)
    elif inp == "2":
        register(user,pwd)

if __name__ == "__main__":
    main()


