import customtkinter as ctk
from math import *

class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator")
        self.root.geometry("480x700")
        self.root.resizable(False, False)
        
        self.expression = ""
        self.text_input = ctk.StringVar()

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.create_widgets()

    def create_widgets(self):
        entry = ctk.CTkEntry(self.root, textvariable=self.text_input, font=('Helvetica', 20, 'bold'), border_width=2)
        entry.grid(row=0, column=0, columnspan=5, pady=10, padx=10, sticky='nsew')

        buttons = [
            ('C', 1, 0), ('(', 1, 1), (')', 1, 2), ('pi', 1, 3), ('log', 1, 4),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3), ('tan', 2, 4),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3), ('cos', 3, 4),
            ('7', 4, 0), ('8', 4, 1), ('9', 4, 2), ('/', 4, 3), ('sin', 4, 4),
            ('0', 5, 0), ('.', 5, 1), ('=', 5, 2), ('+', 5, 3), ('sqrt', 5, 4),
            ('exp', 6, 0), ('mod', 6, 1), ('abs', 6, 2), ('ln', 6, 3), ('x^2', 6, 4),
            ('x^3', 7, 0), ('1/x', 7, 1), ('deg', 7, 2), ('rad', 7, 3), ('fact', 7, 4)
        ]

        for (text, row, col) in buttons:
            action = lambda x=text: self.click(x)
            ctk.CTkButton(self.root, text=text, font=('Helvetica', 18, 'bold'), command=action).grid(row=row, column=col, pady=5, padx=5, sticky='nsew')

        for i in range(8):
            self.root.grid_rowconfigure(i, weight=1)
            self.root.grid_columnconfigure(i, weight=1)

    def click(self, item):
        if item == '=':
            try:
                result = str(eval(self.expression))
                self.text_input.set(result)
                self.expression = result
            except:
                self.text_input.set("ERROR")
                self.expression = ""
        elif item == 'C':
            self.expression = ""
            self.text_input.set("")
        elif item == 'sqrt':
            self.expression += "sqrt("
            self.text_input.set(self.expression)
        elif item == 'pi':
            self.expression += "pi"
            self.text_input.set(self.expression)
        elif item == 'log':
            self.expression += "log10("
            self.text_input.set(self.expression)
        elif item == 'ln':
            self.expression += "log("
            self.text_input.set(self.expression)
        elif item == 'exp':
            self.expression += "exp("
            self.text_input.set(self.expression)
        elif item == 'mod':
            self.expression += "%"
            self.text_input.set(self.expression)
        elif item == 'abs':
            self.expression += "abs("
            self.text_input.set(self.expression)
        elif item == 'x^2':
            self.expression += "**2"
            self.text_input.set(self.expression)
        elif item == 'x^3':
            self.expression += "**3"
            self.text_input.set(self.expression)
        elif item == '1/x':
            self.expression += "1/"
            self.text_input.set(self.expression)
        elif item == 'deg':
            self.expression += "degrees("
            self.text_input.set(self.expression)
        elif item == 'rad':
            self.expression += "radians("
            self.text_input.set(self.expression)
        elif item == 'fact':
            self.expression += "factorial("
            self.text_input.set(self.expression)
        else:
            self.expression += str(item)
            self.text_input.set(self.expression)

if __name__ == "__main__":
    root = ctk.CTk()
    calc = ScientificCalculator(root)
    root.mainloop()
