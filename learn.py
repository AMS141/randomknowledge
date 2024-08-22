Num1=int(input("Enter first number: "))
Num2=int(input("Enter second number: "))
choice=input("Enter your operand: ")


if choice=="+":
    print("Result: ", Num1+Num2)
elif choice=="-":
    print("Result: ", Num1-Num2)
elif choice=="*":
    print("Result: ", Num1*Num2)
elif choice=="/":
    if Num2==0:
        print("Error: Cannot be divided by 0")
    else:
        print("Result: ", Num1/Num2)
elif choice=="%":
    print("Result: ", Num1%Num2)
else:
    print("Invalid Choice")
                       
