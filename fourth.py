#write a code to print the first 100 numbers of the Fibonacci series
def fibonacci(n):
    """Generate the first n numbers of the Fibonacci series."""
    fib_series = []
    a, b = 0, 1
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series
def main():
    n = 100  # Number of Fibonacci numbers to generate
    fib_series = fibonacci(n)
    print(f"The first {n} numbers of the Fibonacci series: {fib_series}")
if __name__ == "__main__":
    main()
    print("Fibonacci series generated successfully.")
# This code generates the first 100 numbers of the Fibonacci series
# using a simple iterative approach and prints them.