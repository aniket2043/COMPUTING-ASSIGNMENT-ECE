print(f'**************************ASSIGNMENT-4*************************')
print('#################################################################')

print(f'**************************QUESTION-1****************************')

# Function to solve the tower of hanoi
 
def TowerOfHanoi(n , source, destination, auxiliary):
    if n==1:
        print ("Move disk 1 from source",source,"to destination",destination)
        return
    TowerOfHanoi(n-1, source, auxiliary, destination)
    print ("Move disk",n,"from source",source,"to destination",destination)
    TowerOfHanoi(n-1, auxiliary, destination, source)
         
# Driver code
n = 3
TowerOfHanoi(n,'A','B','C')
# A, C, B are the name of rods


print('#################################################################')

print(f'**************************QUESTION-2****************************')

# Printing Pascal's Triangle.
# USING FACTORIAL
from math import factorial
print('PASCAL TRIANGLE USING RECURSSION')
# input n
n =int(input('PLEASE ENTER HOW MANY ROWS OF PASCAL TRIANGLE YOU WANT:\n'))
for i in range(n):
	for k in range(n-i+1):

		# for left spacing
		print(end=" ")

	for k in range(i+1):

		print(factorial(i)//(factorial(k)*factorial(i-k)), end=" ")

	print()

# Printing Pascal's Triangle.
# USING RECURSSION.
from math import factorial
a=int(input('PLEASE ENTER HOW MANY ROWS OF PASCAL TRIANGLE YOU WANT:\n'))
def pascal(j):
    global a
    if j==a:
        return 0
    elif j<a:
            # Definig space function for printing space before every line.
            def space(j):
                    print(' '*(a-j),end=" ")
                    # defining line function for pinting the elements in the line.
                    def line(i):
                        nonlocal j
                        if i<j:
                            return print(factorial(j)//(factorial(i)*factorial(j-i)), end=" "),line(1+i)
                            #Printing the elements in line and using recurssion on line() function.
                        elif i==j:
                            return print(factorial(j)//(factorial(i)*factorial(j-i))),line(1+i)
                    line(0)#Executing line function with j=0.
            space(j+1)#Executing space function with j=0.
    return pascal(j+1)#Using recurssion on pascal function.
pascal(-1)#Assigning value of j to be -1.

print('#################################################################')

print(f'**************************QUESTION-3****************************')

num1=int(input('PLEASE ENTER FIRST INTEGER:\n'))
num2=int(input('PLEASE ENTER SECOND INTEGER:\n'))
while True:
    if num1<1 or num2<1:
        print('PLEASE ENTER A POSITIVE INTEGER.')
        num1=int(input('PLEASE ENTER FIRST INTEGER:\n'))
        num2=int(input('PLEASE ENTER SECOND INTEGER:\n'))
    else:
        break
quotient,remainder=divmod(num1,num2)
print('THE QUOTIENT ON DIVIDING  NUM1 BY NUM2 IS:',quotient)
print('THE REMAINDER ON DIVIDING  NUM1 BY NUM2 IS:',remainder)

# 3.a
print("3.a")
# Using inbuilt function callable 
# to check whether it(function/values) is callable or not.
print(callable(quotient))
print(callable(remainder))
print(callable(divmod))

# 3.b
print("3.b")
# Appyling inbuilt function (all()),
# to check whether all values in variable values is zero or not.
values=[quotient,remainder]
print(all(v == 0 for v in values))

# 3.c
print("3.c")
a=[4,5,6]
# Using addition operator to add a and values.
values=a+values
filtered_list=[]
# Using inbuilt function filter(), 
#  to filter out the values which are greater than 4.
filtered_list = filter(lambda value: value >4, values)
filtered_list=list(filtered_list)
print(filtered_list)

# 3.d
print("3.d")
# Using set() function to create a set of filtered list.
set=set(filtered_list)
print(set)

# 3.e
print("3.e")
# Using inbuilt function frozenset() to make the set immutable.
immutable_set=frozenset(set)
print(immutable_set)

# 3.f
print("3.f")
# Using inbuilt function max(),
# to evaluate the maximum value from set.
print(f'THE MAXIMUM VALUE IN THE SET IS: {max(set)}')
# Using inbuilt function hash(),
# to find out its hash value.
print(f'THE HASH VALUE IN THE SET IS: {hash(max(set))}')

print('#################################################################')

print(f'**************************QUESTION-4****************************')

# Creating A Class
class Student:
    # Initalizing
    def __init__(self,name,roll_number):
        self.name=name
        self.roll_number=roll_number
    # Creating Destructor
    def student_details(self):
        print('Student Name:',self.name)
        print('Student Name:',self.roll_number)
    def __del__(self):
        print('Destrucor called,Student deleted ')
# Creating Object
stu_1=Student('Aniket',21105073)
# Printing Detaisl
stu_1.student_details()
# Deleting(Calling destructor)

print('#################################################################')

print(f'**************************QUESTION-5****************************')

# Creating class employees
class Employees():
    # Using init function to assign variables(Initalizing).
    def __init__(self,employee,name,salary):
        self.name=name
        self.salary=salary
        self.employee=employee
    # Creating function to print employee details.
    def details(self):
        print('Employee :',self.employee)
        print('Employee Name :',self.name)  
        print('Employee Salary :',self.salary)
# Creating objects.
emp_1=Employees(1,"Mehak",40000)
emp_2=Employees(2,"Ashok",50000)
emp_3=Employees(3,"Viren",60000)
# Using objects to execute details function. 
emp_1.details()
emp_2.details()
emp_3.details()

# 5.a
# Updating salary of Mehak.
print('5.a')
emp_1.salary=70000
emp_1.details()

# 5.b
# Using inbuilt destructor to delete emp3 object.
print('5.b')
del emp_3
# Showing that emp3 object now does not exist.
# emp_3.details()


print('#################################################################')

print(f'**************************QUESTION-6****************************')

def test():
    george=str(input("PLEASE ENTER YOUR WORD GEORGE:\n"))
    barbie=str(input("PLEASE ENTER YOUR WORD BARBIE:\n"))
    a=str(input("Does Barbie's word make sense?reply in y or n:\n"))
    if a=='y'or a=='Y':
        shopkeeper_input='Yes,the word make sense.'
    elif a=='N' or a=='n':
        shopkeeper_input='No,the word does not make sense.'
    list_george=george.split() 
    if len(list_george)==1:
        characters=tuple(george)
        counts_george=dict()
        for character in characters:
            if character not in counts_george:
                counts_george[character]=1
            else:
                counts_george[character]=counts_george[character]+1
        print(counts_george)


    list_barbie=barbie.split() 
    if len(list_barbie)==1:
        characters=tuple(barbie)
        counts_barbie=dict()
        for character in characters:
            if character not in counts_barbie:
                counts_barbie[character]=1
            else:
                counts_barbie[character]=counts_barbie[character]+1
        print(counts_barbie)
    if counts_barbie!=counts_george:
        print('SORRY,YOUR FRIENDSHIP IS FAKE BECAUSE YOUR LETTERS DID NOT MATCHED.')
    elif counts_barbie==counts_george and shopkeeper_input=='No,the word does not make sense.':
        print("SORRY,YOUR FRIENDSHIP IS FAKE BECAUSE BARBIE'S WORD DOES NOT MADE SENSE.")
    else:
        print("CONGRATULATIONS,YOUR FRIENDSHIP IS TRUE!!!!")

test()

print('#################################################################')