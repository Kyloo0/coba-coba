
""" string """

#1
print("Hello World")

#2
message = "Fitto's World"

#panjang string (termasuk tanda dan spasi)
print(len(message))
#string ke-.... (dimulai dari 0,1,2,...)
print(message[5])
#string pada interval 0 hingga ...
print(message[0:5])
#string pada interval ... hingga akhir
print(message[8:])
#mengubah ke huruf kecil
print(message.lower())
#mengubah ke huruf besar
print(message.upper())
#menghitung banyaknya string
print(message.count('t'))
#mencari string di baris
print(message.find('World'))

#3 (mengganti suatu string)
message = "Fitto's World"
new_message = message.replace('world', 'Universe')
print(new_message)

#4 (penambahan string baru)
message = "Fitto's World"
goal = 'Universe'
result = message + ' ' + 'and' + ' ' + goal
print(result)

new_result = '{} and {}'.format(message, goal)
print(new_result)

new_result2 = f'{message} and {goal}'
print(new_result2)




""" Integers and Float """

#Aritmethic Operators :
#Addition : () + ()
#Subtraction : () - ()
#Multiplication : () * ()
#Division : () / ()
#Floor Division : () // ()
#Exponent : () ** ()
#Modulus/sisa : () % ()

#Comparisson :
#Equal : () == ()
#Not equal : () != ()
#Greater than : () > ()
#Less than : () < ()
#Greater or equal : () >= ()
#Less or equal : () <= ()

#1
num = 3.14
print(type(num))

