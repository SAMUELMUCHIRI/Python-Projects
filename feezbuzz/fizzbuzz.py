#first solution
for i in range(1,101):
    if i%3==0 and i%5==0:
        print("feezbuz")
    elif i%3==0:
        print("feez")
    elif i%5==0:
        print("buzz")
    else:
        print(i)
#second solution 
for i in range(1,101):
    print("feez"*(i%3<1)+(i%5<1)*"buzz" or i)
def feezbuzz(x):
    st=0
    while st<x:
        if st%15==0:
            print("feezbuzz")
        elif st%3==0:
            print("feez")
        elif st%5==0:
            print("buzz")
        else:
            print(st)
        st=st+1
        #just regulat checkup for now ..
feezbuzz(100)
