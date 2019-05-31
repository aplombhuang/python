def main():

    cont = "Y"
    while (cont == "Y"):
        height = eval(input("Enter the height."))
        width = eval(input("Enter the width."))

        if (height > 0 and width > 0):
            print("The area of the rectangle is", getArea(height, width))
            print("The perimeter of the rectangle is", getPerimeter(height, width))

        cont = input("Do you want to continue?")
    # end while
# end main

def getArea(height, width):
    return height * width

# end getArea

def getPerimeter(h, w):
    perimeter =  2 * (h + w)
    return perimeter

# end getPerimeter

main()


    
