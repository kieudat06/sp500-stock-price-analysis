# DATA DICTIONARY – S&P 500 HISTORICAL STOCK DATA

## 1. Thông tin tổng quan

| Thuộc tính | Mô tả |
|---|---|
| Tên bộ dữ liệu | S&P 500 OHCLV Stock Data |
| Nguồn dữ liệu | Kaggle – jacksaleeby |
| Đường dẫn | https://www.kaggle.com/datasets/jacksaleeby/s-and-p500-historical-data |
| Lĩnh vực | Tài chính – Thị trường chứng khoán |
| Tần suất | Theo ngày giao dịch |
| Định dạng | CSV |
| Phạm vi sử dụng | Từ ngày 01/01/2016 trở đi |
| Số lượng biến | 8 |
| Dữ liệu gốc | `data/raw/data_raw.csv` |
| Dữ liệu sau xử lý | `data/processed/data_processed.csv` |

Bộ dữ liệu chứa thông tin giá cổ phiếu và khối lượng giao dịch của các mã cổ phiếu thuộc phạm vi dữ liệu S&P 500.

Mỗi dòng dữ liệu tương ứng với một mã cổ phiếu tại một ngày giao dịch.

## 2. Từ điển dữ liệu

| Tên biến | Kiểu dữ liệu | Đơn vị | Ý nghĩa | Nguồn gốc |
|---|---|---|---|---|
| Ticker | string | Không có | Mã định danh cổ phiếu của doanh nghiệp | Kaggle |
| Date | datetime | YYYY-MM-DD | Ngày diễn ra phiên giao dịch | Kaggle |
| Open | float64 | USD/cổ phiếu | Giá cổ phiếu tại thời điểm mở cửa | Kaggle |
| High | float64 | USD/cổ phiếu | Giá cao nhất trong phiên giao dịch | Kaggle |
| Low | float64 | USD/cổ phiếu | Giá thấp nhất trong phiên giao dịch | Kaggle |
| Close | float64 | USD/cổ phiếu | Giá cổ phiếu tại thời điểm đóng cửa | Kaggle |
| Adj Close | float64 | USD/cổ phiếu | Giá đóng cửa đã điều chỉnh theo các sự kiện doanh nghiệp, tùy phương pháp điều chỉnh của nguồn dữ liệu | Kaggle |
| Volume | int64 | Cổ phiếu | Tổng số cổ phiếu được giao dịch trong phiên | Kaggle |

**Ghi chú:**
- `Ticker` và `Date` kết hợp để xác định một quan sát theo mã cổ phiếu và ngày giao dịch.
- `Open`, `High`, `Low`, `Close` là các biến mô tả biến động giá trong phiên.
- `Adj Close` thường được sử dụng khi phân tích biến động giá trong dài hạn.
- `Volume` phản ánh khối lượng giao dịch, không phải giá trị giao dịch bằng USD.
- Kiểu dữ liệu trong bảng là kiểu dữ liệu dự kiến; cần kiểm tra bằng Pandas để xác nhận kiểu dữ liệu thực tế.

## 3. Nguồn gốc và quy trình xử lý

### 3.1. Nguồn dữ liệu

Dữ liệu được tải từ Kaggle:

https://www.kaggle.com/datasets/jacksaleeby/s-and-p500-historical-data

Dữ liệu gốc được lưu tại:

`data/raw/data_raw.csv`

### 3.2. Quy trình xử lý

Chương trình xử lý được xây dựng bằng Python và Pandas, lưu tại:

`src/data_pipeline.py`

Các bước thực hiện:

1. Đọc dữ liệu từ file CSV gốc.
2. Chuyển đổi cột `Date` sang kiểu ngày tháng.
3. Lọc các bản ghi có ngày giao dịch từ 01/01/2016 trở đi.
4. Giữ nguyên 8 cột dữ liệu ban đầu.
5. Xuất dữ liệu sau lọc sang `data/processed/data_processed.csv`.

Dữ liệu gốc được giữ nguyên để phục vụ kiểm tra và tái lập quá trình xử lý.

## 4. Kiểm tra chất lượng dữ liệu

Các nội dung cần kiểm tra bao gồm:

| Nội dung | Mục đích |
|---|---|
| Missing Values | Phát hiện giá trị bị thiếu trong các cột |
| Duplicates | Phát hiện các dòng dữ liệu trùng lặp |
| Ticker-Date Duplicates | Kiểm tra các bản ghi trùng mã cổ phiếu và ngày giao dịch |
| Data Types | Kiểm tra kiểu dữ liệu của từng biến |
| Invalid Dates | Phát hiện ngày giao dịch không hợp lệ |
| Invalid Prices | Kiểm tra giá cổ phiếu bằng 0 hoặc âm |
| Invalid Volume | Kiểm tra khối lượng giao dịch âm |
| Price Consistency | Kiểm tra tính hợp lý giữa giá cao nhất, thấp nhất, mở cửa và đóng cửa |

Các nội dung trên là tiêu chí kiểm tra, chưa phải kết quả đánh giá chất lượng thực tế.

Việc phân tích dữ liệu khám phá (EDA), xử lý giá trị thiếu, dữ liệu trùng lặp và các giá trị bất thường sẽ được thực hiện chi tiết trong BT3.

## 5. Hạn chế của bộ dữ liệu

- Dữ liệu phản ánh biến động giá trong quá khứ, không đảm bảo khả năng dự báo chính xác trong tương lai.
- Danh sách doanh nghiệp thuộc S&P 500 có thể thay đổi theo thời gian.
- Dữ liệu hiện tại chưa có thông tin phân loại ngành GICS.
- Dữ liệu chưa tích hợp các sự kiện kinh tế và yếu tố vĩ mô.
- Các ngày không có giao dịch có thể không xuất hiện trong dữ liệu.


## 6. Tài liệu tham khảo

Saleeby, J. (n.d.). *S&P 500 OHCLV Stock Data (2.7M+ rows)* [Data set]. Kaggle.

https://www.kaggle.com/datasets/jacksaleeby/s-and-p500-historical-data