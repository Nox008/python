import tkinter as tk
from math import sqrt

# --- Main Application Class ---
class CalculatorApp:
    """A GUI calculator application with a Casio-like design."""

    def __init__(self, master):
        self.master = master
        master.title("Calculator")
        master.geometry("340x520")
        master.resizable(False, False)
        master.configure(bg="#e0e0e0")  # Light grey background similar to Casio

        self.expression = ""
        self.equation = tk.StringVar()

        self._create_widgets()

    def _create_widgets(self):
        """Create and place all the widgets in the window."""
        self._create_display()
        self._create_buttons()

    def _create_display(self):
        """Creates the calculator's display screen."""
        display_frame = tk.Frame(self.master, bg="#e0e0e0", bd=10)
        display_frame.pack(expand=True, fill="both")

        # 
        display = tk.Entry(
            display_frame,
            textvariable=self.equation,
            font=('DS-Digital', 48), # A font that mimics LCD displays
            fg="#2b2b2b",             # Dark grey text
            bg="#c4d5c7",             # Greenish LCD background
            bd=0,
            justify="right",
            state="readonly"
        )
        display.pack(expand=True, fill="both", ipady=10)
        self.equation.set("0") # Start with 0 in the display

    def _create_buttons(self):
        """Creates and arranges the calculator buttons."""
        button_frame = tk.Frame(self.master, bg="#e0e0e0")
        button_frame.pack(expand=True, fill="both")

        # Button layout grid
        buttons = [
            ('AC', '√', '%', '/'),
            ('7', '8', '9', '*'),
            ('4', '5', '6', '-'),
            ('1', '2', '3', '+'),
            ('0', '.', '=')
        ]

        # Button styling
        styles = {
            "number": {"bg": "#f5f5f5", "fg": "#2b2b2b", "activebackground": "#dcdcdc"},
            "operator": {"bg": "#d3d3d3", "fg": "#2b2b2b", "activebackground": "#bebebe"},
            "special": {"bg": "#ff9f0a", "fg": "white", "activebackground": "#e69500"},
            "clear": {"bg": "#ff4d4d", "fg": "white", "activebackground": "#e63939"}
        }

        # Create and place buttons
        for r, row_values in enumerate(buttons):
            button_frame.rowconfigure(r, weight=1)
            for c, val in enumerate(row_values):
                button_frame.columnconfigure(c, weight=1)

                if val.isdigit() or val == '.':
                    style = styles["number"]
                elif val in ['/', '*', '-', '+', '%', '√']:
                    style = styles["operator"]
                elif val == '=':
                    style = styles["special"]
                else: # 'AC'
                    style = styles["clear"]

                # The '=' button should span two columns
                if val == '=':
                    colspan = 2
                else:
                    colspan = 1

                # Make the '0' button wider
                if val == '0':
                    self._make_button(button_frame, val, r, c, 1, style, columnspan=2)
                elif val == '.':
                    self._make_button(button_frame, val, r, c + 1, 1, style)
                elif val == '=':
                     self._make_button(button_frame, val, r, c + 1, 1, style)
                else:
                    self._make_button(button_frame, val, r, c, 1, style)

    def _make_button(self, parent, text, row, col, rowspan=1, style=None, columnspan=1):
        """Helper function to create a styled button."""
        btn = tk.Button(
            parent,
            text=text,
            font=('Arial', 18, 'bold'),
            bd=1,
            relief="raised",
            padx=10,
            pady=20,
            command=lambda t=text: self._on_button_press(t),
            **style
        )
        btn.grid(row=row, column=col, rowspan=rowspan, columnspan=columnspan, sticky="nsew", padx=2, pady=2)

    def _on_button_press(self, button_char):
        """Handles the logic for all button presses."""
        if button_char == 'AC':
            self.expression = ""
            self.equation.set("0")
        elif button_char == '=':
            self._evaluate_expression()
        elif button_char == '√':
            self._calculate_sqrt()
        elif button_char == '%':
            self._calculate_percent()
        else:
            # If current display is "0" or "Error", replace it
            if self.equation.get() == "0" or "Error" in self.equation.get():
                self.expression = str(button_char)
            else:
                self.expression += str(button_char)
            self.equation.set(self.expression)

    def _evaluate_expression(self):
        """Calculates the result of the expression."""
        try:
            # Safely evaluate the expression
            # Replace custom operators if any before eval
            expression_to_eval = self.expression.replace('%', '/100')
            result = str(eval(expression_to_eval))
            self.equation.set(result)
            self.expression = result
        except (SyntaxError, ZeroDivisionError, TypeError):
            self.equation.set("Error")
            self.expression = ""

    def _calculate_sqrt(self):
        """Calculates the square root of the current expression."""
        try:
            result = str(sqrt(float(self.expression)))
            self.equation.set(result)
            self.expression = result
        except (ValueError, SyntaxError):
            self.equation.set("Error")
            self.expression = ""

    def _calculate_percent(self):
        """Converts the current number to its percentage value."""
        try:
            result = str(float(self.expression) / 100)
            self.equation.set(result)
            self.expression = result
        except (ValueError, SyntaxError):
            self.equation.set("Error")
            self.expression = ""


# --- Main execution block ---
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()