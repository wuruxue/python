1����ͨ�ķ����ʼ�

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
server.quit()#�˳�������
#print(msg)

print(msg)



2,html ����

import smtplib
from email.mime.text import MIMEText

from_addr = "1761213498@qq.com"
to_addr = 1761213498@qq.com    #�Լ����͸��Լ�
psw='tqtizbhqrbizbhgj'    #�������������ã��˻���Ȼ���½��Ȩ��֮���õ�
smtp_server="smtp.qq.com"


with open("test.html",'r',encoding="utf-8") as fp:
	contents=fp.read()
print(contents)    #���ʼ��������ҳ��ģ���html��



contents= "<h1>С�����ɰ�����</h1>"
msg=MIMEText(contents,'html','utf-8')    #plain��ͨ��ģ�html�ǼӴְ��
msg['From']=from_addr
msg['To']=to_addr
msg['Subject']="Test"

server=smtplib.SMTP(smtp_server,25)
server.login(from_addr,psw)
server.sendmail(from_addr,to_addr,msg.as_string())
server.quit()  #�˳�������
print(msg)





3���ռ���ķ��ʹ��������ʼ�
import smtplib
from email.mime.text import MIMEText
from email.header import Header  #�൱�ڼ���һ������


from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase   #ÿһ��mimebase��Ӧ����һ������
from email import encoders
def add_attachment(file):
	with open("test.txt",'r') as fp:
		mime=MIMEBase('appilication','octect-string',filename =file)
		mime.add_header("Content-Disposition",'attachment',filename =file)   #���Ը������ݽ�������
		mime.add_header("Content-ID","<0>")
		mime.add_header("X-attachment-ID","0")
		mime.set_payload(fp.read())
		encoders.encode_base64(mime)   #base64  ��һ�ֱ��뷽ʽ����utf-8����
		att_msg.attach(mime)



from_addr = "1761213498@qq.com"
to_addr = from_addr
#psw='tqtizbhqrbizbhgj'
server_addr="smtp.qq.com"
psw='tqtizbhqrbizbhgj'


#�����ʼ����Ķ���
contents= "hello word����"
msg=MIMEText(contents,'plain','utf-8')


#�������������ʼ�����
att_msg =MIMEMultipart()
att_msg['From']=from_addr
att_msg['To']=to_addr
att_msg['Subject']="Test"


att_msg.attach(msg)   #��������ӵ����������ʼ�����


att=["test.txt","test2.txt"]
for a in att:
	add_attachment(a)



#����һ������
# with open("test.txt",'r') as fp:
# 	mime=MIMEBase('appilication','octect-string',filename ="test.txt")
# 	mime.add_header("Content-Disposition",'attachment',filename ="test.txt")#���Ը������ݽ�������
# 	mime.add_header("Content-ID","<0>")
# 	mime.add_header("X-attachment-ID","0")
# 	mime.set_payload(fp.read())
# 	encoders.encode_base64(mime)#base64��һ�ֱ��뷽ʽ����utf-8����
# 	att_msg.attach(mime)


server=smtplib.SMTP(server_addr,25)
server.login(from_addr,psw)
server.sendmail(from_addr,to_addr,att_msg.as_string())
server.quit()    #�˳������� 
print(msg)