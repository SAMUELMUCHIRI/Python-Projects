import csv 
import re
import pandas as pd

'''csvframe=pd.read_csv('C:\\Users\\USER\\Desktop\\site\\Python-Projects\\School Admission system\\clssteacherPerf\\test.csv',sep=',')
for row in csvframe:
    for i in row:
        if i=='CAT':
            print(row)'''

with open('test.csv') as f:
    f_csv = csv.reader(f)
    #headers = next(f_csv)
    for row in f_csv:
        for i in row:
             if i=='CAT':
                
                g=pd.DataFrame(['Symbol','Price','Date','Time','Change','Volume'])
                t=pd.DataFrame([row])
                g=pd.concat(t)
                csvframe=pd.read_csv('C:\\Users\\USER\\Desktop\\site\\Python-Projects\\School Admission system\\clssteacherPerf\\result.csv',sep=',')
                g.to_csv('C:\\Users\\USER\\Desktop\\site\\Python-Projects\\School Admission system\\clssteacherPerf\\result.csv',',')
                
'''t=pd.read_csv('C:\\Users\\USER\\Desktop\\site\\Python-Projects\\School Admission system\\clssteacherPerf\\result.csv')  
print(t)'''