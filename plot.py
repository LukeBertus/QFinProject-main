import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV, making sure the index column is parsed correctly
df = pd.read_csv("trade_prices.csv", index_col=0)

# colors = ["black" if col == "Average" else "grey" for col in df.columns]

# Plot all columns vs index
df.plot(figsize=(12, 6), color=colors)
plt.title("Stock Price Simulation")
plt.xlabel("Index")
plt.ylabel("Price")
plt.grid(True)
plt.show()
