import math
#THis is the formula of pi
π = 3.14159

#This is the input for the radius of the sphere
r = int(input("Please enter the radius of the Sphere:"))

#This is the formula for the sphere
sphere = 4/3*π*r**3

print("The area of your sphere is ")
print(sphere)

a = float(input("Please enter the length of the side of the cube: "))  # Convert input to float
cube = a ** 3  # Calculate the volume of the cube

print("The volume of the cube is:")
print(cube)
#The equation of the cone
cone = 1/3*π*r
# The H value of the cylinder equation.
h = int(input("Please enter the height of Cylinder"))
# The X value of the cylinder equation
x = int(input("Please enter the radius of the Cylinder"))
# The equation of the cylinder
cylinder = π*x**2*h

print("The volume of the sphere is: ")
print(sphere)
print("The volume of the cube: ")
print(cube)
print("The volume of the cylinder is: ")
print(cylinder)

