# PROBLEM-1
print('PROBLEM-1')

string='Python is a case sensitive language'
#a. 
print('a.',len(string))

# b.
print('b.',string[::-1])

#c.
string_new=string[10:26]
print('c.',string_new)
 
#d.
string_new_2=string.replace(string_new,'object oriented')
print('d.',string_new_2)

#e.
print('e.',string.index('a'))

#f.
string_new_3=string.replace(' ','')
print('f.',string_new_3)

print('-----------------------------------------------')


# PROBLEM-2
print('PROBLEM-2')

name='Aniket Gupta'
SID=21105073
department_name='ECE'
CGPA=9.5
string='''Hey, ABC Here!
My SID is 2110XXXX
I am from XYZ department and my CGPA is 9.9'''
string_1=string.replace('ABC',name)
string_2=string_1.replace('2110XXXX',str(SID))
string_3=string_2.replace('XYZ',department_name)
string_final=string_3.replace('9.9',str(CGPA))
print(string_final)

print('-----------------------------------------------')


# PROBLEM-3
print('PROBLEM-3')

a=56
b=10

print('a. a and b is',a&b)

print('b. a or b is',a|b)

print('c. a XOR b is',a^b)

print('d(1). Left Shifting a with 2 bits will give',a<<2)

print('d(2). Left Shifting b with 2 bits will give',b<<2)

print('e(1). Right Shifting a with 2 bits will give',a>>2)

print('e(2). Right Shifting b with 4 bits will give',b>>4)

print('-----------------------------------------------')


# PROBLEM-4
print('PROBLEM-4')

a=int(input('PLEASE ENTER THE FIRST NUMBER:\n'))
b=int(input('PLEASE ENTER THE SECOND NUMBER:\n'))
c=int(input('PLEASE ENTER THE THIRD NUMBER:\n'))
if a>b:
    if a>c:
        greatest=a
    elif a<c:
        greatest=c
elif b>a:
    if b>c:  
        greatest=b
    else:
        greatest=c
print('THE GREATEST OF THREE NUMBERS IS',greatest)

print('-----------------------------------------------')


# PROBLEM-5
print('PROBLEM-5')
string=input('PLEASE ENTER A STRING:\n')
a=string.find('name')
if a>0:
    print('Yes')
elif a==0:
    print('Yes')
else:
    print('No')

print('-----------------------------------------------')


# PROBLEM-6
print('PROBLEM-6')

a=int(input('PLEASE ENTER THE LENGTH OF THE FIRST SIDE:\n'))
b=int(input('PLEASE ENTER THE LENGTH OF THE SECOND SIDE:\n'))
c=int(input('PLEASE ENTER THE LENGTH OF THE THIRD SIDE:\n'))
if a+b>c and a+c>b and b+c>a:
    print('Yes')
else:
    print('No')

print('-----------------------------------------------')
