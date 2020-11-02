shape = input("Which shape?: ")
if(shape == "square" or shape == "Square"): #Square
    side = float(input("What is the length of a side?: "))
    per = side*4
    area = side**2
    print("The area is", area, "and the perimeter is", per)
    print("The ratio between the perimeter and area is:", round(per/area, 4))

if(shape == "rectangle" or shape == "Rectangle"): #Rectangle
    sideA = float(input("What is the width of the rectangle?: "))
    sideB = float(input("What is the height of the rectangle?: "))
    per = sideA*2 + sideB*2
    area = sideA*sideB
    print("The area is", area, "and the perimeter is", per)
    print("The ratio between the perimeter and area is:", round(per/area, 4))

