import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV, making sure the index column is parsed correctly
df = pd.read_csv("trade_prices.csv", index_col=0)

# colors = ["black" if col == "Average" else "grey" for col in df.columns]

# Plot all columns vs index
plt.figure(figsize=(12, 6))
for col in df.columns:
    plt.scatter(df.index, df[col], label=col)

plt.title("Market without Interference")
plt.xlabel("Index")
plt.ylabel("Price")
plt.grid(True)
plt.legend()
plt.show()