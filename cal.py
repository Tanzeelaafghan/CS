import tkinter as tk


def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")


def button_click(event):
    current_text = entry.get()
    text = event.widget.cget("text")

    if text == "=":
        calculate()
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)


# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create an entry widget for input and display
entry = tk.Entry(root, font=("Helvetica", 16))
entry.grid(row=0, column=0, columnspan=4)

# Create buttons for digits, operators, and equals
buttons = [
    "7", "8", "9", "+",
    "4", "5", "6", "-",
    "1", "2", "3", "=",
    "0", "C"
]

row_val = 1
col_val = 0

for button_text in buttons:
    button = tk.Button(root, text=button_text, padx=20, pady=20, font=("Helvetica", 16))
    button.grid(row=row_val, column=col_val)
    button.bind("<Button-1>", button_click)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Start the GUI main loop
root.mainloop()
