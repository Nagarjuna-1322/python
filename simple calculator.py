


# simple calculator

a = float(input("enter the first number"))
op = input("enter the operators(+,-,*,/):")
b = float(input("enter the second number"))


if op=="+":
    print(a+b)
    
elif op== "-":
    print(a-b)
    
elif op =="*":
    print(a*b)
    
elif op=="/":
    print(a/b)
    
else:
    
    print("invalid operator")