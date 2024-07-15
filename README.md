# Scientific Calculator

A scientific calculator built using Python and customtkinter, featuring a dark mode for better user experience.

## Features

- Basic arithmetic operations: addition, subtraction, multiplication, division
- Advanced mathematical functions: sine, cosine, tangent, logarithm (base 10 and natural), square root, exponentiation
- Additional functionalities: pi, factorial, modulus, absolute value, reciprocal, degree-radian conversion

## Requirements

- Python 3.x
- customtkinter library

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/taha-daneshmand/scientific_calculator.git
    cd scientific_calculator
    ```

2. Install the required library:
    ```bash
    pip install customtkinter
    ```

## Usage

Run the calculator by executing the following command in the terminal:
```bash
python main.py
```

## Code Explanation

### Main Code Structure

The calculator is implemented in the `main.py` file. Below is a brief overview of the code structure:

```python
import customtkinter as ctk
from math import *

class ScientificCalculator:
    def __init__(self, root):
        # Initialization and setup
        ...
        
    def create_widgets(self):
        # Creating and placing widgets
        ...

    def click(self, item):
        # Handling button clicks
        ...

if __name__ == "__main__":
    root = ctk.CTk()
    calc = ScientificCalculator(root)
    root.mainloop()
```

### Adding Buttons and Functions

The `create_widgets` method adds buttons to the calculator interface:

```python
buttons = [
    ('C', 1, 0), ('(', 1, 1), (')', 1, 2), ('pi', 1, 3), ('log', 1, 4),
    ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3), ('tan', 2, 4),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3), ('cos', 3, 4),
    ('7', 4, 0), ('8', 4, 1), ('9', 4, 2), ('/', 4, 3), ('sin', 4, 4),
    ('0', 5, 0), ('.', 5, 1), ('=', 5, 2), ('+', 5, 3), ('sqrt', 5, 4),
    ('exp', 6, 0), ('mod', 6, 1), ('abs', 6, 2), ('ln', 6, 3), ('x^2', 6, 4),
    ('x^3', 7, 0), ('1/x', 7, 1), ('deg', 7, 2), ('rad', 7, 3), ('fact', 7, 4)
]
```

Each button is associated with an action that is handled by the `click` method:

```python
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
    else:
        self.expression += str(item)
        self.text_input.set(self.expression)
```

## Customization

You can easily customize the appearance and functionality of the calculator by modifying the code. For example, you can change the theme color or add more mathematical functions.

## Contribution

Contributions are welcome! Please open an issue or submit a pull request for any improvements or features you would like to see.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
