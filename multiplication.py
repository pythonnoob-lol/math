def solution():
    try:
        # Get user inputs and convert them to floats
        numA = float(input("First number: "))
        numB = float(input("Second number: "))

        # Perform multiplication and print the result
        result = numA * numB
        print(f"The result of multiplying {numA} by {numB} is {result}.")
    except ValueError:
        print("Please enter valid numbers.")

solution()