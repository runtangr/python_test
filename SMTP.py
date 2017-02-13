#!usr/bin/env python
# -*- coding:utf-8 -*-
import smtplib
from email.mime.text import MIMEText
import time
from email.header import Header

from email.utils import parseaddr, formataddr
# 输入Email地址和口令:
from_addr = "1048393815@qq.com"
password = "mudczbxwzbjabcfj"
# 输入SMTP服务器地址:
smtp_server = "smtp.qq.com"
# 输入收件人地址:
to_addr = "793319382@qq.com"
now_time = time.strftime('%H:%M:%S',time.localtime(time.time()))
msg = MIMEText('老孔，起床了！现在时间%s' % now_time,'plain', 'utf-8')


msg['From'] = Header('1048393815@qq.com')
msg['To'] = Header('793319382@qq.com')
msg['Subject'] = Header(u'来自唐豆豆的问候', 'utf-8')

try:
    server = smtplib.SMTP_SSL(smtp_server, 465) # SMTP_SSL协议默认端口是465
    #server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25  测试不成功
    server.login(from_addr, password)
    server.sendmail(from_addr, to_addr, msg.as_string())
    print('邮件发送成功')
except Exception:
    print('邮件发送失败')
server.quit()