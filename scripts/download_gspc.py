import yfinance as yf
import pandas as pd
from pathlib import Path

# Download S&P 500 Index
df = yf.download(
    "^GSPC",
    start="2016-01-01",
    end="2026-10-22",
    auto_adjust=False,
    progress=False
)

# Flatten MultiIndex columns
if isinstance(df.columns, pd.MultiIndex):
    df.columns = df.columns.get_level_values(0)

# Reset index
df = df.reset_index()

# Rename columns
df.columns = [
    str(col).lower().replace(" ", "_")
    for col in df.columns
]

# Add ticker
df["ticker"] = "^GSPC"

# Save raw data
output = Path("data/processed/gspc_historical.csv")
output.parent.mkdir(parents=True, exist_ok=True)

df.to_csv(output, index=False)

print("Shape:", df.shape)
print(df.head())
print("Saved:", output)