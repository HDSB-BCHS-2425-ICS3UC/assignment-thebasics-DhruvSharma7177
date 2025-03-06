# Part 1 - User Input

# Integer Whole number
integer = int(input("Enter an integer: "))
# Output the value and type of integer
print("Integer:", integer)

# Float type: Decimal number
float_num = float(input("Enter a float number: "))
# Output the value and type of float
print("Float:", float_num)

# String type: A sequence of characters
string = input("Enter a string: ")
# Output the value and type of string
print("String:", string)

# Boolean type: True or False value
boolean_input = input("Enter a boolean value (True/False): ")
boolean = boolean_input.lower() == 'true'
# Output the value and type of boolean
print("Boolean:", boolean)

#Part 2
import math
# Addition:
num1 = float(input("First number for the sum: "))
num2 = float(input("Second number for the sum: "))
sum_result = num1 + num2
print(sum_result)

# Subtraction:
num3 = float(input("First number for subtraction: "))
num4 = float(input("Second number for subtraction: "))
difference_result = num3 - num4
print(difference_result)

# Multiplication:
num5 = float(input("First number for multiplication: "))
num6 = float(input("Second number for multiplication: "))
product_result = num5 * num6
print(product_result)

# Division: divides the first number by the second
num7 = float(input("First number for division: "))
num8 = float(input("Second number for division: "))
division_result = num7 / num8
print(division_result)

# Modulus: returns the remainder of a division
num9 = float(input("First number for modulus: "))
num10 = float(input("Second number for modulus: "))
modulus_result = num9 % num10
print(modulus_result)

#Part 3

# Program to calculate the Discriminant (Delta)
# Taking inputs
a = float(input("Enter amount A : "))
b = float(input("Enter amount B : "))
c = float(input("Enter amount C : "))
# Calculating the discriminant
delta = b**2 - 4*a*c
# Displaying the result
print(f"The Discriminant is: {delta}")

#Part 4

# Cube
print("Calculate the volume of a Cube")
a = float(input("Enter the length of the cube's edge: "))
volume_cube = a**3
print(volume_cube)

# Sphere
print("Calculate the volume of a Sphere")
r_sphere = float(input("Enter the radius of the sphere: "))
volume_sphere = (4/3) * math.pi * r_sphere**3
print(volume_sphere)

# Cone
print("Calculate the volume of a Cone")
r_cone = float(input("Radius of the base of the cone: "))
h_cone = float(input("Height of the cone: "))
volume_cone = (1/3) * math.pi * r_cone**2 * h_cone
print(volume_cone)

# Cylinder
print("Calculate the volume of a Cylinder")
r_cylinder = float(input("Radius of the base of the cylinder: "))
h_cylinder = float(input("Height of the cylinder: "))
volume_cylinder = math.pi * r_cylinder**2 * h_cylinder
print(volume_cylinder)

