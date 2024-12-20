# 3rd Version
# Read values from v3.txt
try:
    with open('v3.txt', 'r') as file:
        # Read a, b, c, and x values from the file
        values = file.read().strip().split()
        a, b, c, x = map(float, values)

        # Compute the quadratic expression
        y = a * x**2 + b * x + c
        print(f'The value of y is {y}')
except FileNotFoundError:
    print('Error: v3.txt file not found.')
except ValueError:
    print('Error: Invalid data in v3.txt. Ensure it contains four numeric values (a, b, c, x).')
