import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# Load Switzerland shapefile
switzerland = gpd.read_file("swissBOUNDARIES3D_1_4_TLM_KANTONSGEBIET.shp")

# Load data
data = pd.read_pickle("master+about+location+co_entry.pkl")

# Create plot
fig, ax = plt.subplots(figsize=(10, 10))
switzerland.plot(ax=ax, alpha=0.4, edgecolor='black')
ax.scatter(data["lng"], data["lat"], color='red', s=5)

# Save plot
fig.savefig("switzerland_map.png", dpi=300)
