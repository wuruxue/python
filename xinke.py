import os
from chardet import detect
#a = os.path.isfile(r"C:\Users\Administrator\Desktop\root\a.txt")
#print(a)
root_path = os.getcwd()
dir_count,file_count = 0,0
for root,dirs,files in os.walk(root_path):
	#print(root)
	if not os.path.isfile(root):
		dir_count += 1
	for f in files:
		#print(f)
		if os.path.isfile(os.path.join(root,f)):
			file_count == 1
		#print(os.path.join(root,f))
#print(dir_count-1)
print(dir_count-1,"folders")
print(file_count,"files")


# with open("a.txt","rb") as fp:
# 	encode = detect(fp.read())['encoding']
# 	print("ENCODING:",encode)
# 	#print(detect(fp.read()))

# 	# for f in fp:
# 	# 	print(f)
# line_count,blank_count = 0,0
# with open("a.txt",'r',encoding=encode) as fp:
# 	while True:
# 		line = fp.readline()
# 		if not line:
# 			break
# 		line_count += 1
# 		if len(line.strip()) == 0:
# 			blank_count += 1
# print(line_count,"lines(",blank_count,"blanks)")

# # root_path = os.getcwd()
# # offset = len(root_path.split("\\"))
# # #print(offset)
# # #print(root_path.split("\\"))
# # for root,files,dirs in os.walk(root_path):
# # 	 current_dir = root.split("\\")
# # 	 indent_level = len(current_dir) - offset
# # 	 print(indent_level*"\t",current_dir[-1])
# # 	 for f in dirs:
# # 	 	print("\t"*(indent_level+1),f)
