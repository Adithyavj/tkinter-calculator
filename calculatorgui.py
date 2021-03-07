from tkinter import *

win = Tk()  # This is to create a basic window
win.geometry("312x324")  # this is for the size of the window
win.resizable(0, 0)  # this is to prevent from resizing the window
win.title("Calculator")
## Next we create the GUI of calculator

# 'StringVar()' :It is used to get the instance of input field
input_text = StringVar()

"""  USER INPUT FRAME  """
# Creating a frame for the input field
input_frame = Frame(win, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black",
                    highlightthickness=2)
input_frame.pack(side=TOP)

# creating an input field inside the 'Frame' for reading the user input
input_field = Entry(input_frame, font=('arial', 20, 'bold'), textvariable=input_text, width=50, bg="#FFFFFF", bd=0,
                    justify=RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)  # 'ipady' is internal padding to increase the height of input field

"""  BUTTONS FRAME  """
# Let us creating another 'Frame' for the button below the 'input_frame'
btns_frame = Frame(win, width=312, height=272.5, bg="grey")
btns_frame.pack()

win.mainloop()
