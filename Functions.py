import time
print(time.gmtime())#tupil define
time.time()
print(time.gmtime(200000))
time.asctime() #current time
print(time.asctime()) #accept all perameter

print(time.asctime(time.gmtime()))
print(time.ctime(1500000))
print(time.localtime())

from datetime import date
print(date.today()) #today date
print(date.fromtimestamp(3452435)) #to send hidden date for that we use timestamp

import os
print(os.getcwd())#current working directory
print(os.environ)#dictionary element

#ASSIGNMENT
import datetime
a= "1970-12-12"
d=datetime.datetime.strptime(a,"%Y-%m-%d")
print(d.month)

import datetime
a="2012-5-4"
