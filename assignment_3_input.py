print(f'**************************ASSIGNMENT-3*************************')
print('#################################################################')

print(f'**************************QUESTION-1****************************')

print('THIS IS A PROGRAM TO FIND THE NUMBER OF OCCURRENCES WORDS/CHRACTERS IN STRING.')
string=input('PLEASE ENTER A STRING=\n')
list=string.split()
i=True
while i:
    if len(list)<1:
        print('PLEASE ENTER A VALID STRING!!')
        string=input('PLEASE ENTER A STRING=\n')
        list=string.split()
    else:
        i=False
# PROGRAM TO FIND NUMBER OF OCCURENCES OF EACH CHRACATER IF ONLY ONE WORD IS ENTERED BY THE USER.
if len(list)==1:
    characters=tuple(string)
    counts=dict()
    for character in characters:
        if character not in counts:
            counts[character]=1
        else:
            counts[character]=counts[character]+1
    print(counts)
# PROGRAM TO FIND NUMBER OF OCCURENCES OF EACH WORD IN A STRING IF MULTIPLE WORDS ARE ENTERED BY THE USER.
else:
    counts=dict()
    for word in list:
        if word not in counts:
            counts[word]=1
        else:
            counts[word]=counts[word]+1
    print(counts)


print('#################################################################')

print(f'**************************QUESTION-2****************************')

print('THIS IS A PROGRAM TO FIND THE NEXT DATE FOR A GIVEN DATE\n')
# taking input from the user
day=int(input('PLEASE ENTER THE DAY:\n'))
month=int(input('PLEASE ENTER THE MONTH:\n'))
year=int(input('PLEASE ENTER THE YEAR:\n'))
# given conditions in the question.
while True:
    if 1<=day<=31:
        break
    else:
        print('PLEASE ENTER A DAY IN RANGE 1 T0 31')
        day=int(input('PLEASE ENTER THE DAY:\n'))

while True:
    if 1<=month<=12:
        break
    else:
        print('PLEASE ENTER A MONTH IN RANGE 1 T0 12')
        month=int(input('PLEASE ENTER THE MONTH:\n'))

while True:
    if 1800<=year<=2025:
        break
    else:
        print('PLEASE ENTER A YEAR IN RANGE 1800 T0 2025')
        year=int(input('PLEASE ENTER THE YEAR:\n'))
# conditions on month having 30 days.
while True:
    if month==4 or month==6 or month==9 or month==11:
        if day==31:
            print('THE NUMBER OF DAYS POSSIBLE ARE 30 IN THIS MONTH')
            day=int(input('PLEASE ENTER THE DAY:\n'))
            continue
        else:
            break
    else:
        break
# conditions on feburary
while True:
    if month==2:
        if day==29:
            a=year%4
            if a==0 :    
                break
            elif a!=0:
                print('THE NUMBER OF DAYS POSSIBLE ARE 28 IN THIS MONTH THIS YEAR')
                day=int(input('PLEASE ENTER THE DAY:\n'))
                continue
        elif day==30 or day==31:
            print('THE NUMBER OF DAYS POSSIBLE ARE 28 or 29 IN THIS MONTH')
            day=int(input('PLEASE ENTER THE DAY:\n'))
            continue
        else:
            break  
    else:
            break
# conditions on the next date
if 1<=day<=27:
    print(f'THE NEXT DAY FROM THIS DAY WOULD BE {day+1}/{month}/{year}')

elif day==28:
    if month==2:
        a=year%4
        if a==0 :    
            print(f'THE NEXT DAY FROM THIS DAY WOULD BE {day+1}/{month}/{year}')
        elif a!=0:   
             print(f'THE NEXT DAY FROM THIS DAY WOULD BE 1/3/{year}')
    else:
        print(f'THE NEXT DAY FROM THIS DAY WOULD BE {day+1}/{month}/{year}')

elif day==29:
    if month==2:       
        print(f'THE NEXT DAY FROM THIS DAY WOULD BE 1/3/{year}')
    else:
        print(f'THE NEXT DAY FROM THIS DAY WOULD BE {day+1}/{month}/{year}')

elif day==30:
    if month==4 or month==6 or month==9 or month==11:       
        print(f'THE NEXT DAY FROM THIS DAY WOULD BE 1/{month+1}/{year}')
    else:
        print(f'THE NEXT DAY FROM THIS DAY WOULD BE {day+1}/{month}/{year}')

