import matplotlib.pyplot as plt

# Load data from the file
data = []
with open("generaltermdata.txt", "r") as file:
    for line in file:
        n, a = map(int, line.split())
        data.append((n, a))

# Extract x and y values from data
x_values = [point[0] for point in data]
y_values = [point[1] for point in data]

# Plotting the points
plt.scatter(x_values, y_values, color='blue')
plt.title('Sequence')
plt.xlabel('Index (n)')
plt.ylabel('Term (a)')
plt.grid(True)
plt.show()
