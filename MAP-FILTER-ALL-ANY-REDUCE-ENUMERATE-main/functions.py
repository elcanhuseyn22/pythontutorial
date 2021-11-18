#map() function------------------
list1=[1,2,3,4,5]
list2=[6,7,8,9,10]
list3=[11,12,13,14,15]
#print(list(map(lambda i,j,k:i*j*k,list1,list2,list3)))
#-----------------------------------------------------
#reduce function---------------------

from functools import reduce

def sum(x,y):
    return x+y #only 2 arguments accept
#print(reduce(lambda x,y:x*y,[1,2,3,4,5]))

def max(a,b):
    if a>b:
        return a
    else:
        return b

#print(reduce(max,[1,2,3,4,5,-1,-4]))
liste1=[1,2,3,4,5,6,7,8,9,10]
a=list(filter(lambda x:x%2==0,liste1))


b=reduce(lambda x,y:x+y,a)
#print(b)
#++++++++++++++++++++++++++++++++++++++++
#filter() function
#print(list(filter(lambda x:x%2==0,[1,2,3,4,5,6,7,8])))

def a(x):
    if x==1:
        return False
    elif x==2:
        return True
    else:
        for i in range(2,x):
            if x%i==0:
                return False
        return True


#print(list(filter(a,range(1,101))))
list12= [(3,4,5),(6,8,10),(3,10,7)]

def triangle(a):
    if abs(a[1]-a[2]) < a[0] < a[1]+a[2] and a[0] - a[2] < a[1] < a[0] + a[2] and a[0]-a[1]< a[2]<a[0]+a[1]:
        return True
    else:
        return False

#print(list(filter(triangle,list12)))

#enumerate() function

list4=["apple","grenade","bananna","kiwy"]

i=0
result=list()
while i<len(list4):
    result.append((i,list4[i]))
    i+=1

#print(list(enumerate(list4)))

#all and any functions

def all(list5):
    for i in list5:
        if not i:
            return False

    return True

list5=[False,True,True,False]
#print(all(list5))

#zip() function ======================================

isimler = ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]

soyisimler = ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]

for i,j in zip(isimler,soyisimler):
    print(i,j)
