def safe_divide(numerator, denominator):
    try:
        # convert to float first
        num = float(numerator)
        den = float(denominator)
        
        result = num / den
        return f"{num} / {den} = {result}"
    
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Non-numeric input provided."
