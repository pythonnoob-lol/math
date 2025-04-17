def solution():
    try:
        # Get user inputs and convert them to floats
        numA = float(input("First number: "))
        numB = float(input("Second number: "))

        # Perform division and print the result
        result = numA / numB
        print(f"The result of dividing {numA} by {numB} is {result}.")
    except ValueError:
        print("Please enter valid numbers.")
    except ZeroDivisionError:
        print("Division by zero is not allowed.")

solution()