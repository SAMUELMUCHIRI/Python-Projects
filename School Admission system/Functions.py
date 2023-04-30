import csv ,os
import pandas as pd
count=0

# declaring the function body 
def chckInt(number):
    try:
        int1=int(number)
        
    except ValueError:
        print('enter any of the numbers shown')
def chckInt2(number):
    try:
        r=int(number)
        if 0<r<4 :
            print('Procedding to request')
        else:
            print('enter valid number')
            
    except ValueError:
        print('enter any of the numbers shown')
def NewAdmission():
    count=input("assign Adm ")
    name=input('Students Name   ')
    age=input("Age  ")
    chckInt(age)
    
    standard=input("Enter Class ")
    hellofile=open('C:\\Users\\USER\\Desktop\\site\\Python-Projects\\School Admission system\\admisson.txt','a')
    helloContent=hellofile.write(count+'    '+name+'        '+age+'     '+standard+"\n")

    print(helloContent)
    hellofile.close()

def ChckClsandPerf():
        hellofile=open('C:\\Users\\USER\\Desktop\\site\\Python-Projects\\School Admission system\\admisson.txt','a')
        


              

 

 
#   main program   
print(''' ********************************************************************************
                                  HARTI PRIMARY SCHOOL
                                  P.O. BOX 432 GATUNDU  
                
                            WELCOME 
                               Here is our catalogue
                             1:Admitting new student
                             2:Check class teacher and perfomance
                             3:School transfer  ''')
query1=input("Service Number")
try:
    r=int(query1)
    if 0<r<4 :
        if r==1:
           print('Procedding to request ... 1')
           NewAdmission()
        elif r==2:
            print('Procedding to request ... 2')
        else:
            print('Procedding to request ... 3')
        
    else:
        print('enter valid number')
except ValueError:
    print('enter any of the numbers shown')


