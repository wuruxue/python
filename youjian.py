
import smtplib

from email.mime.text import MIMEText
from_addr ="158249451@qq.com" 
to_addr = "158249451@qq.com"
psw='upsiymnhfradbibd'
smtp_server="smtp.qq.com"

with open("test.html","r",encoding="utf-8")as fp:
	contents = fp.read()



#contents = "<h1>Hello world!</h1>"
#contents = "Hello world!"
#msg=MIMEText(contents,'plain','utf-8')
#
msg=MIMEText(contents,'html','utf-8')
msg['From'] = from_addr
msg['To'] = to_addr
msg['Subject'] = "Test"

server=smtplib.SMTP(smtp_server,25)
server.login(from_addr,psw)
server.sendmail(from_addr,to_addr,msg.as_string())
server.quit()

#"192.168.20.2:500"#后面的这个：500是套接字
