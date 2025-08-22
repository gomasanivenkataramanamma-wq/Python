class Calculator:
    def calculate(self, a: float, b: float, operation: str) -> float:
        operation = operation.lower()
        if operation in ["add", "+"]:
            return a + b
        elif operation in ["sub", "-"]:
            return a - b
        elif operation in ["mul", "*"]:
            return a * b
        elif operation in ["div", "/"]:
            if b == 0:
                raise ZeroDivisionError("Division by zero is not allowed")
            return a / b
        else:
            raise ValueError(f"Unknown operation: {operation}")


# Example usage
calc = Calculator()
print(calc.calculate(10, 5, "add"))  # 15
print(calc.calculate(10, 5, "sub"))  # 5
print(calc.calculate(10, 5, "mul"))  # 50
