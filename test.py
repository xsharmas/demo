print("heloo world")
#get the two numbers from the user once at the beginning of the program and then pass those two numbers as arguments to the 'sum', 'multiply', and 'divide' functions This way it will only ask for the inputs once and then perform all the calculations with those values
def sum(a, b):
    return a + b   
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b
def main():
    # Get user input once
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    
    # Perform calculations
    print(f"Sum: {sum(a, b)}")
    print(f"Multiply: {multiply(a, b)}")
    print(f"Divide: {divide(a, b)}")
if __name__ == "__main__":
    main()
    