elif day==31:
    if month==12:
        print(f'THE NEXT DAY FROM THIS DAY WOULD BE 1/1/{year+1}')
    else:    
        print(f'THE NEXT DAY FROM THIS DAY WOULD BE 1/{month+1}/{year}')

print('#################################################################')

print(f'**************************QUESTION-3****************************')

print("THIS IS A PROGRAM TO FIND THE SQUARES OF A LIST OF NUMBERS. ")
# TAKING INPUT FROM USER AND SAVING THE NUMBERS IN A LIST
num=int(input('PLEASE ENTER A NUMBER :\n'))
num_list=[num]
# APPLYING LOOP IN CASE IF USER WANT TO ENTER MULTIPLE NUMBERS AND SAVING THEM IN LIST.
while True:
    a=str(input("DO YOU WANT ANOTHER NUMBER?\nREPLY IN 'Y'OR'N':"))
    if a=='Y'or a=='y':
        num=int(input('PLEASE ENTER A NUMBER :\n'))
        num_list.append(num)
    elif a=='N'or a=='n':
        break
    else:
        print("PLEASE REPLY IN 'Y'OR'N'.")
        continue
# APPLYING LOOP FOR SQUARING THE NUMBERS AND SAVING THEM INSIDE A DICTONARY.
d=dict()
for number in num_list:
    d[number]=number**2
# PRINTING THE ITEMS IN THE DICTONARY
tups=d.items()
print(tups)

print('#################################################################')

print(f'**************************QUESTION-4****************************')

print('THIS IS A PROGRAM TO KNOW YOUR GRADE AND PERFORMANCE FROM A GIVEN GRADE POINT.')
# TAKING INPUT FROM THE USER.
grade=int(input('PLEASE ENTER YOUR GRADE POINTS:\n'))
i=False
while i is False:
    if grade>10 or grade<4:
        print('PLEASE ENTER GRADE POINTS IN RANGE 4 TO 10')
        grade=int(input('PLEASE ENTER YOUR GRADE POINTS:\n'))
    else:
        i=True
# SAVING THE GIVEN CONDITIONS IN A DICTONARY.
grade_dict=dict()
grade_dict[10]="Your Grade is ‘A+’ and Outstanding Performance."
grade_dict[9]="Your Grade is ‘A’ and Excellent Performance."
grade_dict[8]="Your Grade is ‘B+’ and Very Good Performance."
grade_dict[7]="Your Grade is ‘B’ and Good Performance."
grade_dict[6]="Your Grade is ‘C+’ and Average Performance."
grade_dict[5]="Your Grade is ‘C’ and Below Average Performance."
grade_dict[4]="Your Grade is ‘D’ and Poor Performance."
# PROVIDING OUTPUT TO THE USER FROM THE DICTONARY.
print(grade_dict[grade])

print('#################################################################')

print(f'**************************QUESTION-5****************************')

# PROVIDING STRING WHICH GIVES THE BASSIS OF THE PATTERN
string="ABCDEFGHIJK"
n=11
i=0
# APPLYING WHILE LOOP TO PRINT THE GIVEN PATTERN
while i<6:
    print(' '*i,string[0:n-(2*i)])
    i=i+1

print('#################################################################')

print(f'**************************QUESTION-6****************************')

print('THIS IS A PROGRAM TO SAVE THE NAME AND SID OF STUDENTS IN A DICTONARY.')
# TAKING INPUT FROM USER AND SAVING THEM IN RESPECTIVE LISTS.
name=str(input('PLEASE ENTER NAME OF STUDENT:\n'))
sid=int(input('PLEASE ENTER SID OF STUDENT:\n'))
names_list=[name]
sid_list=[sid]
# APPLYING LOOP TO ASK THE USER FOR MULTIPLE INPUTS AND SAVING THEM IN RESPECTIVE LISTS.
while True:
    a=str(input("DO YOU WANT ANOTHER NAME?\nREPLY IN 'Y'OR'N':"))
    if a=='Y'or a=='y':
        name_i=str(input('PLEASE ENTER NAME OF STUDENT:\n'))
        sid_i=int(input('PLEASE ENTER SID OF STUDENT:\n'))
        names_list.append(name_i)
        sid_list.append(sid_i)
    elif a=='N'or a=='n':
        break
    else:
        print("PLEASE REPLY IN 'Y'OR'N'.")
        continue

# 6.a
print('6.a\n')
# APPLYING LOOP TO SAVE THE SID AS KEYS AND RESPECTIVE NAMES AS VALUES IN A DICTONARY AND PRINTING IT.
student_dict=dict()
for i in range(len(sid_list)):
    student_dict[sid_list[i]]=names_list[i]
