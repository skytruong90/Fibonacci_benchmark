import matplotlib.pyplot as plt

# Fibonacci positions updated with your data points
fib_positions = [10, 100, 1000, 10000, 100000, 500000]

# Execution times in seconds updated with your results
execution_times = [
    2.7912799999999998E-5,  # Average time for position 10
    3.64925E-5,             # Average time for position 100
    1.1111155E-4,           # Average time for position 1000
    0.00361640185,          # Average time for position 10000
    0.13940766419999998,    # Average time for position 100000
    3.3220509402            # Average time for position 500000
]

plt.plot(fib_positions, execution_times, marker='o')  # Line plot with points

# Labeling the axes and the plot
plt.xlabel('Sequence Position (n)')
plt.ylabel('Average Execution Time (seconds)')
plt.title('Average Execution Time for Loop Fibonacci Computation')

# Setting the scale of the axes to log due to the wide range of values
plt.xscale('log')
plt.yscale('log')

plt.grid(True)
# Save the figure to a file instead of showing it
plt.savefig('LoopGraph.png')
