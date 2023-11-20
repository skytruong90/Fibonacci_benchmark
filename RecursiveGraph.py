import matplotlib.pyplot as plt

# Fibonacci positions
fib_positions = [10, 100, 1000, 10000, 100000, 1000000]

# Execution times in seconds
execution_times = [9.66582E-5, 7.125E-5, 2.42673E-4, 0.0042481908, 0.1822250638, 15.2225430454]

plt.plot(fib_positions, execution_times, marker='o')  # Line plot with points

# Labeling the axes and the plot
plt.xlabel('Fibonacci Sequence Position (n)')
plt.ylabel('Average Execution Time (seconds)')
plt.title('Average Execution Time for Fibonacci Computation')

# Setting the scale of the axes to log due to wide range of values
plt.xscale('log')
plt.yscale('log')

plt.grid(True)
# Save the figure to a file instead of showing it
plt.savefig('RecursiveGraph.png')

