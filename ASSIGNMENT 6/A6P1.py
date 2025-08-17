import math
def area_circle():
    r=float(input("Enter the radius of the circle:"))
    return math.pi*r*r
def area_square():
    s=float(input("Enter the side of the square:"))
    return s*s
def area_rectangle():
    l=float(input("Enter the length of the rectangle:"))
    b=float(input("Enter the breadth of the rectangle:"))
    return l*b
def area_triangle():
    h=float(input("Enter the height of the triangle:"))
    b=float(input("Enter the base of the triangle:"))
    return 0.5*h*b    
flag=0
while flag==0:
    print("Area Calculator:")
    print("1.Circle")
    print("2.Square")
    print("3.Rectangle")
    print("4.Triangle")
    print("5.Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        print(f"The area of the circle is:{area_circle():.2f}")
    elif choice==2:
        print(f"The area of the square is:{area_square():.2f}")
    elif choice==3:
        print(f"The area of the rectangle is:{area_rectangle():.2f}")
    elif choice==4:
        print(f"The area of the triangle is:{area_triangle():.2f}")
    elif choice==5:
        print("Exiting")
        flag=1
    else:
        print("Invalid input.")
