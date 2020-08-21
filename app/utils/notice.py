#!/usr/bin/env python
# -*- coding: utf-8 -*-
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header
EMAIL_switch=1
class Notice:

    def email(self,message,subject):
        if EMAIL_switch ==1:
            sender = 'luyonghao@shandiany.com'
            receivers = ['roy.lu@rccchina.com','842072252@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

            # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
            message = MIMEText(message, 'plain', 'utf-8')
            message['From'] = Header("闪电猿", 'utf-8')   # 发送者
            message['To'] =  Header("测试", 'utf-8')        # 接收者
            subject = subject
            message['Subject'] = Header(subject, 'utf-8')
            try:
                password='NZ4aULAXRcWge7JM'
                smtp=smtplib.SMTP_SSL('smtp.exmail.qq.com')
                smtp.connect('smtp.exmail.qq.com',465)
                smtp.login(sender,password)
                smtp.sendmail(sender, receivers, message.as_string())
                print("邮件发送成功")
            except smtplib.SMTPException:
                print("Error: 无法发送邮件")
        else:
            print("邮件开关未开启")
    def message(self):
        pass

if __name__=='__main__':
    print(Notice().email(message='test',subject='test'))