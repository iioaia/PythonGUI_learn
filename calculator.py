from tkinter import *

root = Tk()
root.title("Calculator")

# uinput is the User input, numbers. Often referred to as 'entry'

uinput = Entry(root, width=35, borderwidth=5)
uinput.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


# Button List and Functions

def button_click(number):
	#uinput.delete(0, END)
	current = uinput.get()
	uinput.delete(0, END)
	uinput.insert(0, str(current) + str(number))

def button_clear():
	uinput.delete(0, END)

def button_add():
	first_num = uinput.get()
	global f_num
	global math
	math = "addition"
	f_num = int(first_num)
	uinput.delete(0, END)



def button_subtract():
	first_num = uinput.get()
	global f_num
	global math
	math = "subtract"
	f_num = int(first_num)
	uinput.delete(0, END)



def button_multiply():
	first_num = uinput.get()
	global f_num
	global math
	math = "multiply"
	f_num = int(first_num)
	uinput.delete(0, END)


def button_divide():
	first_num = uinput.get()
	global f_num
	global math
	math = "divide"
	f_num = int(first_num)
	uinput.delete(0, END)


def button_equal():
	second_num = uinput.get()
	uinput.delete(0, END)

	
	if math == "subtract":
		uinput.insert(0, f_num - int(second_num))


	if math == "addition":
		uinput.insert(0, f_num + int(second_num))


	if math == "multiply":
		uinput.insert(0, f_num * int(second_num))
	
	if math == "divide":
		uinput.insert(0, f_num / int(second_num))



# Button List
button_0 = Button(root, text="0", padx=20, pady=20, command=lambda: button_click(0))
button_1 = Button(root, text="1", padx=20, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=20, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=20, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=20, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=20, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=20, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=20, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=20, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=20, pady=20, command=lambda: button_click(9))

button_add = Button(root, text="+", padx=18, pady=20, command=button_add)
button_subtract = Button(root, text="-", padx=18, pady=20, command=button_subtract)

button_multiply = Button(root, text="x", padx=18, pady=20, command=button_multiply)
button_divide = Button(root, text="/", padx=18, pady=20, command=button_divide)

button_equal = Button(root, text="=", padx=40, pady=20, command=button_equal)
button_clear = Button(root, text="Clear", padx=35, pady=20, command=button_clear)



# Show buttons on screen in grid format

button_0.grid(row=4, column=0)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_add.grid(row=4, column=1)
button_subtract.grid(row=4, column=2)

button_divide.grid(row=5, column=0)
button_multiply.grid(row=5, column=1)

button_equal.grid(row=5, column=2)
button_clear.grid(row=5, column=3)


root.mainloop()
