import tkinter
from tkinter import BOTH, StringVar, END, ANCHOR

#Define window
root = tkinter.Tk()
root.title("Checklist Application with Tkinter by George Tabet")
#When saving for icons of the app; they have to be in ICO file format
root.iconbitmap("PythonIcon.ico")
root.geometry("700x700")
root.resizable(0,0)

#Define some fonts & colors
myFont = ("Times New Roman", 20)
rootColor = "#7a7a78"       #This is the background color; will change later.
buttonColor = '#e2cff4'
root.config(bg=rootColor)

#Define Functions
def addItem():
    myListBox.insert(END,listEntry.get())

    listEntry.delete(0,END)

def removeItem():
    myListBox.delete(ANCHOR)

def clearList():
    myListBox.delete(0,END)

def saveList():
    with open('checklist.txt', 'w') as f:
        listTuple = myListBox.get(0,END)
        for item in listTuple:
            if item.endswith('\n'):
                f.write(item)
            else:
                f.write(item + '\n')   #This will creat a checklist.txt with the elements you typed.

def openList():
    try:
        with open('checklist.txt', 'r') as f:
            for line in f:
                myListBox.insert(END,line)  #Saves the items in order.
    except:
        return

#Define Layout & Create Frames
inputFrames = tkinter.Frame(root, bg=rootColor)
outputFrames = tkinter.Frame(root, bg=rootColor)
buttonFrames = tkinter.Frame(root, bg=rootColor)
inputFrames.pack()
outputFrames.pack()
buttonFrames.pack()

#Input Frame Layout
listEntry = tkinter.Entry(inputFrames)
listAddButton = tkinter.Button(inputFrames, text="Add Item",font=myFont,command=addItem)
listEntry.grid(row=1,column=2, padx=5, pady=5)
listAddButton.grid(row=1, column=3, padx=5, pady=5, ipadx=5)

#Output Frame Layout
myScrollBar = tkinter.Scrollbar(outputFrames)
myListBox = tkinter.Listbox(outputFrames, height=25, width=45, borderwidth=3, font=myFont,yscrollcommand=myScrollBar.set)
myListBox.grid(row=0, column=0)
myScrollBar.grid(row=0,column=1,sticky="NS")
myScrollBar.config(command=myListBox.yview)

#Button Frame Layout
listRemoveButton = tkinter.Button(buttonFrames, text="Remove Item", borderwidth=2, font=myFont, bg=buttonColor, command=removeItem)
listClearButton = tkinter.Button(buttonFrames, text="Clear List", borderwidth=2, font=myFont, bg=buttonColor, command=clearList)
saveButton = tkinter.Button(buttonFrames, text="Save List", borderwidth=2, font=myFont, bg=buttonColor, command=saveList)
quitButton = tkinter.Button(buttonFrames, text="Quit", borderwidth=2, font=myFont, bg=buttonColor, command=root.destroy)
listRemoveButton.grid(row=0,column=0,padx=10, pady=10)
listClearButton.grid(row=0, column=1,padx=10, pady=10)
saveButton.grid(row=0, column=2,padx=10, pady=10)
quitButton.grid(row=0, column=3,padx=10, pady=10)

#Open the previous list if available
openList()  #This will save the items.

#Run root window's main log; this is basically a loop that will run until you close the window.
root.mainloop()