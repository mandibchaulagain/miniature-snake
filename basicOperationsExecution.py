def perform_operation(x, y, operation):
    """Perform the specified operation on two numbers."""
    if operation == 1:
        return x + y
    elif operation == 2:
        return x - y
    elif operation == 3:
        return x * y
    elif operation == 4:
        if y != 0:  # Avoid division by zero
            return x / y
        else:
            print("Error: Division by zero.")
            return None
    else:
        print("Error: Invalid operation.")
        return None


def get_user_input():
    """Get user input for two numbers and the desired operation."""
    try:
        x, y = map(int, input("Enter two numbers separated by a space: ").split())
        operation = int(input("Enter 1 for addition, 2 for subtraction, 3 for multiplication, 4 for division: "))
        return x, y, operation
    except ValueError:
        print("Error: Please enter valid numeric values.")
        return None, None, None


def main():
    while True:
        number = int(input("Enter 1 to enter two numbers or 0 to exit: "))
        if number == 0:
            print("Program terminated.")
            break

        if number == 1:
            x, y, operation = get_user_input()
            if x is not None and y is not None and operation is not None:
                result = perform_operation(x, y, operation)
                if result is not None:
                    print(f"Result: {result}")
        else:
            print("Invalid input. Please enter either 1 or 0.")


if __name__ == "__main__":
    main()
