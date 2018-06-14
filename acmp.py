#Q1 time tuple
'''This is a module that provide various time related functions,has a tuple of 9 numbers
ie index  Attributes         values

   0   4-digit year  (2008)
   1   month         (1 to 12)
   2   Day           (1 to 31)
   3   Hour          (0 to 23)
   4   Minute        (0 to 59)
   5   second        (0 t0 59)
   6   Day of week   (0 to 6)
   7   Day of year   (-1 to 366 )
   8   Daylight saving (-1,0,1 where -1 means library determines DST


'''
#Q2 to get a formitted time
from datetime import date
print(date.fromtimestamp(456789))
#Q3 extract month from the time
from datetime import date
print(date.today()) #To extracrt today date

#Q4 extract day from the time
import datetime
from datetime import date
a="1996-08-13"
d=datetime.datetime.strptime(a,"%Y-%m-%d")
print(d.day)

#Q5 extract date(ex:11in11/01/2021)from the time.
import datetime
a="2021-01-11"
d=datetime.datetime.strptime(a,"%Y-%m-%d")
print(d.day)

#Q6 print time using localtime method
import time
print(time.localtime())

#Q7 factorial of a number input by user using math package functions
a=int(input("enter a:"))
import math
math.factorial(a)
print(math.factorial(a))

#Q8 GCD of an. input by user using math package functions
a=int(input("enter a:"))
b=int(input("enter b:"))
import math
math.gcd(a,b)
print(math.gcd(a,b))

#Q9 using os package
import os
print(os.getcwd()) # to get current working directory.
print(os.environ) # to get the user environment