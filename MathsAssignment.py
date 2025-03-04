import math

#Part 1

# Integer Whole number
integer = 5 
# Output the type of integer
print(integer)

# Float type: Decimal number
float = 5.5 
# Output the type of float
print(float)

# String type: A sequence of characters
string = ("Hello, World!") 
# Output the type of string
print(string)

# Boolean type: True or False value
boolean = True
# Output the type of boolean
print(boolean)

# Part 2

# Addition operation: Adds two numbers
addition = 5 + 3  
print(addition)

# Subtraction operation: Subtracts the second number from the first
subtraction = 10 - 4  
print(subtraction)

# Multiplication operation: Multiplies two numbers
multiplication = 6 * 2
print(multiplication)

# Division operation: Divides the first number by the second
division = 8 / 4 
print(division)

# Part 3: Discriminant Calculation

# Input values for the discriminant formula
a = 1  
b = 5  
c = 6  

# Calculate the discriminant (Delta)
delta = b**2 - 4*a*c  
# Output the discriminant result
print("The discriminant (Delta) is:", delta)


# Part 4

# 1. Cube Volume (V = side^3)

side_length = int(input("Enter the length of the side of the cube: "))
cube_volume = side_length**3

# Output the volume of the cube
print(f"The volume of the cube with side length {side_length} is: {cube_volume}")
pi = 3.141592653589793238462643383279502884197
# 2. Sphere Volume (V = 4/3 * pi * radius^3)
# Take input for the radius of the sphere
radius = input("Enter the radius of the sphere: ")  # No conversion to float
sphere_volume = (4/3) * pi * (int(radius)**3)  # Convert radius inside the formula

# Corrected print statement to display radius and sphere volume
print(f"The volume of the sphere with radius {radius} is: {sphere_volume}")

# 3. Cylinder Volume (V = pi * radius^2 * height)
height = int(input("Enter the height of the cylinder: "))
cylinder_volume = pi * (int(radius)**2) * height  # Formula: Volume of cylinder = pi * radius^2 * height
print(f"The volume of the cylinder with radius {radius} and height {height} is: {cylinder_volume}")
