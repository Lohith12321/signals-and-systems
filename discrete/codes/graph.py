import matplotlib.pyplot as plt

# Calculate the sum of squares of terms of natural numbers from 5 to 20
n_values = range(5, 21)
sum_of_squares = sum([(n*(n+1)*(2*n+1)/6)-30 for n in n_values])

# Create a stem plot
plt.stem(n_values, [ (n*(n+1)*(2*n+1)/6)-30  for n in n_values], use_line_collection=True)
plt.xlabel('n')
plt.ylabel('y(n)')
plt.title('Sum of Squares of Terms of Natural Numbers from 5 to 20')
plt.show()
plt.savefig('graph.png')
