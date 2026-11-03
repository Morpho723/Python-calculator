from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

KV = """
<CalculatorRoot>:
    orientation: "vertical"
    padding: "18dp"
    spacing: "10dp"
    Label:
        text: "CALCULATOR"
        size_hint_y: None
        height: "42dp"
        font_size: "20sp"
    Label:
        text: root.expression
        size_hint_y: None
        height: "42dp"
        font_size: "22sp"
        halign: "right"
        text_size: self.size
    Label:
        text: root.display
        size_hint_y: 1
        font_size: "42sp"
        halign: "right"
        text_size: self.size
    GridLayout:
        cols: 4
        spacing: "8dp"
        size_hint_y: 2.6
        Button:
            text: "AC"
            on_release: root.press("AC")
        Button:
            text: "⌫"
            on_release: root.press("⌫")
        Button:
            text: "%"
            on_release: root.press("%")
        Button:
            text: "÷"
            on_release: root.press("÷")
        Button:
            text: "7"
            on_release: root.press("7")
        Button:
            text: "8"
            on_release: root.press("8")
        Button:
            text: "9"
            on_release: root.press("9")
        Button:
            text: "×"
            on_release: root.press("×")
        Button:
            text: "4"
            on_release: root.press("4")
        Button:
            text: "5"
            on_release: root.press("5")
        Button:
            text: "6"
            on_release: root.press("6")
        Button:
            text: "−"
            on_release: root.press("−")
        Button:
            text: "1"
            on_release: root.press("1")
        Button:
            text: "2"
            on_release: root.press("2")
        Button:
            text: "3"
            on_release: root.press("3")
        Button:
            text: "+"
            on_release: root.press("+")
        Button:
            text: "±"
            on_release: root.press("±")
        Button:
            text: "0"
            on_release: root.press("0")
        Button:
            text: "."
            on_release: root.press(".")
        Button:
            text: "="
            on_release: root.press("=")
"""

class CalculatorRoot(BoxLayout):
    display = StringProperty("0")
    expression = StringProperty("")
    just_calculated = False

    def press(self, key):
        if key == "AC":
            self.display, self.expression = "0", ""
            self.just_calculated = False
        elif key == "⌫":
            self.display = self.display[:-1] or "0"
        elif key == "±":
            if self.display != "0":
                self.display = self.display[1:] if self.display.startswith("-") else "-" + self.display
        elif key == "=":
            self.calculate()
        elif key == "%":
            try:
                self.display = self.fmt(float(self.display) / 100)
            except ValueError:
                self.display = "Error"
        elif key in ("+", "−", "×", "÷"):
            self.expression = self.display + " " + key
            self.display = "0"
            self.just_calculated = False
        elif key == ".":
            if self.just_calculated:
                self.display, self.just_calculated = "0", False
            if "." not in self.display:
                self.display += "."
        elif key.isdigit():
            if self.just_calculated or self.display in ("0", "Error"):
                self.display, self.just_calculated = key, False
            else:
                self.display += key

    def calculate(self):
        if not self.expression:
            return
        try:
            left_s, op = self.expression.rsplit(" ", 1)
            a, b = float(left_s), float(self.display)
            if op == "+":
                result = a + b
            elif op == "−":
                result = a - b
            elif op == "×":
                result = a * b
            elif op == "÷":
                if b == 0:
                    self.display, self.expression = "Cannot divide by zero", ""
                    return
                result = a / b
            else:
                return
            self.expression += " " + self.display + " ="
            self.display = self.fmt(result)
            self.just_calculated = True
        except (ValueError, OverflowError):
            self.display, self.expression = "Error", ""

    @staticmethod
    def fmt(value):
        if value.is_integer():
            return str(int(value))
        return f"{value:.8f}".rstrip("0").rstrip(".")

class CalculatorApp(App):
    def build(self):
        self.title = "Calculator"
        return Builder.load_string(KV)

if __name__ == "__main__":
    CalculatorApp().run()
