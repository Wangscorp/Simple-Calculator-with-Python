print("How many times do you want to run your calculator")
times=int(input())
for i in range (times):
    print("The calculator accepts three values")
    print("Enter the first number")
    num1=float(input())
    print("Enter the computational sign")
    sign1=input()
    print("Enter the second number")
    num2=float(input())
    print("Enter the computational sign")
    sign2=input()
    print("Enter the third number")
    num3=float(input())
    #if the first sign is Addition
    if sign1=="+" and sign2=="+":
        Calc=num1+num2+num3
        print("Ans= {}".format(Calc))
    elif sign1=="+" and sign2=="-":
        Calc=num1+num2-num3
        print("Ans={}".format(Calc))
    elif sign1=="+" and sign2=="*":
        Calc=num1+num2*num3
        print("Ans={}".format(Calc))
    elif sign1=="+" and sign2=="/":
        Calc=num1+num2/num3
        print("Ans={}".format(Calc))
    elif sign1=="+" and sign2=="%":
        Calc=num1+num2%num3
        print("Ans={}".format(Calc))
    # If the first sign is Substracion
    elif sign1=="-" and sign2=="-":
        Calc=num1-num2-num3
        print("Ans={}".format(Calc))
    elif sign1=="-" and sign2=="+":
        Calc=num1-num2+num3
        print("Ans={}".format(Calc))
    elif sign1=="-" and sign2=="*":
        Calc=num1-num2*num3
        print("Ans={}".format(Calc))
    elif sign1=="-" and sign2=="/":
        Calc=num1-num2/num3
        print("Ans={}".format(Calc))
    elif sign1=="-" and sign2=="%":
        Calc=num1-num2%num3
        print("Ans={}".format(Calc))
    # If the first sign is Multiplication
    elif sign1=="*" and sign2=="*":
        Calc=num1*num2*num3
        print("Ans={}".format(Calc))
    elif sign1=="*" and sign2=="+":
        Calc=num1*num2+num3
        print("Ans={}".format(Calc))
    elif sign1=="*" and sign2=="-":
        Calc=num1*num2-num3
        print("Ans={}".format(Calc))
    elif sign1=="*" and sign2=="/":
        Calc=num1*num2/num3
        print("Ans={}".format(Calc))
    elif sign1=="*" and sign2=="%":
        Calc=num1*num2%num3
        print("Ans={}".format(Calc))
    # If the first sign is Division
    elif sign1=="/" and sign2=="/":
        Calc=num1/num2/num3
        print("Ans={}".format(Calc))
    elif sign1=="/" and sign2=="+":
        Calc=num1/num2+num3
        print("Ans={}".format(Calc))
    elif sign1=="/" and sign2=="-":
        Calc=num1/num2-num3
        print("Ans={}".format(Calc))
    elif sign1=="/" and sign2=="*":
        Calc=num1/num2*num3
        print("Ans={}".format(Calc))
    elif sign1=="/" and sign2=="%":
        Calc=num1/num2%num3
        print("Ans={}".format(Calc))
    #If the first sign is Modulus
    elif sign1=="%" and sign2=="%":
        Calc=num1%num2%num3
        print("Ans={}".format(Calc))
    elif sign1=="%" and sign2=="+":
        Calc=num1%num2+num3
        print("Ans={}".format(Calc))
    elif sign1=="%" and sign2=="-":
        Calc=num1%num2-num3
        print("Ans={}".format(Calc))
    elif sign1=="%" and sign2=="/":
        Calc=num1%num2/num3
        print("Ans={}".format(Calc))
    elif sign1=="%" and sign2=="*":
        Calc=num1%num2*num3
        print("Ans={}".format(Calc))
    else:
        print("Invalid Sign")
