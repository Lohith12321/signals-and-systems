import matplotlib.pyplot as plt

def calculate_a(n_values, d):
    return [((n + 1) / 2) * (4 + 7 * n) for n in n_values]

def plot_function(n_values, a_values):
    plt.plot(n_values, a_values, marker='o', linestyle='-')
    plt.xlabel('n')
    plt.ylabel('a')
    plt.title('Plot of a=((n+1)/2)*(4+7*n)')
    plt.grid(True)
    plt.show()
    plt.sav

# Define the range of n values (only integral values)
n_values = range(1, 40, 1)  

# Define the common difference (d)
d = 1  # Example: d = 1

# Calculate the corresponding 'a' values
a_values = calculate_a(n_values, d)

# Plot the function
plot_function(n_values, a_values)
