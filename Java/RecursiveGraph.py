import matplotlib.pyplot as plt

# Fibonacci positions updated with your data points
fib_positions = [10, 20, 30, 40]

# Execution times in seconds updated with your results
execution_times = [
    1.6067349999999998E-5,  # Average time for position 10
    6.40872E-5,             # Average time for position 20
    0.0047045639,           # Average time for position 30
    0.5206960987            # Average time for position 40
]

plt.plot(fib_positions, execution_times, marker='o')  # Line plot with points

# Labeling the axes and the plot
plt.xlabel('Fibonacci Sequence Position (n)')
plt.ylabel('Average Execution Time (seconds)')
plt.title('Average Execution Time for Recursive Fibonacci Computation')

# Setting the scale of the axes to log due to the wide range of values
plt.xscale('log')
plt.yscale('log')

plt.grid(True)
# Save the figure to a file instead of showing it
plt.savefig('RecursiveGraph.png')
