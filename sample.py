#0
#print("Hey {}! You'll turn 100 years old in {}".format(input("Enter name: "),2018 - int(input("Enter age: ")) + 100))

#1
'''a = eval(input("Enter value: "))
if isinstance(a, int):
	print('int')
elif isinstance(a, float):
	print('Float')
else:
	print('Unknown')'''
	
#2
'''n=int(input("Enter number of elements: "))
l=[]
print("Enter the elements")
for i in range(0,n):
	l.append(int(input()))
l1=[]
for i in range(0,n):
	if l[i]<5:
		l1.append(l[i])
for i in l1:
	print(i)'''
		
#3
'''l = [1,2,3,2,0,65,21,4,2,10]
result = []
x=int(input("Enter element:"))
for i, value in enumerate(l):
	if(value==x):
		result.append(i)
print(result)'''

#4
'''l=[1,1,2,3,4,64,25,93,35,87,4,3]
result=[]
check=True
for i in l:
	for j in result:
		if j==i:
			check=False
	if check==True:
		result.append(i)
	check=True
print(result)'''

#5
'''l={}
i=0
while i<3:
	usn=input('USN: ')
	name=input('Name: ')
	email=input('Email: ')
	if usn not in l:
		l[usn]={'name':name,'email':email}
		i+=1
	else:
		print('error')
print(l)'''

#6
'''def add(a,b):
    return a+b

def sub(a,b):
    if a>b:
        return a-b
    else:
        return b-a
    
def mul(a,b,x,y):
    return a(x,y)*b(x,y)

print(mul(add,sub,10,5))'''

#7
'''a=[1,2,3]
b=[5,6,7]
c=[10,20,30]
d=[]
for x,y,z in zip(a,b,c):
    d.append((x+y+z)**2)
print(d)'''


#8
'''a=input('Enter string: ')
c=input('Enter word to be replaced: ')
b=a.split()
d=input('Enter replacement word: ')
output=''
for i, val in enumerate(b):
    if val==c:
        b.remove(c)
        b.insert(i,d)
for x in b:
    output=output+" "+x
print(output)'''

#9
password=input('Enter password: ')
print('Valid') if all([len(password)>=8,any([x.isupper() for x in password]),any([x.islower() for x in password]),any([x.isdigit() for x in password])]) else print('Invalid')

