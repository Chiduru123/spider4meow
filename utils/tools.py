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
        mail_user = "****@qq.com"  # 用户名
        mail_pass = "*****"  # 口令

        sender = '****@qq.com'
        receivers = ['*****@qq.com']  # 接收邮件

        message = MIMEText(msg, 'plain')
        message['From'] = Header("")
        message['To'] = Header("")

        subject = 'title'  # 标题
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
        accountSID = '*****'
        authToken = '****'
        twilioNumber = '+*****'
        myNumber = '+*****'

        try:
            twilioCli = Client(accountSID, authToken)
            signal = twilioCli.messages.create(
                body=msg,
                from_=twilioNumber,
                to=myNumber)
            print('短信发送成功')
        except Exception as e:
            print('短信发送失败：{}'.format(str(e)))

