from tkinter import * # Import tkinter
    
class CanvasDemo:
    def __init__(self):
        window = Tk() # Create a window
        window.title("Canvas Demo") # Set title
        
        # Place self.canvas in the window
        self.canvas = Canvas(window, width = 200, height = 100, 
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
        self.canvas.create_rectangle(5, 2, 190, 90, tags = "rect")
        
    
    # Display a line
    def displayLine(self):
        self.canvas.create_line(10, 10, 190, 90, 5, 5, 150, 75, 45, 45, 100, 2, 10, 10, fill = "red", 
            tags = "line")
    
    
    # Display a string
    def displayString(self):
        self.canvas.create_text(60, 40, text = "minimum x is:" +str(2)+ "\n maximum" + str(190), 
           font = "Times 10 bold underline", tags = "string")
    
    # Clear drawings
    def clearCanvas(self):
        self.canvas.delete("rect", "line", "string")

CanvasDemo() # Create GUI 
