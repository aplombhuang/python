items = input("try this").strip().split()

i = 0

if (len(items))%2 == 1:
        
        input("need to enter even amount of numbers")
        exit(0)
else:
        j = int((len(items))/2)

num1 = [0 for i in range(j)]

num2 = [0 for i in range(j)]

for i in range(j):
        num1[i] = eval(items[2 * i])
        num2[i] = eval(items[2*i +1])



length = sorted(num1)

width = sorted(num2)

maxLength = length[j-1]

maxWidth = width[j-1]

midLength = ((maxLength - length[0])/2)

midWidth = ((maxWidth - width[0])/2)

string1 = str(length[0])

string2 = str(width[0])

from tkinter import * # Import tkinter
    
class CanvasDemo:
    def __init__(self):
        window = Tk() # Create a window
        window.title("Canvas Demo") # Set title
        
        # Place self.canvas in the window
        self.canvas = Canvas(window, width = 400, height = 400, 
            bg = "white")
        self.canvas.pack()
        
        # Place buttons in frame
        frame = Frame(window)
        frame.pack()
        btRectangle = Button(frame, text = "Rectangle", 
            command = self.displayRect)

       
        btLine = Button(frame, text = "Line", 
            command = self.displayLine)
        btString = Button(frame, text = "String", 
            command = self.displayString)
        btClear = Button(frame, text = "Clear", 
            command = self.clearCanvas)
        btRectangle.grid(row = 1, column = 1)

        btLine.grid(row = 1, column = 2)
        btString.grid(row = 1, column = 3)
        btClear.grid(row = 1, column = 4)
        
        window.mainloop() # Create an event loop


    # Display a rectangle
    def displayRect(self):
        self.canvas.create_rectangle(length[0]+1, width[0]+1, maxLength+1, maxWidth+1, tags = "rect")
        
    
    # Display a line
    def displayLine(self):
        for i in range (j-1):
                self.canvas.create_line(num1[i]+1, num2[i]+1, num1[i+1]+1, num2[i+1]+1, fill = "red", tags = "line")
        self.canvas.create_line(num1[j-1]+1, num2[j-1]+1, num1[0]+1, num2[0]+1, fill = "red", tags = "line")
    
    
    # Display a string
    def displayString(self):
        self.canvas.create_text(maxLength+60, maxWidth+60, text = "minimum length x: " + str(length[0])
                                + "\n minimum width y is: " + str(width[0])
                                + "\n maximum x is: " + str(maxLength)
                                + "\n maximum y is: " + str(maxWidth)
                                + "\n center point is: (" + str(midLength) + " , " + str(midWidth)+ ")" , 
           font = "Times 14 bold underline", tags = "string")
    
    # Clear drawings
    def clearCanvas(self):
        self.canvas.delete("rect", "line", "string")

CanvasDemo() # Create GUI 


