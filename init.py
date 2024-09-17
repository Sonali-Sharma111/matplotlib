import matplotlib.pyplot as plt

# Create a 2x2 grid of subplots
fig, axs = plt.subplots(2, 2)

# First subplot in position [0, 0]
axs[0, 0].plot([1,2,3], [4,5,6])
axs[0, 0].set_title('Plot 1')

# Second subplot in position [0, 1]
axs[0, 1].plot([1, 2, 3], [6, 5, 4])
axs[0, 1].set_title('Plot 2')

# Third subplot in position [1, 0]
axs[1, 0].plot([1, 2, 3], [4, 6, 5])
axs[1, 0].set_title('Plot 3')

# Fourth subplot in position [1, 1]
axs[1, 1].plot([1, 2, 3], [5, 4, 6])
axs[1, 1].set_title('Plot 4')

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()
