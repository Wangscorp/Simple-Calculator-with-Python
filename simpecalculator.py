#"This is a basic calculator with python"
x=float(input("Enter the first number "))
sign1=input("Enter the operation sign")
y=float(input("Enter the second number "))
sign2=input("Enter the operation sign")
z=float(input("Enter the third number "))
#  if Addition is the first sign
if sign1=="+" and sign2=="+":
    calc=x+y+z
    print("Ans is {}".format(calc))
elif sign1=="+" and sign2=="-":
    calc=x+y-z
    print("Ans is {}".format(calc))
elif sign1=="+" and sign2=="*":
    calc=x+y*z
    print("Ans is {}".format(calc))
elif sign1=="+" and sign2=="/":
    calc=x+y/z
    print("Ans is {}".format(calc))
elif sign1=="+" and sign2=="%":
    calc=x+y%z
    print("Ans is {}".format(calc))
#  if Subtraction is the first sign
elif sign1=="-" and sign2=="-":
    calc=x-y-z
    print("Ans is {}".format(calc))
elif sign1=="-" and sign2=="*":
    calc=x-y*z
    print("Ans is {}".format(calc))
elif sign1=="-" and sign2=="/":
    calc=x-y/z
    print("Ans is {}".format(calc))
elif sign1=="-" and sign2=="+":
    calc=x-y+z
    print("Ans is {}".format(calc))
elif sign1=="-" and sign2=="%":
    calc=x-y%z
    print("Ans is {}".format(calc))
#  if Multiplication is the first sign
elif sign1=="*" and sign2=="*":
    calc=x*y*z
    print("Ans is {}".format(calc))
elif sign1=="*" and sign2=="-":
    calc=x*y-z
    print("Ans is {}".format(calc))
elif sign1=="*" and sign2=="/":
    calc=x*y/z
    print("Ans is {}".format(calc))
elif sign1=="*" and sign2=="+":
    calc=x*y+z
    print("Ans is {}".format(calc))
elif sign1=="*" and sign2=="%":
    calc=x*y+z
    print("Ans is {}".format(calc))
# if division is the first sign
elif sign1=="/" and sign2=="/":
    calc=x/y/z
    print("Ans is {}".format(calc))
elif sign1=="/" and sign2=="+":
    calc=x/y+z
    print("Ans is {}".format(calc))
elif sign1=="/" and sign2=="-":
    calc=x/y-z
    print("Ans is {}".format(calc))
elif sign1=="/" and sign2=="*":
    calc=x/y*z
    print("Ans is {}".format(calc))
elif sign1=="/" and sign2=="%":
    calc=x/y%z
    print("Ans is{}".format(calc))
#  if Modulus is the first sign
elif sign1=="%" and sign2=="%":
    calc=x%y%z
    print("Ans is {}".format(calc))
elif sign1=="%" and sign2=="+":
    calc=x%y+z
    print("Ans is {}".format(calc))
elif sign1=="%" and sign2=="-":
    calc=x%y-z
    print("Ans is {}".format(calc))
elif sign1=="%" and sign2=="*":
    calc=x%y*z
    print("Ans is {}".format(calc))
elif sign1=="%" and sign2=="/":
    calc=x%y/z
    print("Ans is {}".format(calc))    
#Made by Wanyoike Ngigi Kenya(Wang's) "The Man you were destined to be is the man you decide to be"