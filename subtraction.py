def solution():
    try:
        # Get user inputs and convert them to floats
        numA = float(input("Enter the first number: "))
        numB = float(input("Enter the second number: "))

        # Perform subtraction and print the result
        result = numA - numB
        print(f"The result of subtracting {numB} from {numA} is {result}.")
    except ValueError:
        print("Please enter valid numbers.")

solution()