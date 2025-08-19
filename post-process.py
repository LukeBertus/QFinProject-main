# Add index column
import pandas as pd
from scipy.stats import pearsonr

df = pd.read_csv("trade_prices.csv")

## Add index column ##
#df.insert(0, "Index", range(1, len(df) + 1))

## Add average column ##
#price_columns = [col for col in df.columns if col != "Index"]
#df["Average"] = df[price_columns].mean(axis=1)

## Delete Columns ##
#df = df.drop(columns=["Price_2", "Price_3", "Price_8"], errors="ignore")

## Convert to change in price ##
#price_columns = [col for col in df.columns if col != "Index"]
#for col in price_columns:
#    df[col] = df[col].diff()

## Remove Outliers ##
#price_columns = [col for col in df.columns if col != "Index"]
#for col in price_columns:
#    mask = (df[col] > 10) | (df[col] < -10)
#    df[col] = df[col].where(~mask, df[col].shift())

results = {}

for col in [c for c in df.columns if c.startswith('Price_')]:
    # Calculate past and future 5-step changes
    past_change = df[col] - df[col].shift(5)
    future_change = df[col].shift(-5) - df[col]
    
    # Drop rows with NaN values (due to shifting)
    valid = (~past_change.isna()) & (~future_change.isna())
    past_change = past_change[valid]
    future_change = future_change[valid]
    
    # Compute correlation and p-value
    corr, pval = pearsonr(past_change, future_change)
    results[col] = {'correlation': corr, 'p_value': pval}

# Display results
for col, res in results.items():
    print(f"{col}: correlation={res['correlation']:.4f}, p-value={res['p_value']:.4g}")

#df.to_csv("trade_prices.csv", index=False)
