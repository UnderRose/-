#python3.4
import math
s=0
n=eval(input("输入"))
a=n
for i in range(1,6):
    b=a%10
    c=a//10
    a=c
    S=s+b*pow(10,5-i)
if S==n:
    print("是回文数")
else:
    print("不是回文数")
