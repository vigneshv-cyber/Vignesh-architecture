counter=1
a=int(input("Enter the number 1 -- "))
counter=counter+1
b = int(input("Enter the number 2 --"))
counter=counter+1
print("1-Addition 2-Subtraction 3-Multiplication 4-Division");
print("Enter your choice: ")
choice=int(input())
if choice==1:
    print("Performing Addition...")
    res=a+b
    counter=counter+1
if choice==2:
    print("Performing Subtraction...")
    res=a-b
    counter=counter+1
if choice==3:
    print("Performing Multiplication")
    res=a*b
    counter=counter+1
if choice==4:
    if b==0:
        print("Denominator can't be Zero")
    print("Perfroming Division...")
    res=a/b
    counter=counter+1
if choice>=5:
    print("Enter the correct Input")
print(res)
counter=counter+1
print("CYCLE VALUE IS: ",counter)
ins=int(input("Enter the no.of instructions: "))
performance_measure=ins/counter
print("Performance measure is : ",performance_measure)
