x = input("Enter the 1st number")
y = input("Enter the 2nd number")
z = input("Enter the 3rd number")
if x > y and x > z:
    print(f"({x}is the largest of the three)")
elif y > x and y > z:
    print(f"({y}is the largest of the three)")
elif z > x and z > y:
    print(f"({z}is the largest of the three)")
