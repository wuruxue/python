 
# try:
# 	open("a.txt")
# except:
# 	print("no such file or directory!")
# try:
# 	1/0
# except:
# 	print("error")

dirs_path = r'C:\Users\Administrator\Desktop\root\dir1\cp3_data_size.c'
try:
	#1/0
	d = open(dirs_path)
	#open("a.txt")
except:
	print("no such file or directory!")
finally:
	d.close()
	#print("clear up!")
	print("file closed!")
