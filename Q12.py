import math
print("(a)")
print("Length of the ladder= 16 feet")
print("Angle formed= 75 degrees")
num1=16
num2=75

radian= math.radians(num2)
sin= math.sin(radian)
result1= round(num1 * sin,2)
print("Heigth of the wall(in feet) is: ",result1)

print("(b)")
print("Length of the ladder= 20 feet")
print("Angle formed= 0 degrees")
num3=20
num4=0

radian= math.radians(num4)
sin= math.sin(radian)
result2= round(num3 * sin,4)
print("Heigth of the wall(in feet) is: ",result2)

print("(c)")
print("Length of the ladder= 24 feet")
print("Angle formed= 45 degrees")
num5=24
num6=45

radian= math.radians(num6)
sin= math.sin(radian)
result3= round(num5 * sin,6)
print("Heigth of the wall(in feet) is: ",result3)

print("(d)")
print("Length of the ladder= 24  feet")
print("Angle formed= 80 degrees")
num7=24
num8=80
radian= math.radians(num8)
sin= math.sin(radian)
result4= round(num7 * sin,8)
print("Heigth of the wall(in feet) is: ",result4)

