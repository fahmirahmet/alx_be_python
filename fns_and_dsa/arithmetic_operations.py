def perform_operation (num1,num2,operation):
    match operation:
        case 'add':
            return num1 + num2 
        case 'subtract':
            return num1 - num2
        case 'multiply':
            return num1 * num2
        case 'divide':
            if num2 == 0:
                return f" {num1} can't be divided by 0"
            else:
                return num1 / num2
        case _:
            return "Enter a valid operation." 



             
