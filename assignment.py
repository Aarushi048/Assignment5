#Q1
print("question 1")
f=open("test1.txt",encoding="utf8")
a=(f.readlines())
a.reverse()
n=int(input("Enter number of line:"))
for i in range(0,n):
    print(a[i])
f.close()
print("")

#Q2
print("question 2")
a="o"
f=open("test2.txt","r")
z=f.read()
m=z.split()
print(z.count(a))
print("")

#Q3
try:
  e=open("test1.txt", encoding="utf8")
  h=open("test3.txt","r+")
  h.writelines(wordstring)
  e.close()
  h.close()
  print("COPY OPERATION PERFORMED")
except Exception:
  print("")

#Q4
print("question 4:")
a= open("test4.txt", "r+")
b = open("test2.txt", "r+")
print("Combined Lines:")
for line1, line2 in zip(a,b):
    print(line2+line1,end="")
a.close()
a.close()
print("")

#Q5
print("question 5")
import random
list=[]
sortedlist=[]
for i in range(0,10):
    list.append(random.randint(1,10))
f=open("test.txt","w")
for s in list:
    r="".join(str(s))
    f.write(r)
f.close()
f1=open("test5.txt","r")
t=f1.read()
for u in t:
    if(u.isdigit()):
        v="".join(u)
        sortedlist.append(v)
sortedlist.sort()
w=open("Sorted.txt","w")
w.write(str(sortedlist))
f.close()
print("")
print("Sorted")