## TASK 1 SIMPLE CALCULATOR

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y

def main():
    print("Basic Calculator")
    while True:
        print("\n1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice in ["1", "2", "3", "4"]:
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))

                if choice == "1":
                    print("Result:", add(num1, num2))
                elif choice == "2":
                    print("Result:", subtract(num1, num2))
                elif choice == "3":
                    print("Result:", multiply(num1, num2))
                elif choice == "4":
                    try:
                        print("Result:", divide(num1, num2))
                    except ValueError as e:
                        print("Error:", e)
            except ValueError:
                print("Invalid input. Please enter valid numbers.")

        elif choice == "5":
            break

        else:
            print("Invalid choice. Please select a valid option.")
if __name__ == "__main__":
    main()

