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
    count=0
    name=input('Students Name')
    age=input("Age")
    chckInt(age)
    
    standard=input("Enter Class")
    path=os.getcwd
    with open('admisson.csv','w' , newline='') as file:
        writer=csv.writer(file)
        writer.writerow([ name, age,standard])
              

 

 
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
NewAdmission()