import pandas as pd
import csv
p=input('class number')
with open('C:\\Users\\USER\\Desktop\\site\\Python-Projects\\School Admission system\\clssteacherPerf\\ClassTeacher.csv') as csvfile:
    readobj=csv.reader(csvfile)
    for row in readobj:
        for i in row:
          if i==p:
            print(row)