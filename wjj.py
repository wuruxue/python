import os
root_path = os.getcwd()

for root,files,dir in os.walk(root_path):
	print(root)