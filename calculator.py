from tkinter import *

def buttonOnClick(number):
    global operator
    operator= operator + str(number)
    text_input.set(operator)

def clearButtonOnClick():
      global operator
      operator=""
      text_input.set("")
def equalButtonOnClick():
    global operator
    sumup=str(eval(operator))
    text_input.set(sumup)
    operator=""
    
calc= Tk()
calc.title("MY CALCULATOR")
calc.resizable(False,False)
operator=""
text_input=StringVar()

txtDisplay=Entry(calc,font=('New Times Roman',20,'bold'),textvariable=text_input,bd=30,insertwidth=4,
                 bg="powder blue",justify='right').grid(columnspan=4)
#first row 7,8,9 and +
bt7=Button(calc,padx=16,pady=16,bd=8,fg="black",font=('New Times Roman',20,'bold'),
           text="7",bg="purple", command=lambda:buttonOnClick(7)).grid(row=1,column=0)
bt8=Button(calc,padx=16,pady=16,bd=8,fg="black",font=('New Times Roman',20,'bold'),
           text="8",bg="purple",command=lambda:buttonOnClick(8)).grid(row=1,column=1)
bt9=Button(calc,padx=16,pady=16,bd=8,fg="black",font=('New Times Roman',20,'bold'),
           text="9",bg="purple",command=lambda:buttonOnClick(8)).grid(row=1,column=2)
add=Button(calc,padx=16,pady=16,bd=8,fg="black",font=('New Times Roman',20,'bold'),
           text="+",bg="powder blue",command=lambda:buttonOnClick("+")).grid(row=1,column=3)
#second row 4,5,6 and -
bt4=Button(calc,padx=16,pady=16,bd=8,fg="black",font=('New Times Roman',20,'bold'),
           text="4",bg="purple",command=lambda:buttonOnClick(4)).grid(row=2,column=0)
bt5=Button(calc,padx=16,pady=16,bd=8,fg="black",font=('New Times Roman',20,'bold'),
           text="5",bg="purple",command=lambda:buttonOnClick(5)).grid(row=2,column=1)
bt6=Button(calc,padx=16,pady=16,bd=8,fg="black",font=('New Times Roman',20,'bold'),
           text="6",bg="purple",command=lambda:buttonOnClick(6)).grid(row=2,column=2)
subsract=Button(calc,padx=16,pady=16,bd=8,fg="black",font=('New Times Roman',20,'bold'),
           text="-",bg="powder blue",command=lambda:buttonOnClick("-")).grid(row=2,column=3)
#third row 1,2,3 and -
bt1=Button(calc,padx=16,pady=16,bd=8,fg="black",font=('New Times Roman',20,'bold'),
           text="1",bg="purple",command=lambda:buttonOnClick(1)).grid(row=3,column=0)
bt2=Button(calc,padx=16,pady=16,bd=8,fg="black",font=('New Times Roman',20,'bold'),
           text="2",bg="purple",command=lambda:buttonOnClick(2)).grid(row=3,column=1)
bt3=Button(calc,padx=16,pady=16,bd=8,fg="black",font=('New Times Roman',20,'bold'),
           text="3",bg="purple",command=lambda:buttonOnClick(3)).grid(row=3,column=2)
multipy=Button(calc,padx=16,pady=16,bd=8,fg="black",font=('New Times Roman',20,'bold'),
           text="*",bg="powder blue",command=lambda:buttonOnClick("*")).grid(row=3,column=3)
#forth 0,clear button,equal button and /
bt0=Button(calc,padx=16,pady=16,bd=8,fg="black",font=('New Times Roman',20,'bold'),
           text="0",bg="purple",command=lambda:buttonOnClick(0)).grid(row=4,column=0)
btclear=Button(calc,padx=16,pady=16,bd=8,fg="black",font=('New Times Roman',20,'bold'),
           text="C",bg="powder blue",command=clearButtonOnClick).grid(row=4,column=1)
btequal=Button(calc,padx=16,pady=16,bd=8,fg="black",font=('New Times Roman',20,'bold'),
           text="=",bg="powder blue",command=equalButtonOnClick).grid(row=4,column=2)
devide=Button(calc,padx=16,pady=16,bd=8,fg="black",font=('New Times Roman',20,'bold'),
           text="/",bg="powder blue",command=lambda:buttonOnClick("/")).grid(row=4,column=3)

calc.mainloop()
