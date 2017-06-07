from Tkinter import *
#To initialize Tkinter, we have to create a Tk root widget, which is a window with a title bar and other decoration provided by the window manager. The root widget has to be created before any other widgets and there can only be one root widget.
root = Tk()

#The next line of code contains the Label widget. The first parameter of the Label call is the name of the parent window, in our case "root". So our Label widget is a child of the root widget. The keyword parameter "text" specifies the text to be shown
#Title widget
w1 = Label(root, text="Labyrinth Solver",
		 fg = "light green",
		 bg = "dark green",
		 font = "Helvetica 16 bold italic", padx = 20).pack()

#Label for image
#logo = PhotoImage(file="/home/sysadmin/Desktop/1.jpg")
#w2 = Label(root,image=logo).pack(side="left")


#The window won't appear until we enter the Tkinter event loop
root.mainloop()