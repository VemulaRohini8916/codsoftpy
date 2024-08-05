def add(a,b):
    return a+b;
def diff(a,b):
    return a-b;
def multiply(a,b):
    return a*b;
def division(a,b):
    if b==0:
        return "cannot divide by zero"
    else:
        return a/b;
def Calculator():
    while True:
        a=int(input("Enter first value: "))
        b=int(input("Enter second value: "))
        op=input("Enter an operator: ")
        if op=='+':
            print("Sum = "+add(a,b))
        elif op=='-':
            print("Subtraction: "+diff(a,b))
        elif op=='*':
            print("Multiplication: "+multiply(a,b)) 
        elif op=='/':
            print("Division: "+division(a,b))
        else:
            print("Invalid")           