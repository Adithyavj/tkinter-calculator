from tkinter import *

win = Tk()  # This is to create a basic window
win.geometry("312x324")  # this is for the size of the window
win.resizable(0, 0)  # this is to prevent from resizing the window
win.title("Calculator")
## Next we create the GUI of calculator

# 'StringVar()' :It is used to get the instance of input field
input_text = StringVar()

# Let us creating a frame for the input field
input_frame = Frame(win, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black",
                    highlightthickness=2)
input_frame.pack(side=TOP)

# Let us create a input field inside the 'Frame'
input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="#FFFFFF", bd=0,
                    justify=RIGHT)
input_field.grid(row=0, column=0)
input_field.pack()
win.mainloop()
