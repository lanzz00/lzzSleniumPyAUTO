# encoding: utf-8
'''
@author: lileilei
@file: email_send.py
@time: 2017/4/26 21:02
'''
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
import smtplib,time,os
def create_report_sendemali(from_addr,password,mail_to,subject,path):
    mail_body = ''
    msg = MIMEMultipart()
    msg['Subject'] =subject
    msg['From'] = from_addr
    msg['to'] =mail_to
    msg['Date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')
    report_obj = open(path, 'rb')
    mail_body_value = report_obj.read()
    mail_body = mail_body_value
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(mail_body_value)
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(r'C:\Users\Administrator\Desktop\xuesheng\report\xueshang.html'))
    msg.attach(part)
    report_obj.close()
    body = MIMEText(mail_body, _subtype="html", _charset='utf-8')
    msg.attach(body)
    smtp = smtplib.SMTP()
    server = smtplib.SMTP_SSL("smtp.163.com", 465)
    server.login(from_addr, password)
    server.sendmail(from_addr, mail_to, msg.as_string())
    server.quit()