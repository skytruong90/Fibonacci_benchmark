import matplotlib.pyplot as plt

# Fibonacci positions
fib_positions = [10, 100, 1000, 10000, 100000, 1000000,
                 10000000, 100000000, 1000000000, 10000000000, 100000000000]

# Execution times in seconds (updated with your results)
execution_times = [
    8.014E-06,  # Average time for position 10
    2.595E-06,  # Average time for position 100
    4.064E-06,  # Average time for position 1000
    3.387E-06,  # Average time for position 10000
    4.225E-06,  # Average time for position 100000
    4.411E-06,  # Average time for position 1000000
    4.888E-06,  # Average time for position 10000000
    6.465E-06,  # Average time for position 100000000
    6.798E-06,  # Average time for position 1000000000
    1.0843E-05,  # Average time for position 10000000000
    1.5649E-05  # Average time for position 100000000000
]

plt.plot(fib_positions, execution_times, marker='o')  # Line plot with points

# Labeling the axes and the plot
plt.xlabel('Fibonacci Sequence Position (n)')
plt.ylabel('Average Execution Time (seconds)')
plt.title('Average Execution Time for Matrix Exponentiation')

# Setting the scale of the axes to log due to the wide range of values
plt.xscale('log')
plt.yscale('log')

plt.grid(True)
# Save the figure to a file instead of showing it
plt.savefig('MatrixExponentiationGraph.png')


