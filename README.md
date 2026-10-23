# sp500-stock-price-analysis

# S&P 500 Stock Price Analysis

Dự án phân tích dữ liệu giá cổ phiếu thuộc chỉ số S&P 500 trong giai đoạn 2016–2026 bằng Python.

## 1. Cài đặt dự án

Clone repository:

```bash
git clone https://github.com/kieudat06/sp500-stock-price-analysis.git
cd sp500-stock-price-analysis
```

Cài đặt các thư viện cần thiết:

```bash
pip install -r requirements.txt
```

## 2. Chuẩn bị dữ liệu gốc

Tải bộ dữ liệu S&P 500 Historical Data tại: https://www.kaggle.com/datasets/jacksaleeby/s-and-p500-historical-data

Giải nén và đổi tên file CSV thành:

```text
data_raw.csv
```

Đặt file vào thư mục:

```text
data/raw/data_raw.csv
```

Cấu trúc thư mục:

```text
sp500-stock-price-analysis/
│
├── data/
│   ├── raw/
│   │   └── data_raw.csv
│   │
│   └── processed/
│
├── scripts/
│   ├── data_pipeline.py
│   ├── download_gspc.py
│   └── add_gics_sector.py
│
├── requirements.txt
└── README.md
```

## 3. Quy trình xử lý dữ liệu

Chạy lần lượt các script sau từ thư mục gốc của dự án.

### Bước 1: Lọc dữ liệu từ năm 2016

```bash
python scripts/data_pipeline.py
```

Script thực hiện:

* Đọc dữ liệu từ `data/raw/data_raw.csv`.
* Chuyển đổi cột `Date` sang định dạng ngày tháng.
* Kiểm tra ngày không hợp lệ.
* Lọc dữ liệu từ ngày 01/01/2016 trở đi.

**Kết quả:**

```text
data/processed/data_processed.csv
```

### Bước 2: Tải dữ liệu chỉ số S&P 500

```bash
python scripts/download_gspc.py
```

Script sử dụng thư viện `yfinance` để tải dữ liệu lịch sử của chỉ số S&P 500 (`^GSPC`) từ Yahoo Finance.

**Kết quả:**

```text
data/raw/gspc_historical.csv
```

Bước này yêu cầu kết nối Internet.

### Bước 3: Bổ sung thông tin ngành GICS

```bash
python scripts/add_gics_sector.py
```

Script thực hiện:

* Đọc dữ liệu cổ phiếu.
* Truy vấn thông tin ngành của từng mã cổ phiếu từ Yahoo Finance.
* Ánh xạ ngành sang mã phân loại được sử dụng trong dự án.
* Bổ sung cột `GICS_Sector`.

**Kết quả:**

```text
data/processed/data_clean.csv
```

Bước này yêu cầu kết nối Internet. Một số mã cổ phiếu có thể không lấy được thông tin ngành.

## 4. Kết quả sau khi chạy

Cấu trúc dữ liệu:

```text
data/
├── raw/
│   ├── data_raw.csv
│   └── gspc_historical.csv
│
└── processed/
    ├── data_processed.csv
    └── data_clean.csv
```

| File                  | Nội dung                            |
| --------------------- | ----------------------------------- |
| `data_raw.csv`        | Dữ liệu cổ phiếu gốc                |
| `data_processed.csv`  | Dữ liệu cổ phiếu từ năm 2016        |
| `gspc_historical.csv` | Dữ liệu lịch sử chỉ số S&P 500      |
| `data_clean.csv`      | Dữ liệu cổ phiếu được bổ sung ngành |

## 5. Chạy toàn bộ quy trình

Sau khi chuẩn bị dữ liệu gốc và cài đặt thư viện, có thể chạy lần lượt:

```bash
python scripts/data_pipeline.py
python scripts/download_gspc.py
python scripts/add_gics_sector.py
```

Các file kết quả sẽ được lưu tự động vào thư mục `data/`.

**Lưu ý:** Chạy các lệnh từ thư mục gốc của repository và đảm bảo có kết nối Internet khi tải dữ liệu từ Yahoo Finance.
