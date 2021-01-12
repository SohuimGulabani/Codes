from tkinter import *

window=Tk()

window.geometry("312x324")
window.resizable(0,0)
window.title("Calculator")

def btn_click(item):
	global expression
	expression=expression+str(item)
	input_text.set(expression)

def btn_clear():
	global expression
	expression=""
	input_text.set("")

input_frame=Frame(window, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=1)

input_frame.pack(side=TOP)

input_field=Entry(input_frame, font=("georgia",18, "bold"),textvariable=input_text, width=50, bg="#eee", bd=0, justify=Right)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)

btns_frame=Frame(window, width=312, height=272.5, bg="grey")
btns_frame.pack()


window.]                   nnjnnmainloop()
