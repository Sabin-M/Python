import tkinter as tk

class Calculator(tk.Tk):
    def _init_(self):
        super()._init_()

        self.title("Calculator")
        self.geometry("400x600")
        
        self.expression = ""
        self.input_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Entry widget to display expressions and results
        entry = tk.Entry(self, textvariable=self.input_var, font=("Arial", 24), bd=10, insertwidth=2, width=14, borderwidth=4)
        entry.grid(row=0, column=0, columnspan=4)

        # Button definitions
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', 'C', '=', '+'
        ]

        # Creating buttons dynamically
        row_val = 1
        col_val = 0
        for button in buttons:
            action = lambda x=button: self.on_button_click(x)
            tk.Button(self, text=button, padx=20, pady=20, font=("Arial", 18), command=action).grid(row=row_val, column=col_val)

            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def on_button_click(self, char):
        if char == 'C':
            self.expression = ""
        elif char == '=':
            try:
                self.expression = str(eval(self.expression))
            except Exception as e:
                self.expression = "Error"
        else:
            self.expression += str(char)
        
        self.input_var.set(self.expression)

if __name__ == "_main_":
    app = Calculator()
    app.mainloop()