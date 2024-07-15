import tkinter as tk import math

class Calculator(tk.Tk): def init(self): super().init()
    self.title("Calculator")
    self.geometry("300x300")  # Widened for extra buttons

    self.result_var = tk.StringVar()

    self.create_widgets()

def create_widgets(self):
    # Entry to display the result
    entry = tk.Entry(self, textvariable=self.result_var, font=("Arial", 24), bd=10)
    entry.grid(row=0, column=0, columnspan=4)

    # Buttons for numbers, operators, and functions
    buttons = [
        ("7", 1, 0),
        ("8", 1, 1),
        ("9", 1, 2),
        ("/", 1, 3),
        ("4", 2, 0),
        ("5", 2, 1),
        ("6", 2, 2),
        ("*", 2, 3),
        ("1", 3, 0),
        ("2", 3, 1),
        ("3", 3, 2),
        ("-", 3, 3),
        ("0", 4, 0),
        (".", 4, 1),
        ("+", 4, 2),
        ("=", 4, 3),
        ("C", 5, 0),  # Clear button
        ("√", 5, 1),   # Square root button
        ("USD-INR", 5, 2),  # USD to INR conversion
        # Add more buttons as needed
    ]

    for (text, row, col) in buttons:
        button = tk.Button(self, text=text, font=("Arial", 18), width=5, height=2, command=lambda t=text: self.on_button_click(t))
        button.grid(row=row, column=col)

def on_button_click(self, text):
    if text == "=":
        try:
            expression = self.result_var.get()
            result = str(eval(expression))  # Evaluate the expression
            self.result_var.set(result)
        except:
            self.result_var.set("Error")
    elif text == "C":
        self.result_var.set("")  # Clear the entry
    elif text == "√":
        try:
            num = float(self.result_var.get())
            if num >= 0:
                result = math.sqrt(num)
                self.result_var.set(result)
            else:
                self.result_var.set("Invalid Input")
        except:
            self.result_var.set("Error")
    elif text == "USD-INR":
        try:
            usd = float(self.result_var.get())
            # You'll need to fetch the current exchange rate dynamically
            # For now, let's assume a rate:
            inr_rate = 80.0  # Replace with actual rate
            inr = usd * inr_rate
            self.result_var.set(inr)
        except:
            self.result_var.set("Error")        
    else:
        current_text = self.result_var.get()
        new_text = current_text + text
        self.result_var.set(new_text)
