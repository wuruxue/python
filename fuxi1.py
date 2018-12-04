#import chardet
from chardet import detect
from os.path import isfile
count,blanks = 0,0#rb以二进制代码读
with open("a.txt",'rb') as fp:
	code = detect(fp.read())['encoding']
	print(code)

#pip install chardet
# chardet python库-pip-pip install chardet
#with open("a.txt",'r',encoding='utf-8') as fp:
with open("a.txt",'r',encoding=code) as fp:
	while True:
		line = fp.readline()
		if not line:
			break
		#print(line)
		# if(len(line)-1) == 0:
		# 	blanks += 1
		if len(line.strip()) == 0:
			blanks += 1
		#print(len(line.strip()))
		count += 1
print(count,blanks)
path = r"C:\Users\Administrator\Desktop\root\a.txt"#原生字符串r
print(isfile(path))#  返回True是文件,否是False,idfile(字符串)