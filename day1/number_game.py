#!usr/bin/env python
# -*- coding:utf-8 -*-
lucky_num = 43
print("猜字游戏：数字范围0~100")
while True:
    number = int(input("请输入数字："))
    if number < lucky_num:
        print("请输入大一点的数")
    if number > lucky_num:
        print("请输入小一点的数")
    if number == lucky_num:
        print("输入正确！")
        break
