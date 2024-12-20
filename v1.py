import matplotlib.pyplot as plt

# Initialize empty lists for x and y values
x_values = []
y_values = []

# Open and read the file v4.txt
with open('v4.txt', 'r') as file:
    for _ in range(40):  # Read 40 lines as there are 40 sets of values
        try:
            # Split each line into a, b, c, x
            line = file.readline().strip().split()
            a = float(line[0])
            b = float(line[1])
            c = float(line[2])
            x = float(line[3])
            
            # Calculate the y value
            y = a * x**2 + b * x + c
            
            # Append x and y values to their respective lists
            x_values.append(x)
            y_values.append(y)

        except (IndexError, ValueError):
            print("Error reading a line. Check your data format.")
            break

# Plot the graph
plt.plot(x_values, y_values, marker='o', linestyle='-', color='b')
plt.title('Graph of y = ax^2 + bx + c')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()
