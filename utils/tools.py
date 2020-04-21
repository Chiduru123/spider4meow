#!/usr/bin/env python
# encoding: utf-8
'''
# Author:        Guo Qi
# File:          tools.py
# Date:          2020/4/20
# Description:   自定义工具类函数：发邮件/ 发短信
'''

import smtplib
from email.header import Header
from email.mime.text import MIMEText
from twilio.rest import Client


class util(object):
    def __init__(self):
        pass

    def send_email(self, msg):
        # 第三方 SMTP 服务
        mail_host = "smtp.qq.com"  # 服务器
        mail_user = "395366251@qq.com"  # 用户名
        mail_pass = "wnjnxktwgyklbgfj"  # 口令

        sender = '395366251@qq.com'
        receivers = ['395366251@qq.com',
                     'ahhjy0807@163.com'
                     ]  # 接收邮件

        message = MIMEText(msg, 'plain')
        message['From'] = Header("是爸爸呀")
        message['To'] = Header("智慧小郭 & 搬砖小惠")

        subject = '豆瓣车价信息'  # 标题
        message['Subject'] = Header(subject)

        try:
            smtpObj = smtplib.SMTP()
            smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
            smtpObj.login(mail_user, mail_pass)
            smtpObj.sendmail(sender, receivers, message.as_string())
            print("邮件发送成功")
        except Exception as e:
            print("Error: 无法发送邮件：" + str(e))

    def send_messge(self, msg):
        accountSID = 'AC8d444e950bbdf2f2ba7b31ef9986e314'
        authToken = '98ee284d0a9aa020be1c37c3ea4876e2'
        twilioNumber = '+17027124022'
        myNumber = '+8615066112078'

        try:
            twilioCli = Client(accountSID, authToken)
            signal = twilioCli.messages.create(
                body=msg,
                from_=twilioNumber,
                to=myNumber)
            print('短信发送成功')
        except Exception as e:
            print('短信发送失败：{}'.format(str(e)))

