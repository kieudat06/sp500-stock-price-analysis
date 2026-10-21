from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent

RAW_PATH = BASE_DIR / "data" / "raw" / "data_raw.csv"
PROCESSED_PATH = BASE_DIR / "data" / "processed" / "data_processed.csv"


def load_data():
    return pd.read_csv(RAW_PATH)


def filter_data(df):
    df = df.copy()

    df["Date"] = pd.to_datetime(
        df["Date"],
        format="%Y-%m-%d",
        errors="coerce"
    )

    invalid_dates = df["Date"].isna().sum()

    if invalid_dates > 0:
        raise ValueError(
            f"Có {invalid_dates} dòng chứa ngày không hợp lệ. "
            "Vui lòng kiểm tra dữ liệu RAW."
        )

    df = df[df["Date"] >= "2016-01-01"].copy()

    return df


def save_data(df):
    PROCESSED_PATH.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    df.to_csv(PROCESSED_PATH, index=False)


def main():
    df = load_data()

    print("Số dòng dữ liệu RAW:", len(df))

    df = filter_data(df)

    save_data(df)

    print("Số dòng sau khi lọc:", len(df))
    print("Ngày bắt đầu:", df["Date"].min())
    print("Ngày kết thúc:", df["Date"].max())
    print("Đã lưu tại:", PROCESSED_PATH)


if __name__ == "__main__":
    main()