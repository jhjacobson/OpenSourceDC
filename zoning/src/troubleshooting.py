# Helpful scripts for troubleshooting

# Verify that they are the same CRS
print("ANCs CRS: ", ancs.crs)
print("Planning Areas CRS: ", planning_areas.crs)

# Inspect the input data by visualizign both DataFrames

import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(10, 10))
ancs.boundary.plot(ax=ax, color='blue', linewidth=1, label='ANCs')
planning_areas.boundary.plot(ax=ax, color='red', linewidth=1, label='Planning Areas')
plt.legend()
plt.show()
