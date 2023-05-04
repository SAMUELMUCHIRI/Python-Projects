from dataclasses import make_dataclass
import csv 
import re
import pandas as pd

csvframe=pd.read_csv('C:\\Users\\USER\\Desktop\\site\\Python-Projects\\School Admission system\\clssteacherPerf\\test.csv',sep=',')
for row in csvframe:
    for i in row:
        if i=='CAT':
            k=pd.dataframes[i]
            k.to_csv('C:\\Users\\USER\\Desktop\\site\\Python-Projects\\School Admission system\\clssteacherPerf\\result.csv' +name[i] + ".csv" ,index= False)  
             
'''for j in range(101):
    x = dataframes[j]
    x.to_csv(path + name[j] + ".csv", index = False)
            print(row)'''

'''point=make_dataclass("Point",[("Symbol",str),("Price",str),("Date",str),("Time",str),("Change",str),("Volume",str)])

f=open('test.csv')
f_csv = csv.reader(f)
#headers = next(f_csv)
for row in f_csv:
    for i in row:
        if i=='CAT':
                
            g={'Symbol':[0] ,'Price':[0] ,'Date':[0],'Time':[0],'Change':[0],'Volume':[0]}
            k=pd.DataFrame(data=g)
            t=pd.DataFrame([row])
            
            y=pd.DataFrame([point(t[0],t[1],t[2],t[3],t[4],t[5])])
            print(y)
            csvframe=pd.read_csv('C:\\Users\\USER\\Desktop\\site\\Python-Projects\\School Admission system\\clssteacherPerf\\result.csv',sep=',')
            t.to_csv('C:\\Users\\USER\\Desktop\\site\\Python-Projects\\School Admission system\\clssteacherPerf\\result.csv',index=False,header=False)'''
                
'''t=pd.read_csv('C:\\Users\\USER\\Desktop\\site\\Python-Projects\\School Admission system\\clssteacherPerf\\result.csv')  
            print(t)'''
            