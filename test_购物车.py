#/usr/bin/env python
# -*- coding:utf-8 -*-
#author :tangyui
#购物车
goods = [{"name":"钱包","price":50},
		 {"name":"鼠标","price":35},
		 {"name":"电脑","price":4000},
		 {"name":"手机","price":990},
		 {"name":"书","price":30},
		 {"name":"书包","price":45}
		]
price_list = {"钱包":50,"鼠标":35,"电脑":4000,"手机":990,"书":30,"书包":45} 
shopping_car = {"钱包":0,"鼠标":0,"电脑":0,"手机":0,"书":0,"书包":0}

flag = True
total = 0 #资产
sum = 0 #购物车中的总价

print("商品列表如下：")
for i,k in enumerate(goods):
	print(i,k)

total = int(input("输入你的总资产："))
while flag:
	print("输入1为选择需要购买商品，输入2为确认完成购买，输入3为退出")
	select = input("输入：")
	if int(select) == 1:
		goods_serial_num = int(input("输入选择购买商品的编号："))
		goods_geshu = int(input("输入购买商品个数："))
		if goods_serial_num>5:
			print("无此商品！请从新操作")
			continue
		print("商品%s已加入%d个到购物车。" %(goods[goods_serial_num]["name"], goods_geshu) )
		shopping_car[goods[goods_serial_num]["name"]]+=goods_geshu
		
	elif int(select) == 2:
		print("购物车现有商品及其个数如下：")
		print(shopping_car)
		print("确认购买输入1，取消购买输入0")
		enable = int(input("输入："))
		if enable == 1:
			for i,v in shopping_car.items():
				sum+= price_list[i]*v
				#充值或移除商品
			while 1:
				if total < sum:
					print("资金不够！请充值或移除商品或者退出！")
					n = int(input("充值输入1，移除输入2 退出输入3："))
					if n == 1:
						input_money = int(input("输入充值的金额："))
						total+=input_money
						print("充值成功！你的总金额为：%d" % total)
					elif n ==2:
						
						k = int(input("输入移除商品的编号："))
						num = int(input("输入移除商品的数量："))
						if k > 5 :
							print("商品编号错误！，请从新选择")
							continue
						if num > shopping_car[goods[k]["name"]]:
							print("商品数量超过购物车商品数量，请从新选择")
							continue
					elif n ==3:
						break
						
				if total > sum:
					total -=sum
					print("购买成功!")
					print("资产还剩余%d" % total)
					break
		else:
			continue
	elif int(select) == 3:
		print("程序已退出！")
		break
	else:
		print("输入错误，请从新输入！")
		continue
