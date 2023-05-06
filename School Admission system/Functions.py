import csv ,os,time
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
    
    
    
    hellofile=open('C:\\Users\\USER\\Desktop\\site\\Python-Projects\\School Admission system\\admisson.csv','a',newline='')
    hello=csv.writer(hellofile,lineterminator='\n')
    count=input("assign Adm ")
    name=input('Students Name   ')
    standard=input("Enter Class ")
    age=input("Age  ")
    chckInt(age)
    listclass_1=[count,name,age,standard]
    hello.writerow(listclass_1)

    #print(helloContent)
    print('Student is Regstered')
    hellofile.close()

#checking class teacher and performance
def RegisterClassT():
    print('Registering class Teacher write cl\'class number' 'for example class 1  is written like cl1' )
    Myfile=open('C:\\Users\\USER\\Desktop\\site\\Python-Projects\\School Admission system\\clssteacherPerf\\ClassTeacher.csv','a')
    csvframe=csv.writer(Myfile)
    classTeacher_name=str(input('Class Teacher name'))
    Class_number=str(input('input class number'))
    listclass=[classTeacher_name,Class_number]
    csvframe.writerow(listclass)
    print('Class is Regstered')

    #csvframe.close()
def checkClass(p):
    with open('C:\\Users\\USER\\Desktop\\site\\Python-Projects\\School Admission system\\clssteacherPerf\\ClassTeacher.csv') as csvfile:
        readobj=csv.reader(csvfile)
        for row in readobj:
            for i in row:
                if i==p:
                    print(row)
   



def ChckClsandPerf():
    number=input("enter class of student")
    try:
        r=int(number)
        if 0<r<9 :
            print('Procedding to request')
            if r==1:
               hellofile=open('C:\\Users\\USER\\Desktop\\site\\Python-Projects\\School Admission system\\clssteacherPerf\\class1.txt')
                
            elif  r==2:
                hellofile=open('C:\\Users\\USER\\Desktop\\site\\Python-Projects\\School Admission system\\clssteacherPerf\\class2.txt')      
            elif  r==3:
                hellofile=open('C:\\Users\\USER\\Desktop\\site\\Python-Projects\\School Admission system\\clssteacherPerf\\class3.txt')              
            elif  r==4:
                hellofile=open('C:\\Users\\USER\\Desktop\\site\\Python-Projects\\School Admission system\\clssteacherPerf\\class4.txt')      
            elif  r==5:
                hellofile=open('C:\\Users\\USER\\Desktop\\site\\Python-Projects\\School Admission system\\clssteacherPerf\\class5.txt')      
            elif  r==6:
                hellofile=open('C:\\Users\\USER\\Desktop\\site\\Python-Projects\\School Admission system\\clssteacherPerf\\class6.txt')      
            elif  r==7:
                hellofile=open('C:\\Users\\USER\\Desktop\\site\\Python-Projects\\School Admission system\\clssteacherPerf\\class7.txt')      
            else:
                hellofile=open('C:\\Users\\USER\\Desktop\\site\\Python-Projects\\School Admission system\\clssteacherPerf\\class8.txt')
        else:
            print('enter valid number')
            
    except ValueError:
        print('enter any of the numbers shown')
        hellofile=open('C:\\Users\\USER\\Desktop\\site\\Python-Projects\\School Admission system\\admisson.txt','a')
        


              

 

 
#   main program  
def startupscreen(): 
    print(''' ********************************************************************************
                                    HARTI PRIMARY SCHOOL
                                    P.O. BOX 432 GATUNDU  
                    
                                WELCOME 
                                Here is our catalogue
                                1:Admitting new student
                                2:Check or Register class teacher
                                3:School transfer  ''')
def mainprogram():
    query1=input("Service Number    ")

    try:
        r=int(query1)
        if 0<r<4 :
            if r==1:
                print('      Procedding to request ... 1')
                NewAdmission()
                p=int(input('''
                            do you want to go back ? 
                            >to previous step enter 1 <,
                            >to main program enter 2 <<
                            >to exit enter 3 >
                            --------------------'''))
                if p==1:

                    NewAdmission()
                elif p==2:
                    mainprogram()
                else:
                    print('................')
            elif r==2:
                print('     Procedding to request ... 2')
                time.sleep(2)
                print('''   
                            >Check class Teacher Enter 1
                            >Register class Teacher Enter 2  ''')
                Resp=input('Enter Choice    ')
                try:
                    p=int(Resp)
                    if 0<p<3:
                        if p==1:
                            print('''
                                 To check class Teacher input class teacher\'s  
                                  class like for class one the class number is 1''')
                            time.sleep(2)
                            clp=input('Class number     ')
                            try:
                                f=int(clp)
                                if 0<f<9:
                                    o=str(f)
                                    p=('cl'+o)
                                    print(checkClass(p))

                                else:
                                    print('Enter any number within the valid range')
                            except ValueError:
                                print('Enter a  number')   

                        else:
                            print('Registering Class Teacher')
                            RegisterClassT()
                except ValueError:
                    print('Enter a  number')               
            
            else:
                print('     Procedding to request ... 3')
        
        else:
            print('enter valid number')
    except ValueError:
        print('enter any of the numbers shown')


startupscreen()
mainprogram()