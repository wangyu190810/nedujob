#coding:utf-8
import random
import smtplib
from email.mime.text import MIMEText
import time

from config import Config

mail_host = 'smtp.163.com'
mail_user = Config.email.get("MAIL_USERNAME")
mail_pwd = Config.email.get("MAIL_PASSWORD")


def send_mail(mailto):


	msg=MIMEText("""123123""")#定义发送能容

	msg['From']=mail_user

	msg['SUbject']=u"测试"

	msg['To']=",".join(mailto)

	try:
		print 'connectting',mail_host
		s=smtplib.SMTP_SSL(mail_host,465)

		print 'Login to mail_host'
		s.login(mail_user,mail_pwd)

		print 'Send mail'
		s.sendmail(mail_user,mailto,msg.as_string())

		print 'close the connection between the mail server'
		s.close()
	except Exception as e:
		print "Exceptioin ",e
def make_mail():
	#产生随机数邮箱，
	nummail=random.randint(100000000,3999999999)
	nummail=str(nummail)
	return nummail+"@qq.com"

def time_mail():
	#设定为十秒发送一封邮件
	time.sleep(10)

if __name__=="__main__":

	send_mail("190810401@qq.com")
	time_mail()

