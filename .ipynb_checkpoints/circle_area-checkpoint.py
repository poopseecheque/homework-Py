# importing the math package first to be able to use the PI constant
import math

radius = int(input("Input circle radius: " ))
# pivalue = float(3.141592653589793)

if radius >= 0:
  print("cicle area =", math.pi*radius*radius) # changed pivalue to math.pi
else:
  print("radius must be a non-negative number")