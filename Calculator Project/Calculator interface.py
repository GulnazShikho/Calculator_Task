import Calculator_logic


def get_float_input(prompt):
    while True:
        try:
            number = float(input(prompt))
            return number
        except ValueError:
            print("Please enter a float number.")


def get_operation_choice():
    while True:
        print("\nOperations:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Factorial (!)")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")
        if choice in ['1', '2', '3', '4', '5', '6']:
            return int(choice)
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


def main():
    while True:
        print("\n=== Calculator ===")
        operation = get_operation_choice()

        # Operations that require two operands
        if operation in [1, 2, 3, 4]:
            num1 = get_float_input("Enter the first float number: ")
            num2 = get_float_input("Enter the second float number: ")

            if operation == 1:
                result = Calculator_logic.add(num1, num2)
                print(f"{num1} + {num2} = {result}")
            elif operation == 2:
                result = Calculator_logic.subtract(num1, num2)
                print(f"{num1} - {num2} = {result}")
            elif operation == 3:
                result = Calculator_logic.multiply(num1, num2)
                print(f"{num1} * {num2} = {result}")
            elif operation == 4:
                result = Calculator_logic.divide(num1, num2)
                print(f"{num1} / {num2} = {result}")

        # Factorial operation (requires one operand only)
        elif operation == 5:
            num = get_float_input("Enter a float number to compute its factorial: ")
            if num < 0:
                print("Factorial is not defined for negative numbers.")
            else:
                result = Calculator_logic.factorial(num)
                print(f"{num}! = {result}")

        # Exit option
        elif operation == 6:
            print("Exiting calculator...")
            break

        another_operation = input("\nDo you want to perform another operation? (yes/no): ").strip().lower()
        if another_operation != 'yes':
            print("Exiting calculator...")
            break


if __name__ == "__main__":
    main()