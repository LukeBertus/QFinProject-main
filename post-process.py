# Add index column
import pandas as pd

df = pd.read_csv("trade_prices.csv")

# Add index column
# df.insert(0, "Index", range(1, len(df) + 1))

# Add average column
price_columns = [col for col in df.columns if col != "Index"]
df["Average"] = df[price_columns].mean(axis=1)


df.to_csv("trade_prices.csv", index=False)