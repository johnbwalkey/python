import numpy as np
import matplotlib.pyplot as plt

# Generate some sample data
np.random.seed(0)
event_times = np.random.normal(loc=0, scale=1, size=1000)  # Sample event times

# Define the bin edges for the histogram
bin_edges = np.arange(-5, 6, 0.5)  # Bins from -5 to 5 in steps of 0.5

# Create the histogram
hist, bins = np.histogram(event_times, bins=bin_edges)

# Calculate bin centers
bin_centers = (bins[:-1] + bins[1:]) / 2

# Plot the histogram
plt.bar(bin_centers, hist, width=0.4)
plt.xlabel('Time (s) relative to trigger')
plt.ylabel('Event count')
plt.title('Posterior Event Time Histogram (PETH)')
plt.grid(True)
plt.show()

