import matplotlib.pyplot as plt

# Fibonacci positions
fib_positions = [10, 100, 1000, 10000, 100000, 1000000,
                 10000000, 100000000, 1000000000, 10000000000, 100000000000]

# Execution times in seconds (updated with your results)
execution_times = [
    2.587E-06,  # Average time for position 10
    1.35E-07,   # Average time for position 100
    1.04E-07,   # Average time for position 1000
    1.24E-07,   # Average time for position 10000
    5.7E-08,    # Average time for position 100000
    5.9E-08,    # Average time for position 1000000
    5.6E-08,    # Average time for position 10000000
    5.8E-08,    # Average time for position 100000000
    9.1E-08,    # Average time for position 1000000000
    9.8E-08,    # Average time for position 10000000000
    9.4E-08     # Average time for position 100000000000
]

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
