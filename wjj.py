import os
root_path = os.getcwd()
offset = len(root_path.split("\\"))
print(offset)
#print(root_path.split("\\"))
for root,files,dirs in os.walk(root_path):
	 current_dir = root.split("\\")
	 indent_level = len(current_dir) - offset
	 print(indent_level*"\t",current_dir[-1])
