import tkinter as tk


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.resizable(False, False)

        self.expression = ""

        self.display = tk.Entry(root, font=("Arial", 20), justify="right", bd=10)
        self.display.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("C", 4, 2), ("+", 4, 3),
            ("=", 5, 0),
        ]

        for text, row, col in buttons:
            colspan = 4 if text == "=" else 1
            btn = tk.Button(
                root,
                text=text,
                font=("Arial", 16),
                width=5,
                height=2,
                command=lambda t=text: self.on_click(t),
            )
            btn.grid(row=row, column=col, columnspan=colspan, sticky="nsew", padx=2, pady=2)

    def on_click(self, value):
        if value == "C":
            self.expression = ""
            self.display.delete(0, tk.END)
        elif value == "=":
            try:
                result = eval(self.expression)
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
                self.expression = str(result)
            except Exception:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
                self.expression = ""
        else:
            self.expression += value
            self.display.delete(0, tk.END)
            self.display.insert(0, self.expression)


if __name__ == "__main__":
    root = tk.Tk()
    Calculator(root)
    root.mainloop()
