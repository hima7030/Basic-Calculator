from tkinter import *

def addition():
    num1 = int(entry.get())
    num2 = int(entry2.get())
    res= num1+num2
    output.insert(END,res)

def subtraction():
    num1 = int(entry.get())
    num2 = int(entry2.get())
    res = num1 - num2
    output.insert(END, res)

def multiplication():
    num1 = int(entry.get())
    num2 = int(entry2.get())
    res = num1 * num2
    output.insert(END, res)

def division():
    num1 = int(entry.get())
    num2 = int(entry2.get())
    res = num1 / num2
    output.insert(END, res)

def clearFunct():
    entry.delete(0, END)
    entry2.delete(0, END)
    output.delete('1.0', END)
    entry.focus_set()

def main():

    root = Tk()

    root.title('Calculator')

    root.geometry("200x500")
    label = Label(root,text="calculator",
                  width=30,height=5)
    label.pack()
    global entry
    entry = Entry(root)
    entry.pack()
    entry.focus_set()
    blank = Label(root,text="   ")
    blank.pack()
    global entry2
    entry2 = Entry(root)
    entry2.pack()


    add = Button(root, text='+', command=addition, width=5)
    sub = Button(root, text='-', command=subtraction, width=5)
    mul = Button(root, text='*', command=multiplication, width=5)
    div = Button(root, text='/', command=division, width=5)
    clear = Button(root, text='Reset', command=clearFunct, width=5)
    blank = Label(root,text="   ")
    blank.pack()
    add.pack()
    blank = Label(root,text="   ")
    blank.pack()
    sub.pack()
    blank = Label(root,text="   ")
    blank.pack()
    mul.pack()
    blank = Label(root,text="   ")
    blank.pack()
    div.pack()
    blank = Label(root,text="   ")
    blank.pack()

    global output
    output = Text(root, height=2,
                  width =10,
                  bg = "light yellow")
    output.pack()
    blank = Label(root,text="   ")
    blank.pack()
    clear.pack()
    root.mainloop()

if __name__ == '__main__':
    main()