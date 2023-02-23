def feezbuzz(x):
    for i in range(1,x):
        print("feez"*(i%3<1)+(i%5<1)*"buzz" or i)
feezbuzz(100)
