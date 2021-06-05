'''
Name= Krish Sharma
Class= XI-G
Roll no.= 24
Question 6
'''
#Write a program to calculate the simple interest and amount

num1=float(input(" Enter the Principle Amount: "))
num2=float(input("Enter the Rate of Interest: "))
num3=float(input("Enter Time: "))

SI= num1 * num2 * num3/100
print("Simple Interest is: ",SI)

amount= num1+SI
print("Amount is: ",amount)
