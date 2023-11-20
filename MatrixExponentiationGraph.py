import matplotlib.pyplot as plt

# Fibonacci positions
fib_positions = [10, 100, 1000, 10000, 100000, 1000000]

# Execution times in seconds
execution_times = [
    4.23965E-6,  # Average time for position 10
    3.0482300000000003E-6,  # Average time for position 100
    3.3332E-6,  # Average time for position 1000
    3.6856600000000003E-6,  # Average time for position 10000
    3.7343499999999997E-6,  # Average time for position 100000
    4.61764E-6  # Average time for position 1000000
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
