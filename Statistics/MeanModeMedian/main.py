hellofile=open('C:\\Users\\USER\\Desktop\\site\\Python-Projects\\School Admission system\\admisson.txt')
helloContent = hellofile.read()
print(helloContent)
hellofile.close()
hellofile=open('C:\\Users\\USER\\Desktop\\site\\Python-Projects\\School Admission system\\admisson.txt','a')
p=input("no")
helloContent=hellofile.write(p+"\n")

print(helloContent)
hellofile.close()