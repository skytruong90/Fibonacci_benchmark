import matplotlib.pyplot as plt

# Fibonacci positions
fib_positions = [10, 100, 1000, 10000, 100000, 1000000]

# Execution times in seconds
execution_times = [1.81268E-6, 1.0370900000000001E-6,
                   4.5129E-7, 3.7069E-7, 3.01E-7, 2.6316E-7]

plt.plot(fib_positions, execution_times, marker='o')  # Line plot with points

# Labeling the axes and the plot
plt.xlabel('Fibonacci Sequence Position (n)')
plt.ylabel('Average Execution Time (seconds)')
plt.title('Average Execution Time for Closed-Form Fibonacci Computation')

# Setting the scale of the axes to log due to wide range of values
plt.xscale('log')
plt.yscale('log')

plt.grid(True)
# Save the figure to a file instead of showing it
plt.savefig('ClosedFormGraph.png')
