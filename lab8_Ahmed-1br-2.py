"""
Program Name: Geometry Calculator
Author: Ahmed Ibrahim
Purpose: Provides a menu for calculating the area and perimeter/circumference of circles and rectangles.
Starter code: None
Date: September 27, 2026
"""

import circle as c
import rectangle as r
#Aliases are important to help distinguish between functions with the same name in different modules,
#since they both have calc_area functions

while True:
    print("\nGeometry Calculator")
    print("---------------------")
    print("1. Calculate Circle Area")
    print("2. Calculate Circle Circumference")
    print("3. Calculate Rectangle Area")
    print("4. Calculate Rectangle Perimeter")
    print("5. Exit")
    choice = input("\nEnter your choice (1-5): ")

    if choice == "1":
        radius = float(input("Enter the radius of the circle: "))
        area = c.calc_area(radius)
        print(f"The area of the circle is {area}.")
        input("\nPress Enter to continue...")
    elif choice == "2":
        radius = float(input("Enter the radius of the circle: "))
        circumference = c.calc_circumference(radius)
        print(f"The circumference of the circle is {circumference}.")
        input("\nPress Enter to continue...")
    elif choice == "3":
        width = float(input("Enter the width of the rectangle: "))
        height = float(input("Enter the height of the rectangle: "))
        area = r.calc_area(width, height)
        print(f"The area of the rectangle is {area}.")
        input("\nPress Enter to continue...")
    elif choice == "4":
        width = float(input("Enter the width of the rectangle: "))
        height = float(input("Enter the height of the rectangle: "))
        perimeter = r.calc_perimeter(width, height)
        print(f"The perimeter of the rectangle is {perimeter}.")
        input("\nPress Enter to continue...")
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")