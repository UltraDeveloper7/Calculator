import math
from tkinter import*
root=Tk()
root.title("Scientific Calculator")
e=Entry(root, width=50, borderwidth=10)
e.grid(row=0,column=1, columnspan=4, padx=40, pady=20)
######################## Functions for buttons#########################
def button_click(number):
    current=e.get()
    e.delete(0, END)
    e.insert(0, str(current)+str(number))
def button_clear():
    e.delete(0,END)   
def button_add():
    first_number=e.get()
    global f_num
    global math
    math='Addition'
    f_num=float(first_number)
    e.delete(0,END)
def button_equal():
    second_number=e.get()
    e.delete(0,END)
    if math=="Addition":
        e.insert(0, f_num + float(second_number))
    if math=="Subtraction":
        e.insert(0, f_num -  float(second_number))
    if math=="Multiplication":
        e.insert(0, f_num *  float(second_number))
    if math=="Division":
        e.insert(0, f_num /  float(second_number))
def button_subtract():
    first_number=e.get()
    global f_num
    global math
    math='Subtraction'
    f_num=float(first_number)
    e.delete(0,END)
def button_multiply():
    first_number=e.get()
    global f_num
    global math
    math='Multiplication'
    f_num=float(first_number)
    e.delete(0,END)
def button_divide():
    first_number=e.get()
    global f_num
    global math
    math='Division'
    f_num=float(first_number)
    e.delete(0,END)
def button_backspace():
    number=e.get()
    length=len(number)-1
    e.delete(length,END)

##################################Buttons#############################
button_1=Button(root, text="1", padx=41, pady=20, command=lambda:button_click("1"))
button_1.grid(row=4, column=1)
button_2=Button(root, text="2", padx=41, pady=20, command=lambda:button_click("2"))
button_2.grid(row=4, column=2)
button_3=Button(root, text="3", padx=41, pady=20, command=lambda:button_click("3"))
button_3.grid(row=4, column=3)
button_4=Button(root, text="4", padx=41, pady=20, command=lambda:button_click("4"))
button_4.grid(row=3, column=1)
button_5=Button(root, text="5", padx=41, pady=20, command=lambda:button_click("5"))
button_5.grid(row=3, column=2)
button_6=Button(root, text="6", padx=41, pady=20, command=lambda:button_click("6"))
button_6.grid(row=3, column=3)
button_7=Button(root, text="7", padx=41, pady=20, command=lambda:button_click("7"))
button_7.grid(row=2, column=1)
button_8=Button(root, text="8", padx=41, pady=20, command=lambda:button_click("8"))
button_8.grid(row=2, column=2)
button_9=Button(root, text="9", padx=41, pady=20, command=lambda:button_click("9"))
button_9.grid(row=2, column=3)
button_0=Button(root, text="0", padx=41, pady=20, command=lambda:button_click("0"))
button_0.grid(row=5, column=1)
button_add=Button(root, text="+", padx=41, pady=20, command=button_add)
button_add.grid(row=4, column=4)
button_equal=Button(root, text="=", padx=42, pady=20, command=button_equal)
button_equal.grid(row=5, column=4)
button_subtract=Button(root, text="-", padx=41, pady=20, command=button_subtract)
button_subtract.grid(row=3, column=4)
button_multiply=Button(root, text="x", padx=41, pady=20, command=button_multiply)
button_multiply.grid(row=2, column=4)
button_divide=Button(root, text="/", padx=41, pady=20, command=button_divide)
button_divide.grid(row=5, column=2)
button_backspace=Button(root, text="<--", padx=35, pady=20, command=button_backspace)
button_backspace.grid(row=1, column=4)
button_clear=Button(root, text="AC", padx=35, pady=20, command=button_clear)
button_clear.grid(row=1, column=3)
button_dot=Button(root, text=".", padx=41, pady=20, command=lambda:button_click("."))
button_dot.grid(row=5, column=3)
button_par1st=Button(root, text="(", padx=41, pady=20, command=lambda:button_click("("))
button_par1st.grid(row=1, column=1)
button_par2st=Button(root, text=")", padx=41, pady=20, command=lambda:button_click(")"))
button_par2st.grid(row=1, column=2)
root.mainloop()

   



