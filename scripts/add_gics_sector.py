import pandas as pd
import yfinance as yf
from pathlib import Path
from tqdm import tqdm

input_path = Path("data/raw/data_raw.csv")
output_path = Path("data/processed/data_clean.csv")

sector_map = {
    "Energy": "EN",
    "Basic Materials": "MAT",
    "Industrials": "IND",
    "Consumer Defensive": "CS",
    "Consumer Cyclical": "CD",
    "Healthcare": "HC",
    "Financial Services": "FIN",
    "Technology": "IT",
    "Communication Services": "COM",
    "Utilities": "UT",
    "Real Estate": "RE"
}

df = pd.read_csv(input_path)

sector_data = {}

for ticker in tqdm(df["Ticker"].dropna().unique()):
    try:
        sector = yf.Ticker(str(ticker)).info.get("sector")
        sector_data[ticker] = sector_map.get(sector)
    except Exception:
        sector_data[ticker] = None

df["GICS_Sector"] = df["Ticker"].map(sector_data)

missing_sector_map = {
    "BK": "FIN",
    "BRK.B": "FIN",
    "CTRA": "EN",
    "DAY": "IND",
    "HOLX": "HC",
    "SEE": "MAT"
}

df["GICS_Sector"] = df["GICS_Sector"].fillna(
    df["Ticker"].map(missing_sector_map)
)

output_path.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(output_path, index=False)

print(df["GICS_Sector"].value_counts(dropna=False))
print("Đã lưu:", output_path)