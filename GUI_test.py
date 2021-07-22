from tkinter import *



root = Tk()
entry = Entry(root, width=50)
entry.pack()
entry.insert(0, "Enter your name: ")


def myClick():
	hello = "Hello " + entry.get()
	myLabel1 = Label(root, text=hello)
	myLabel1.pack()

#Creating the label widget (frame)
myLabel = Label(root, text="Memoires")

# Showing on screen
myLabel.pack()

# Add button to screen, include Text of button.  Commande to call function of MyClick
myButton = Button(root, text="Enter Name", command=myClick, fg="green")
myButton.pack()


root.mainloop()
