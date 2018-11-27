#import 包名(把包导入)
#import 包名 as 包别名 (给包取别名)
#from 包名 import *(导入包里的所有函数)
#from 包名 import 函数名 as 函数别名(明确知道导入包里指定的东西)
#from 包名 import 函数1，函数2，...,函数n (明确知道导入包里要用的东西)

import turtle as t
colors = ["red","pink","green","purple"]
t.pensize(2)
for x in range(100):
	t.fd(3*x)
	t.color(colors[x%4])
	t.left(96)
t.done()



