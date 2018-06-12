
#Q1

i=0
while(i<10):
    num=input("enter your no:")
    print("enter no is"+num)
    i=i+1
#Q2

i=0
while("true"):
    print("infinite")

#Q3
num=[]
sq=[]
for i in range(0,5):
    x=int(input("enter the num"))
    num.append(x)
print(num)
for x in num:
    k=x*x
    sq.append(k)
print(sq)
#Q4 form a list for integer,float and string
i=()
l=[1,2,"abc",2.0]
a=[]
b=[]
c=[]
for i in l:
  if(type(i)==int):
    a.append(i)
  elif(type(i)==str):
      b.append(i)
  else:
      c.append(i)
print(a)
print(b)
print(c)



#Q5 using range(1,101),make a list contaning even and odd numbers


odd =[]
even =[]
for num in range(1 , 101):
    if (num %2 ==0):
        even.append(num)
    else:
     odd .append(num)
print("even no:", even)
print("odd no:", odd)

#Q6 print patterns
i=1
for i in  range (0,5):
    for j in range(0,i+1):
           print("*",end="")
    print()
    

#Q7 creat a user defined dictionary and get keys corresponding to the value using for loop

#        i=0
a={'name':'aaru','age':21,'roll no':1123}
for i in a:
    print(i,a[i])

#Q8 perform inputs and search and deletion from user in a list
i=0
c=[]
while(i<5):
    a=int(input("enter number"))
    c.append(a)
    i=i+1
a=int(input("enter number to be searched"))
for i in c:
     if(a==i):
        c.remove(i)
print(c)







