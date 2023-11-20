import matplotlib.pyplot as plt

# Fibonacci positions
fib_positions = [10, 100, 500, 1000]

# Execution times in seconds
execution_times = [7.85718E-5, 8.7983E-5, 1.381102E-4, 1.637494E-4]

# Create a figure and axis with more customization options
fig, ax = plt.subplots()

# Plot the data with a solid line and markers
ax.plot(fib_positions, execution_times, marker='o',
        linestyle='-', color='b', label='Execution Time')

# Set axis labels and title with larger font size
ax.set_xlabel('Fibonacci Sequence Position (n)', fontsize=14)
ax.set_ylabel('Average Execution Time (seconds)', fontsize=14)
ax.set_title('Average Execution Time for Memoized Fibonacci', fontsize=16)

# Use a logarithmic scale for both axes
ax.set_xscale('log')
ax.set_yscale('log')

# Add a grid for better readability
ax.grid(True, which='both', linestyle='--', lw=0.5)

# Add a legend
ax.legend()

# Customize the appearance of tick labels
ax.tick_params(axis='both', which='major', labelsize=12)
ax.tick_params(axis='both', which='minor', labelsize=10)

# Save the figure with higher resolution and better layout
fig.tight_layout()
fig.savefig('MemoizedGraph.png', dpi=300)

# Show the plot (optional)
plt.show()
