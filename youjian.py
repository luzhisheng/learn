#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import smtplib
print(smtplib)


def send_email(send_content, receiver):
    # python 发送邮件操作
    # try:
    sender = 'aiyingfeng110@qq.com'
    password = 'ccc'
    smtpserver = 'imap.qq.com'

    smtp = smtplib.SMTP_SSL(smtpserver, timeout=10)
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    (code, resp) = smtp.login(sender, password)
    print('Email login success.')
    result = smtp.sendmail(sender, receiver, send_content)
    print('Email sending result:{}'.format(result))
    smtp.quit()
    # except smtplib.SMTPRecipientsRefused:
    #     print('Recipient refused')
    # except smtplib.SMTPAuthenticationError:
    #     print('Auth error')
    # except smtplib.SMTPSenderRefused:
    #     print('Sender refused')
    # except smtplib.SMTPException as e:
    #     print(e)


send_email('34213123123', 'aiyingfeng110@qq.com')