print(3+2)
print(3-2)
print(3*2)
print(3/2)
print(3**2)
print(3//2)
print(3%2)
print((3*2**2-5+2)/2)

num *=10
print(num)

#2 (mutlak)
print(abs(-104))

#3 (pembulatan)
print(round(4.25))
print(round(4.25, 1)) 

#4 (check the comparisson)
num1 = 189
num2 = 77
print(num1 == num2)

#5 (interger as string)
num_1 = '89'
num_2 = '171'

num_1 = int(num_1)
num_2 = int(num_2)
print(num_1 + num_2)




""" List,tuple,set """
#Empty lists
empty_list = []
empty_list = list()
#Empty tuple
empty_tuple = ()
empty_tuple = tuple()
#Empty sets
empty_set = {}
empty_set = set()

#1
#value
Subject = ['physics','math','chemistry','biology']
print(Subject)
#banyak
Subject = ['physics','math','chemistry','biology']
print(len(Subject))
#lokasi (dimulai dari 0,1,2,... atau minus)
Subject = ['physics','math','chemistry','biology']
print(Subject[0])
print(Subject[-2])
print(Subject[0:2])
print(Subject[:3])
print(Subject[1:])
#penambahan item di list dengan append
Subject = ['physics','math','chemistry','biology']
Subject.append('CompSci')
print(Subject)
#penambahan dengan penempatan
Subject = ['physics','math','chemistry','biology']
Subject.insert(0,'Law')
print(Subject)
#Penambahan dengan extend
Subject = ['physics','math','chemistry','biology']
Subject2 = ['CompSci','Law']
Subject.extend(Subject2)
#menghilangkan item
Subject = ['physics','math','chemistry','biology']
Subject.remove('math')
print(Subject)
#menghilangkan dengan metode pop (dari belakang/reverse)
Subject = ['physics','math','chemistry','biology']
popped = Subject.pop()
print(popped)
print(Subject)
#reverse
Subject = ['physics','math','chemistry','biology']
Subject.reverse()
print(Subject)

#2
#sortir urut abjad dan angka
Subject = ['physics','math','chemistry','biology']
Subject.sort()
print(Subject)

nums = [5,3,0,2,4,1]
Subject.sort()
nums.sort()
print(Subject,nums)

sorted_Subject = sorted(Subject)
print(Subject)
#Sortir dan reverse
Subject.sort(reverse=True)
nums.sort(reverse=True)
print(Subject,nums)
#min,max,sum
nums = [5,3,0,2,4,1]
print(sum(nums))
print(min(nums))
print(max(nums))
#indeks
Subject = ['physics','math','chemistry','biology']
print(Subject.index('math'))
#mencari kata
Subject = ['physics','math','chemistry','biology']
print('Art' in Subject)
#loop
Subject = ['physics','math','chemistry','biology']
for item in Subject:
    print(item)
#loop dengan indeks
Subject = ['physics','math','chemistry','biology']
for index,Subject in enumerate(Subject):
    print(index,Subject)

Subject = ['physics','math','chemistry','biology']
for index,Subject in enumerate(Subject, start=1):
    print(index,Subject)

#3
#mengubah list ke bentuk string
Subject = ['physics','math','chemistry','biology']
Subject_str = ' - '.join(Subject)
print(Subject_str)
#mengembalikan ke bentuk list
Subject = ['physics','math','chemistry','biology']
Subject_str = ' - '.join(Subject)
new_list = Subject_str.split(' - ')
print(new_list)

#4
#sets (acak)
Subject = {'physics','math','chemistry','biology'}
print(Subject)
#irisan
Subject1 = {'physics','math','chemistry','biology'}
Subject2 = {'physics','math','CompSci','Law'}
print(Subject1.intersection(Subject2))
#gabungan/union
Subject1 = {'physics','math','chemistry','biology'}
Subject2 = {'physics','math','CompSci','Law'}
print(Subject1.union(Subject2))




""" dictionaries """

#1
student = {'name':'Kyle', 'age':19, 'course':['math','compsci','physics']}
print(student)
print(student['name'])
print(student['age'])
print(student['course'])
print(student.get('name'))
#penambahan
student = {'name':'Kyle', 'age':19, 'course':['math','compsci','physics']}
student['phone'] = '111-1111-2222'
print(student.get('phone', 'not found'))
print(student)
#diganti
student = {'name':'Kyle', 'age':19, 'course':['math','compsci','physics']}
student.update({'name':'Cloe','age':15,'phone':'555-4444-6666'})
print(student)
#dihilangkan
student = {'name':'Kyle', 'age':19, 'course':['math','compsci','physics']}
del student['age']
print(student)
#banyak key
student = {'name':'Kyle', 'age':19, 'course':['math','compsci','physics']}
print(len(student))
#keys and values
student = {'name':'Kyle', 'age':19, 'course':['math','compsci','physics']}
print(student.keys())
print(student.values())
#items
student = {'name':'Kyle', 'age':19, 'course':['math','compsci','physics']}
print(student.items())
#loop
student = {'name':'Kyle', 'age':19, 'course':['math','compsci','physics']}
for key, value in student.items():
    print(key, value)




""" Conditionals and Boolean """

#Equal : () == ()
#Not equal : () != ()
#Greater than : () > ()
#Less than : () < ()
#Greater or equal : () >= ()
#Less or equal : () <= ()
#Object identity : is

#1
#if-else
language = 'Python'
if language == 'Python':
    print('Conditional is True')
else:
    print('error')

language = 'Java'
if language == 'Python':
    print('Conditional is True')
else:
    print('error')
#if-elif-else
language = 'Java'
if language == 'Python':
    print('Language is Python')
elif language == 'Java':
    print('Language is Java')
else:
    print('No Match')

#2
#and
user = 'Admin'
logged_in = True
if user == 'Admin' and logged_in:
    print('Admin Page')
else:
    print('Bad Creds')
#or
user = 'Admin'
logged_in = False
if user == 'Admin' or logged_in:
    print('Admin Page')
else:
    print('Bad Creds')
#not
user = 'Admin'
logged_in = True
if not logged_in:
    print('Please!')
else:
    print('Welcome!')

#3
#checking
a = [1,2,3]
b = [1,2,3]
print(id(a))
print(id(b))
print (a is b)
print (a == b)
#False values:
...# False
...# None
...# Zero of any numeric types
...# Any empty sequance. ex : '', (), []
...# Any empty mapping. ex : {}
condition = 0
if condition:
    print ('Evaluated to True')
else:
    print ('Evaluated to False')




""" Loops and Iterations """

#1
nums = [1,2,3,4,5]
for num in nums:
    print(num)
#loop and break statement
nums = [1,2,3,4,5]
for num in nums:
    if num == 3:
        print('found!')
        break 
    print(num)
#loop and continue 
nums = [1,2,3,4,5]
for num in nums:
    if num == 3:
        print('found!')
        continue
    print(num)
#loop in loop
nums = [1,2,3,4,5]
for num in nums:
    for letter in 'ab':
        print(num,letter)

#2
#range
for i in range(5):
    print(i)

for i in range(1,11):
    print (i)
#use conditional
x = 0
while x < 10:
    if x == 5:
        break
    print(x)
    x += 1

#3
x = 0
while True:
    if x == 100:
        break 
    print (x)
    x += 1




""" Function """

#1
#check
def hello_function():
    pass
print(hello_function())
#try
def hello_function():
    print('WKWKWK!')
hello_function()

def hello_func():
    return 'Hello!'
print(hello_func())
#loop
def hello_function():
    print('WKWKWK!')
hello_function()
hello_function()
hello_function()
#menggunakan parameter
def hello_func(greeting):
    return '{}'.format(greeting)
print(hello_func('Hi'))

def hello_func(greeting, name = 'You'):
    return '{}, {}'.format(greeting, name)
print(hello_func('Hi'))
#star
def student_info(*args,**kwargs):
    print(args)
    print(kwargs)
student_info('Math','CompSci', name='Letha', age=18)

#
def student_info(*args,**kwargs):
    print(args)
    print(kwargs)
course = ['Math','CompSci']
info = {'name':'Letha', 'age':18}
student_info(course,info)

#2 Example
#number of days per month. First value placeholder for indexing purpose
month_days = [0,31,28,31,30,31,30,31,31,30,31,30,31]
def is_leap(year):
    """ Return True for leap year, False for non-leap year"""
    return year %4 == 0 and (year %100 != 0 or year %400 == 0)

def days_in_month(year, month):
    """ Return number of days in that mont in that year"""
    if not 1 <= month <= 12:
        return 'Invalid Month'
    if month ==2 and is_leap(year):
        return 29
    return month_days[month]
print(is_leap(2020))
print(days_in_month(2017, 2))




""" Import Module """

import module
course = ['Math', 'History', 'Physics', 'CompSci']
index = module.find_index(course, 'Math')
print(index)

import module as m
course = ['Math', 'History', 'Physics', 'CompSci']
index = m.find_index(course, 'Math')
print(index)

from module import find_index
course = ['Math', 'History', 'Physics', 'CompSci']
index = find_index(course, 'Math')
print(index)

from module import find_index, test
course = ['Math', 'History', 'Physics', 'CompSci']
index = find_index(course, 'Math')
print(index)
print(test)

from module import *
course = ['Math', 'History', 'Physics', 'CompSci']
index = find_index(course, 'Math')
print(index)
print(test)



a = '1'
b = '2'
c = '3'

print('Hasil = ',a + b + c)

print('''Kesatuan Paragraf yang baik haruslah memiliki satu gagasan utama.
Artinya, dalam paragraf mungkin terdapat beberapa gagasan tambahan atau kalimat penjelas, tetapi gagasan-gagasan itu harus terfokus pada satu gagasan utama atau kalimat pokok sebagai pengendali.'''.split('\n') )

print('Jum\'at')