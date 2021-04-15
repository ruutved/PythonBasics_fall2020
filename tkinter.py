# A very simple tkinter exercise for a small GUI that adds together three numbers entered

from tkinter import *

# Creating a GUI, giving it the dimensions and a title

gui = Tk()
gui.geometry('300x120')
gui.title("tk")

# Defining the texts to the left side

text0 = Label(gui, text="        ")
text0.grid(column=0, row=2)
text1 = Label(gui, text="1st number")
text1.grid(column=1, row=2)
text2 = Label(gui, text="2nd number")
text2.grid(column=1, row=3)
text3 = Label(gui, text="3rd number")
text3.grid(column=1, row=4)
text4 = Label(gui, text="Total:")
text4.grid(column=1, row=5)

# Defining the fields where the numbers will be entered

number1 = Entry(gui)
number1.grid(column=2, row=2)
number2 = Entry(gui)
number2.grid(column=2, row=3)
number3 = Entry(gui)
number3.grid(column=2, row=4)

# Defining a button to shut down the program

button1 = Button(gui, text="Exit", command=gui.destroy)
button1.grid(column=1, row=7)


# The below function adds up the entered numbers only after they're all entered 
# and "Show result" button has been 

def calculate():
    calc_result = [int(str(number1.get())), int(str(number2.get())), int(str(number3.get()))]
    final_result = sum(calc_result)
    result = Label(gui, text=final_result)
    result.grid(column=2, row=5)


# And now we activate the function to do the math:

button2 = Button(gui, text="Show result", command=calculate)
button2.grid(column=2, row=7)

gui.mainloop()
