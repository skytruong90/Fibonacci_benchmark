import matplotlib.pyplot as plt

# Fibonacci positions
fib_positions = [10, 100, 1000, 10000, 100000, 1000000,
                 10000000, 100000000, 1000000000, 10000000000, 100000000000]

# Execution times in seconds
execution_times = [
    5.40048E-6,  # Average time for position 10
    3.9218E-6,  # Average time for position 100
    3.76985E-6,  # Average time for position 1000
    4.28705E-6,  # Average time for position 10000
    4.06399E-6,  # Average time for position 100000
    4.75117E-6,  # Average time for position 1000000
    1.188029E-5,  # Average time for position 10000000
    7.32075E-6,  # Average time for position 100000000
    8.33363E-6,  # Average time for position 1000000000
    9.899259999999999E-6,  # Average time for position 10000000000
    1.100015E-5  # Average time for position 100000000000
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

# Show the plot (optional)
# plt.show()
