import matplotlib.pyplot as plt

# Fibonacci positions
fib_positions = [10, 100, 1000, 10000, 100000, 1000000,
                 10000000, 100000000, 1000000000, 10000000000, 100000000000]

# Execution times in seconds
execution_times = [5.2459E-7, 1.54193E-6, 5.1919E-7, 2.9974E-7, 3.0151999999999996E-7, 3.4372999999999997E-7,
                   4.1556E-7, 2.9786E-7, 2.9568E-7, 2.934E-7, 2.956E-7]

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
