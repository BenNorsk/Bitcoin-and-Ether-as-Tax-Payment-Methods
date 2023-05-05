import pandas as pd
import matplotlib.pyplot as plt

# read the master+about+location.pkl
df = pd.read_pickle("master+about+location.pkl")

# Find the total sum of employees on linkedin
total_employees = df["employees_on_linkedin"].sum()
print("Total employees on linkedin:")
print(total_employees)

# Create a pie chart of the industry
df["industry"].value_counts().plot.pie()
plt.savefig("industry.png")

# Print the top 10 industries
print("Top 10 industries:")
print(df["industry"].value_counts()[:10])
