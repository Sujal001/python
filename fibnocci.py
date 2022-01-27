x= int(input("The range of fibnocci series is"))
a=0
b=1
count=0
if x<=0:
    print("please enter a positive no.")
elif x==1:
    print("the fibnocci series is ",a)
else:
    print("Fibnocci series", end ="")
    while count<=x:
        print(a,end= "")
        y=a+b
        a=b
        b=y
        count+= 1
