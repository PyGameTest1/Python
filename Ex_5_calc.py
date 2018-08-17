# CALCULATOR

'''

a=float(input("Num1 = "))
b=float(input("Num2 = "))
sign=input("SignOfOperation = ")

if sign=="+":
    print(a+b)
elif sign=="-":
    print(a-b)
elif sign=="*":
    print(a*b)
elif sign=="/":
    print(a/b)
else:
    print("TheWrongSignOfOperation")

# or
print("or")
print("1)+\n2)-\n3)*\n4)/")
a=float(input("Num1 = "))
b=float(input("Num2 = "))
sign=int(input("NumberOfSignOfOperation = "))

if sign==1:
    print(a+b)
elif sign==2:
    print(a-b)
elif sign==3:
    print(a*b)
elif sign==4:
    print(a/b)
else:
    print("TheWrongSignOfOperation")

'''

# or
print("or")
print("1)+\n2)-\n3)*\n4)/")
sign=int(input("NumberOfSignOfOperation = "))
if sign==1:
    print("x+y=z")
    x=float(input("Num1 = "))
    y=float(input("Num2 = "))
    z=x+y
    print("Answer: "+str(z))
print("1)+\n2)-\n3)*\n4)/")
sign=int(input("NumberOfSignOfOperation = "))
elif sign==2:
    print("x-y=z")
    x=float(input("Num1 = "))
    y=float(input("Num2 = "))
    z=x-y
    print("Answer: "+str(z))
print("1)+\n2)-\n3)*\n4)/")
sign=int(input("NumberOfSignOfOperation = "))
elif sign==3:
    print("x*y=z")
    x=float(input("Num1 = "))
    y=float(input("Num2 = "))
    z=x*y
    print("Answer: "+str(z))
print("1)+\n2)-\n3)*\n4)/")
sign=int(input("NumberOfSignOfOperation = "))
elif sign==4:
    print("x/y=z")
    x=float(input("Num1 = "))
    y=float(input("Num2 = "))
    z=x/y
    print("Answer: "+str(z))
else:
    print("Debil")

