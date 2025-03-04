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
