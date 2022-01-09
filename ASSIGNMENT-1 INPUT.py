print("\t\t\t\t\t\tINTRODUCTION TO COMPUTING ASSIGNMENT-1")
print('\t\t\t\t\t\t\t\tPROBLEM-1')

num1=int(input("please enter number 1:"))
num2=int(input("please enter number 2:"))
num3=int(input("please enter number 3:"))
print((num1+num2+num3)/3)

print('\t\t\t\t\t\t\t\tPROBLEM-2')

gerinc=int(input("please enter your Gross Income in dollars:\n"))
deppeople= int(input("please enter the number of dependentns in your family:\n"))
taxrate=1/5
standarddeduction=10000
dependentdeduction=3000
Taxableincome=gerinc-standarddeduction-(deppeople)*dependentdeduction
Tax=Taxableincome*taxrate
print("YOU HAVE TO PAY:\n",Tax)

print('\t\t\t\t\t\t\t\tPROBLEM-3')

print("please enter your details in the following manner:::[SID,Name,Gender,Department Name,CGPA]")
student1=[21105073,'Aniket Gupta',"M",'ECE',9.2]
print(student1)

print('\t\t\t\t\t\t\t\tPROBLEM-4')

print('Marks of five students ')
Marks=[12,23,43,45,56]
Marks.sort()
print(Marks)

print('\t\t\t\t\t\t\t\tPROBLEM-5(a)')

List=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
List.remove('Black')
print(List)

print('\t\t\t\t\t\t\t\tPROBLEM-5(b)')

List=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
List[3:5]=['Purple']
print(List)
