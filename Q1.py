"""
Name= Krish Sharma
Class= XI-G
Roll no.= 24

Question 1
"""
num1=int(input("Enter the First number: "))
num2=int(input("Enter the Second number: "))

print("Enter which operation would you like to perform : ")
ch=input("Enter any of these char for specific operations +,-,*,/,%,//,** :")

result= 0
if ch == '+':
    result= num1+num2
elif ch == '-':
    result= num1-num2
elif ch == '*':    
    result= num1*num2
elif ch == '/':
    result= num1/num2
elif ch == '%':
    result= num1%num2
elif ch == '//':
    result= num1//num2
elif ch == '**':
    result= num1**num2
else:
    print("Input character not recognised!")

print(num1, ch , num2, ":", result)
