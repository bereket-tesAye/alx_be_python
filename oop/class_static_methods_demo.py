class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    # Static method: works independently of class or instance
    @staticmethod
    def add(a, b):
        return a + b

    # Class method: has access to class attributes via cls
    @classmethod
    def multiply(cls, a, b):
        print(f"Calculation type: {cls.calculation_type}")
        return a * b