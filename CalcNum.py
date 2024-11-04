# I lost it gdi


# Simple Calculator in Python

# Function to add 2 numbers
def add(x, y):
    return x + y

# Function to subtract 2 numbers
def subtract(x, y):
    return x - y

# Function to multiply 2 numbers
def multiply(x, y):
    return x * y

# Function to divide 2 numbers
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero. Please try again."
    else:
        return x / y

# Main program, need another fl
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    # Take input from the user
    choice = input("Enter choice (1/2/3/4): ")

    # Check if choice is one of the options
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(f"The result is: {add(num1, num2)}")
            elif choice == '2':
                print(f"The result is: {subtract(num1, num2)}")
            elif choice == '3':
                print(f"The result is: {multiply(num1, num2)}")
            elif choice == '4':
                print(f"The result is: {divide(num1, num2)}")

        except ValueError:
            print("Invalid input. Please enter numbers only.")

    else:
        print("Invalid choice. Please select a valid option.")
    
    # Option to exit the loop
    next_calculation = input("Do you want to perform another calculation? (yes/no): ")
    if next_calculation.lower() != 'yes':
        break
