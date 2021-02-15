from tkinter import *
window = Tk()
window.title("Tkinter")

def hello():
    value="hello"
    input_text.set(value)
    
input_text= StringVar()

value =""

input_field = Entry(window, textvariable=input_text, fg="black", width=50)
input_field.grid(row=0, column=0)

btn = Button(window, text="Hello", width=10, height=2, command= lambda: hello())
btn.grid(row=1, column=0)
mainloop()