"""
Graphical User Interfaces with Tk -Python Documentation
https://docs.python.org/3/library/tk.html

Modern Tkinter:
https://tkdocs.com/tutorial/index.html

• older official documentation
    https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/index.html

tKinter Repository:
https://github.com/roseman/tkdocs

"""

'''
AP Considerations:
    •   Project needs to be ACHIEVABLE:
        •   Build this only within the constraints of what Create PT is
            asking for.
                • Data must be stored in a list
                • You must use a function with one or more parameters 
                  and include sequencing, selection, and iteration.
                    • Sequencing - Application of each step of an algorithm in order.
                    • Selection - Branching Statements: If/Else, Try/Catch
                    • Iteration - Loops.
            
    •   I cannot give you feedback on your project or help you solve problems.
         • Can help solve very similar problems.
	• You and your classmates may work together on a project, but you 
	must have your own separate contributions that act as parts of a whole.

Other things:
    •   Comments comments comments. You will not remember what each of these
        things do, and as we continue to improve on our projects, the progression
        of how we got from A to B to C in our project will disappear.

'''

import tkinter as tk
from PIL import Image, ImageTk

# Initializes our window with specifications
root = tk.Tk()
bgString = "#023047"
canvas = tk.Canvas(root, height = 500, width = 325, bg=bgString)
canvas.grid(rowspan=3, columnspan=3)

gradesList = []

# Loads an image into python and makes it compatible for tkinter use.
logo = Image.open("CalcLogo23.png")
#logo.show() #to display image.

logo = ImageTk.PhotoImage(logo) #Making it campatible for Tk (?)

logoLabel = tk.Label(root, image=logo, bg = bgString)
logoLabel.grid(row=0, column=1)



'''
First thing we need to do is hide the entry box until the start button is pressed.
Once the button is pressed, we want to add another button alongside it.
Then we're going to want to reassign the function of the buttons so that one adds values to a list
and the other averages those values.

We want to construct this in a light where its suitable for the Create PT project.
It is very possible to construct this in a way where its completely unsuitable for Create PT.
    • Functions without Parameters
    • Not using a list, etc.
'''

# Initializes all of the remaining primary objects for the project.
# - Avg_btn - calculates the average of values in the list.
# - Entry - a text box for getting grades as input
def start():
    global entry, avg_Btn
    welcome_txt.config(text="", font=("Raleway", 20))
    start_btn.config(width=10, command=lambda:getNums())
    start_btn.grid(row=1, sticky="W")

    avg_Btn = tk.Button(beFrame, text="Calc\n Avg", command=lambda: calcAverage(gradesList), height=2, width=9,
                        font=("Raleway", 12),
                        bg="#000000", fg="white", activebackground="#505050", activeforeground="grey")
    avg_Btn.grid(row=1,sticky="E")

    entry = tk.Entry(beFrame, font=("Raleway", 12))
    entry.bind("<Return>", _getNums)
    entry.grid(row=0, sticky="WE")

# Allows us to only enter integers into the text box.
# Handles any raised value error as a result.
def getNums():
    global entry
    try:
        gradesList.append(int(entry.get()))
        myString = makeGradeString(gradesList)
        welcome_txt.config(text=myString)

    except ValueError:
        welcome_txt.config(text="Enter a valid Number")

    entry.delete(0, len(entry.get()))

# Builds ands formats a string out of all current values in the grade list.
# Commas and spaces are added to each value except the last one entered.
# A new string is generated and displayed when a grade has been entered.
def makeGradeString(myList):
    myString = "Grades:\n"
    for i in range(len(gradesList)):
        if (i == len(gradesList) - 1):
            myString += str(gradesList[i]) + " "
        else:
            myString += str(gradesList[i]) + ", "
            if ((i + 1) % 4 == 0 and i != 0):
                myString += "\n"
    return myString

# The logic for calculating our average and displaying it on screen.
def calcAverage(myList):
    avgString = "Average:\n"
    sum=0
    for val in myList: sum += val
    grade = round((sum/len(myList)), 2)
    avgString+= str(grade)
    end(avgString)

# Displays the average on the final screen and reconfigures the button to
# restart the program over again.
def end(myString):
    welcome_txt.config(text=myString)
    entry.destroy()
    avg_Btn.destroy()
    gradesList.clear()

    start_txt.set("Restart!")
    start_btn.config(width=15, command=lambda:start())



# Event Handler for getNums, allows us to bind the Enter key to GetNums
def _getNums(event):
    getNums()


# Creation of the frame to subdivide sections of our window.
beFrame = tk.Frame(root)
beFrame.grid(row=2, column = 1)

start_txt = tk.StringVar()
start_btn = tk.Button(beFrame, textvariable=start_txt,
                      command=lambda:start(), height = 2, width =15,
                      font = ("Raleway",12), bg="#ff8400", fg="white",
                      activebackground="#ba4e00")
start_txt.set("Start")
start_btn.grid(row=1)



welcome_txt = tk.Label(root, text="Welcome!", font=("Raleway", 25), bg=bgString, fg = "#FFDE9B")
welcome_txt.grid(column=1, row=1) # Used to manage the placement of objects.

# Keeps our objects centered
root.rowconfigure([0,1,2], weight=1)
root.columnconfigure([0,1,2], weight=1)

root.mainloop()