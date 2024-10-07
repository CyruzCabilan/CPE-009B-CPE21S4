from tkinter import *
class MyWindow:
    def __init__(self, win):
        #common widget
        self.Label1 = Label(win, fg = "red", text = "Calculator")
        self.Label1.place(x =150, y = 50)
        self.Label2 = Label(win, fg = "black", text = "Number 1:")
        self.Label2.place(x = 50, y = 80)
        self.Entry1 = Entry(win,bd = 2)
        self.Entry1.place(x = 120, y = 80)
        self.Label3 = Label(win, text = "Number 2:")
        self.Label3.place(x = 50, y = 120)
        self.Entry2 = Entry(win, bd = 2)
        self.Entry2.place(x = 120, y = 120)
        self.Label4 = Label(win, text = "Result:")
        self.Label4.place(x = 50, y = 160)
        self.Entry3 = Entry(win, bd = 2)
        self.Entry3.place(x = 120, y = 160)

        self.Button1 = Button(win, fg = "blue", text = "Add")
        self.Button1.place(x = 210, y =200)
        self.Button1.bind('<Button-1>', self.add)

        self.Button2 = Button(win, fg="blue", text="sub")
        self.Button2.place(x=160, y=200)
        self.Button2.bind('<Button-1>', self.sub)

        self.Button2 = Button(win, fg="blue", text="mult")
        self.Button2.place(x=120, y=200)
        self.Button2.bind('<Button-1>', self.mult)

        self.Button2 = Button(win, fg="blue", text="div")
        self.Button2.place(x=100, y=200)
        self.Button2.bind('<Button-1>', self.div)

    def add(self,win):
        self.Entry3.delete(0, 'end')
        num1 = int(self.Entry1.get())
        num2 = int(self.Entry2.get())
        result = num1 + num2
        self.Entry3.insert(END, str(result))


    def sub(self,win):
        self.Entry3.delete(0, 'end')
        num1 = int(self.Entry1.get())
        num2 = int(self.Entry2.get())
        result = num1 - num2
        self.Entry3.insert(END, str(result))

    def mult(self, win):
        self.Entry3.delete(0, 'end')
        num1 = int(self.Entry1.get())
        num2 = int(self.Entry2.get())
        result = num1 * num2
        self.Entry3.insert(END, str(result))

    def div(self, win):
        self.Entry3.delete(0, 'end')
        num1 = int(self.Entry1.get())
        num2 = int(self.Entry2.get())
        result = num1 / num2
        self.Entry3.insert(END, str(result))



window=Tk()
MyWin = MyWindow(window)
window.geometry("400x300+10+10")
window.configure(bg = 'green')
window.title("Standard Calculator")
window.mainloop()
window.mainloop