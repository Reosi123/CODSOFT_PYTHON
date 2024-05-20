from tkinter import *
from tkinter import messagebox

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        messagebox.showerror("Error", "Cannot divide by zero!")
        return None
    return a / b

def perform_operation():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    choice = operation_var.get()

    if choice == "Add":
        result = add(num1, num2)
    elif choice == "Subtract":
        result = subtract(num1, num2)
    elif choice == "Multiply":
        result = multiply(num1, num2)
    elif choice == "Divide":
        result = divide(num1, num2)
    else:
        result = "Invalid Operation"

    if result is not None:
        label_result.config(text="Result: " + str(result))


root = Tk()
root.title("Simple Calculator")


label_num1 = Label(root, text="Enter the first number:")
label_num1.pack(pady=5)
entry_num1 = Entry(root)
entry_num1.pack(pady=5)

label_num2 = Label(root, text="Enter the second number:")
label_num2.pack(pady=5)
entry_num2 = Entry(root)
entry_num2.pack(pady=5)

operation_var = StringVar()
operation_var.set("Add")  

label_operation = Label(root, text="Select Operation:")
label_operation.pack(pady=5)

option_add = Radiobutton(root, text="Add", variable=operation_var, value="Add")
option_add.pack(anchor=W)

option_subtract = Radiobutton(root, text="Subtract", variable=operation_var, value="Subtract")
option_subtract.pack(anchor=W)

option_multiply = Radiobutton(root, text="Multiply", variable=operation_var, value="Multiply")
option_multiply.pack(anchor=W)

option_divide = Radiobutton(root, text="Divide", variable=operation_var, value="Divide")
option_divide.pack(anchor=W)

button_calculate = Button(root, text="Calculate", command=perform_operation)
button_calculate.pack(pady=10)

label_result = Label(root, text="Result:")
label_result.pack(pady=5)

root.mainloop()