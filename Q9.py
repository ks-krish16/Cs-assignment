'''
Name= Krish Sharma
Class= XI-G
Roll no.= 24
Question 9
'''
#Write a program to calculate in how many days a work will be completed by 3 workers

A=float(input("number of days taken by worker A: "))
B=float(input("number of days taken by worker B: "))
C=float(input("number of days taken by worker C: "))

result= (A*B*C)/((A*B)+(B*C)+(A*C))
print("Total number of days taken by workers A B and C: ",result)
