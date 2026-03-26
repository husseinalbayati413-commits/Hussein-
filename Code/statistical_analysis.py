import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Sample data
np.random.seed(0)
data = np.random.randn(1000)

# Statistical analysis
mean = np.mean(data)
median = np.median(data)
std_dev = np.std(data)

# Print statistics
print(f'Mean: {mean}')
print(f'Median: {median}')
print(f'Standard Deviation: {std_dev}')

# Histogram
plt.hist(data, bins=30, alpha=0.5, color='blue')
plt.title('Data Distribution')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.grid()
plt.show()