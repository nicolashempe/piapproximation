from tkinter import *
import random
import math
# import sys and os to reset app
import sys
import os

# initialize screen object
top = Tk()
top.title("Monte Carlo Approximation of PI")

# set up canvas to add content
c = Canvas(top, bg="black", height="300", width="300")
c.pack(side="left")

# add user input entry to enter the calulate range
# amount of random points

inputAmt = Entry(top)
inputAmt.place(x=305)
inputAmt.insert(0, 'Enter Sample Range')
inputAmt.pack()
inputAmt.focus_set()

# circle outline
c.create_oval(0,0,300,300, fill="", outline="white")

# create inner and outer lists to hold the points created
inner = []
outer = []

# main function
def main():

    # make sure user input is an int
    try:
        int(inputAmt.get())
    except ValueError:
        print("Type value invalid")
        reset()

    # function calculates the random points
    def calculate():
        for i in range(int(inputAmt.get())):
            x = random.randint(0,300)
            y = random.randint(0,300)
            s = point(x, y)
            if s.r <= 150:
                inner.append(s)
            else:
                outer.append(s)

    # class object for point
    class point:
        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.r = math.sqrt(math.pow((self.x - 150), 2) + math.pow((self.y - 150), 2))

    # run claculate function to create points
    calculate()

    # initialize variables
    innersum = 0
    outersum = 0
    result = 0
    outerf = 0
    innerf = 0

    # draw points on canvas
    for p in inner:
        c.create_oval(p.x,p.y,(p.x + 3), (p.y + 3), fill="#00b21a", outline="")

    for p in outer:
        c.create_oval(p.x,p.y,(p.x + 3), (p.y + 3), fill="red", outline="")

    for i in range(len(inner)):
        innersum += i

    innerf = innersum/len(inner)

    for i in range(len(outer)):
        outersum += i

    outerf = outersum/len(outer)

    result = float("{0:.4f}".format(4*(innerf / (outerf+innerf))))


    # labels
    innerLabel = Label(top, text="Inner: " + str(len(inner)))
    innerLabel.place(x=305,y=30)

    outerLabel = Label(top, text="Outer: " + str(len(outer)))
    outerLabel.place(x=305,y=60)

    totalLabel = Label(top, text="Total: " + str(len(inner) + len(outer)))
    totalLabel.place(x=305,y=90)

    aproxLabel = Label(top, text="Approximation: " + str(result)) 
    aproxLabel.place(x=305,y=130)

# window size
top.geometry("500x300")

# frame for button pack in_
bottom = Frame(top)
bottom.pack(side=BOTTOM, fill=BOTH, expand=True)


# enter a run button to initiate loop
b = Button(top, text="Run", command=main)
b.pack(in_=bottom, side="left")

''' closes the program and then loads it again'''
def reset():
    python = sys.executable
    os.execl(python, python, * sys.argv)

br = Button(top, text="Reset", command=reset)
br.pack(in_=bottom, side="left")

# execute
top.mainloop()
