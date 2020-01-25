import math
f = open('file2.txt','r',encoding='utf-8')
m=f.read()
emp = []
tot=0
for i in range(256):
	emp.append(0)
for x in m:
	z=ord(x)
	if z<256:
		tot+=1
		emp[z]+=1
num=0
entropy=0.0
for i in range(256):
	if emp[i]!=0:
		num+=1
		emp[i]=emp[i]/tot
		entropy-=emp[i]*math.log(emp[i],2)
print(num)
print(entropy)

opt=tot*entropy/8
print(opt)
