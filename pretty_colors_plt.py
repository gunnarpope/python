# found here: https://matplotlib.org/gallery/text_labels_and_annotations/custom_legends.html#sphx-glr-gallery-text-labels-and-annotations-custom-legends-py

# sphinx_gallery_thumbnail_number = 2
from matplotlib import rcParams, cycler
import matplotlib.pyplot as plt
import numpy as np

# Fixing random state for reproducibility
np.random.seed(19680801)

N = 10
data = [np.logspace(0, 1, 100) + np.random.randn(100) + ii for ii in range(N)]
data = np.array(data).T
cmap = plt.cm.coolwarm
rcParams['axes.prop_cycle'] = cycler(color=cmap(np.linspace(0, 1, N)))

fig, ax = plt.subplots()
plt.title("CMAP of coolwarm looks pretty")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
lines = ax.plot(data)
ax.legend(lines)
plt.show()
