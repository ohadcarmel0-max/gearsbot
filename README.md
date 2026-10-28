print("1 add\n2 sutratc\n3 multiply\n4 divide")
def caculate():
    action = int(input("please Pick action 1-4\n"))
    if action > 4:
        print("This is not an action!")
        caculate()
    num1 = int(input("enter your first number "))
    num2 = int(input("enter your second number "))

    if action == 1:
        print(num1,"+",num2,"=",num1+num2)
    elif action == 2:
        print(num1,"-",num2,"=",num1 - num2)
    elif action == 3:
        print(num1,"*",num2,"=",num1 * num2)
    elif action == 4:
        if num2 == 0:
            print("You cannot divide by zero")
            caculate()
        print(num1,"/",num2,"=",num1/num2)
    caculate()

caculate()
     print(num1,"/",num2,"=",num1/num2)
