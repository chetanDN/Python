from tkinter import *

RootWindow = Tk()

def click():
	enteredText = textEntryBox.get() #to get entered data
	output.delete(0.0, END)
	output.insert(END,enteredText)
	
	
RootWindow.geometry("500x500") #setting size of app to 500x500
# RootWindow.resizable(0,0) #dont allow resizing of window in x or y direction

RootWindow.title("Display Content")

#create label
# Label(RootWindow, text="enter here:", bg="black", fg="white", font="none 12 bold").grid(row=1,column=0, sticky=W)
textLabel = Label(RootWindow, text="enter here:").grid(row=1,column=0, sticky=W)
# Label(RootWindow, text="enter here:")
# Label().grid(row=1,column=0, sticky=W)

#Create textbox
textEntryBox = Entry(RootWindow, width=20)
textEntryBox.grid(row=2, column=0, sticky=W)


#Create submit button
submitButton = Button(RootWindow, text="Submit", width='10', command=click).grid(row=3, column=0, sticky = W)


#label to display 
outLabel = Label(RootWindow, text='Description:').grid(row=4,column=0,sticky=W)

#textbox for showing output
output = Text(RootWindow, width=75, height=6, wrap=WORD, background="white")
output.grid(row=5, column=0,columnspan=2, sticky=W)


RootWindow = mainloop()

