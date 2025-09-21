# Simple Calculator - Basic Version
print("Simple Calculator")
print("Operations: +, -, *, /")

while True:
    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))
        
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                print("Error: Division by zero!")
                continue
        else:
            print("Invalid operator!")
            continue
            
        print(f"Result: {num1} {operator} {num2} = {result}")
        
        again = input("Do another calculation? (y/n): ")
        if again.lower() != 'y':
            break
            
    except ValueError:
        print("Please enter valid numbers!")
