# This inputs math into the python code so that math.pi could function.
import math

# This part calculates the circumference. Just like the JS code, it reads the input and puts it into the variable and runs it through the string and then displaying on the console.
print("Please input radius for Circumference of a circle")
radiusC = int(input())
print (2 * math.pi * radiusC)
# Like before, it takes the input and runs it through the string and then prints displaying the area.
print("Please input radius for Area of a circle")
radiusA = int(input())
print (math.pi * radiusA * radiusA)
