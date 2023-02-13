import numpy as np
import matplotlib.pyplot as plt

# Define the k-points along the x-axis
kpoints = np.linspace(-np.pi, np.pi, 100)

# Calculate the eigenenergies at each k-point
eigenenergies = np.cos(kpoints)

# Plot the band structure
plt.plot(kpoints, eigenenergies)
plt.xlabel('k-point')
plt.ylabel('Eigenenergy')
plt.title('Band Structure')
plt.savefig("/data/home/liuhanyu/hyliu/code/pwkit/test/demo.jpg")