def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        den = float(denominator)

        result = num / den
        return f"The result of the division is {result}"

    except ValueError:
        return "ERROR: Please enter numeric values"

    except ZeroDivisionError:
        return "ERROR: Division by zero is not allowed"
