1，普通的发送邮件

import smtplib
from email.mime.text import MIMEText

from_addr = "1761213498@qq.com"
to_addr = "1273615605@qq.com"
psw='tqtizbhqrbizbhgj'
smtp_server="smtp.qq.com"

contents= "hello word"
msg=MIMEText(contents,'plain','utf-8')

server=smtplib.SMTP(smtp_server,25)
server.login(from_addr,psw)
server.sendmail(from_addr,to_addr,msg.as_string())
server.quit()#退出服务器
#print(msg)

print(msg)



2,html 发送

import smtplib
from email.mime.text import MIMEText

from_addr = "1761213498@qq.com"
to_addr = 1761213498@qq.com    #自己发送给自己
psw='tqtizbhqrbizbhgj'    #在邮箱里点击设置，账户，然后登陆授权码之后获得的
smtp_server="smtp.qq.com"


with open("test.html",'r',encoding="utf-8") as fp:
	contents=fp.read()
print(contents)    #把邮件变成了网页版的（即html）



contents= "<h1>小姐姐真可爱！！</h1>"
msg=MIMEText(contents,'html','utf-8')    #plain普通版的，html是加粗版的
msg['From']=from_addr
msg['To']=to_addr
msg['Subject']="Test"

server=smtplib.SMTP(smtp_server,25)
server.login(from_addr,psw)
server.sendmail(from_addr,to_addr,msg.as_string())
server.quit()  #退出服务器
print(msg)





3、终极版的发送带附件的邮件
import smtplib
from email.mime.text import MIMEText
from email.header import Header  #相当于加上一个主题


from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase   #每一个mimebase对应的是一个附件
from email import encoders
def add_attachment(file):
	with open("test.txt",'r') as fp:
		mime=MIMEBase('appilication','octect-string',filename =file)
		mime.add_header("Content-Disposition",'attachment',filename =file)   #即对附件内容进行描述
		mime.add_header("Content-ID","<0>")
		mime.add_header("X-attachment-ID","0")
		mime.set_payload(fp.read())
		encoders.encode_base64(mime)   #base64  是一种编码方式，和utf-8相似
		att_msg.attach(mime)



from_addr = "1761213498@qq.com"
to_addr = from_addr
#psw='tqtizbhqrbizbhgj'
server_addr="smtp.qq.com"
psw='tqtizbhqrbizbhgj'


#创建邮件正文对象
contents= "hello word！！"
msg=MIMEText(contents,'plain','utf-8')


#创建带附件的邮件对象
att_msg =MIMEMultipart()
att_msg['From']=from_addr
att_msg['To']=to_addr
att_msg['Subject']="Test"


att_msg.attach(msg)   #将正文添加到带附件的邮件对象


att=["test.txt","test2.txt"]
for a in att:
	add_attachment(a)



#创建一个附件
# with open("test.txt",'r') as fp:
# 	mime=MIMEBase('appilication','octect-string',filename ="test.txt")
# 	mime.add_header("Content-Disposition",'attachment',filename ="test.txt")#即对附件内容进行描述
# 	mime.add_header("Content-ID","<0>")
# 	mime.add_header("X-attachment-ID","0")
# 	mime.set_payload(fp.read())
# 	encoders.encode_base64(mime)#base64是一种编码方式，和utf-8相似
# 	att_msg.attach(mime)


server=smtplib.SMTP(server_addr,25)
server.login(from_addr,psw)
server.sendmail(from_addr,to_addr,att_msg.as_string())
server.quit()    #退出服务器 
print(msg)