print(student_dict)

#6.b
print('6.b\n')
# APPLYING LOOP TO SAVE THE NAME AS KEY AND RESPECTIVE SID AS VALUE IN A DICTONARY AND PRINTING IT.
student_dict_1=dict()
for i in range(len(sid_list)):
    student_dict_1[names_list[i]]=sid_list[i]
# SORTING THE DICTONARY USING SID .
student_dict_2=dict(sorted(student_dict_1.items()))
# APPLYING A PROGRAM TO INVERT THE DICTONARY TO SAVE THE SORTED SID'S AS KEYS AND NAMES AS VALUES IN A NEW DICTONARY.
# SAVING THE NAMES IN THE SORTED DICTONARY IN A LIST.
names_list_sorted =[]
for i in student_dict_2.keys():
    names_list_sorted.append(i)
# SAVING THE SID'S IN THE SORTED DICTONARY IN A LIST.
sid_list_sorted =[]
for i in student_dict_2.values():
    sid_list_sorted.append(i)
student_dict_3=dict()
# APPLYING LOOP TO SAVE THE FINAL NAME AND SID LIST IN RESPECTIVE ORDER IN A FINAL DICTONARY.
for i in range(len(sid_list)):
    student_dict_3[sid_list_sorted[i]]=names_list_sorted[i]
print(student_dict_3)

# 6.c
print('6.c\n')
# SORTING THE DICTONARY USING SID .
print(sorted(student_dict.items()))

#6.d
print('6.d\n')
# PROVIDING THE USER THE LIST OF SID'S OF STUDENTS AND TAKING INPUT OF THE SID OF STUDENT THEY WANT TO FIND.
print('GIVEN BELOW IS THE LIST OF SID OF STUDENTS ')
sid_list.sort()
print(sid_list)
find_sid=int(input('PLEASE ENTER THE SID OF STUDENT YOU WANT TO FIND.'))
# APPLYING LOOP TO CHECK WHETHER THE SID IS VALID.
while True:
    if find_sid not in sid_list_sorted:
        print('PLEASE ENTER THE SID FROM THE GIVEN LIST.')
        print(sid_list)
        find_sid=int(input('PLEASE ENTER THE SID OF STUDENT YOU WANT TO FIND:\n'))
        continue
    else:
        break
# FINDING AND PRINTING THE NAME OF THE STUDENT WITH THE GIVEN SID.
print(student_dict.get(find_sid))


print('#################################################################')

print(f'**************************QUESTION-7****************************')

print('THIS IS A PROGRAM TO PRINT A FIBONACCI SEQUENCE.')
# TAKING INPUT FROM THE USER.
n=int(input('PLEASE ENTER THE VALUE UPTO WHICH YOU WANT TO PRINT THE SEQUENCE:\n'))
while True:
    if n<=0:
        print('PLEASE ENTER A POSITIVE INTEGRAL VALUE.')
        n=int(input('PLEASE ENTER THE VALUE UPTO WHICH YOU WANT TO PRINT THE SEQUENCE:\n'))
        continue
    else:
        break
# SETTING INITIAL PARAMETERS.
n1=0
n2=1
count=0
print(f'THE FIBONACCI SEQUENCE UPTO {n} TERMS IS:\n',end='')
# APPLYING WHILE LOOP TO PRINT THE SEQUENCE.
while count<n:
    print(n1)
    nth=n1+n2
    n1=n2
    n2=nth
    count+=1

print('#################################################################')

print(f'**************************QUESTION-8****************************')

set1= {1, 2, 3, 4, 5}
set2= {2, 4, 6, 8}
set3= {1, 5, 9, 13, 17}

#8.a
set4=(set1|set2)-(set1&set2)
print(f'8.a:{set4}')
#8.b
set5=(set1|set2|set3)-(set1&set2)-(set1&set3)-(set2&set3)
print(f'8.b:{set5}')
#8.c
set6=(set1|set2|set3)-(set1&set2&set3)
print(f'8.c:{set6}')
#8.d
set7={1, 2, 3, 4, 5,6,7,8,9,10}
set8=set7-set1
print(f'8.d:{set8}')
#8.e
set7={1, 2, 3, 4, 5,6,7,8,9,10}
set9=set7&set3
set10=set7-(set1|set2|set9)
print(f'8.e:{set10}')

print('#################################################################')
