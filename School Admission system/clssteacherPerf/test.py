import pandas as pd
import csv
def test():
  p=input('class number')
  with open('C:\\Users\\USER\\Desktop\\site\\Python-Projects\\School Admission system\\clssteacherPerf\\ClassTeacher.csv') as csvfile:
      readobj=csv.reader(csvfile)
      for row in readobj:
          for i in row:
            if i==p:
              print(row)

def deleterow(w,j):
    print('undoing changes to file')
    data=pd.read_csv(w,encoding='utf-8')
    data.set_index('Name')
    data.drop(['008','David Kimani','9','cl3'])
    '''with open(w) as file:
       
       rt=csv.reader(file)
       for row in file:
            for i in row:
                if i==j:
                  p=j '''
                  
                  

                  
                  
                    #df=pd.read_csv(w)
                    #rt.drop(row)

w='C:\\Users\\USER\\Desktop\\site\\Python-Projects\\School Admission system\\admisson.csv'
j='Casey Njoki'
deleterow(w,j)