# Data Dictionary

**Dataset:** S&P 500 Historical Stock Data

## English

| **Column** | **Data Type** | **Unit** | **Description** |
|------------|---------------|----------|-----------------|
| Ticker | String | - | Stock ticker symbol of an S&P 500 company. |
| Date | Date | YYYY-MM-DD | Trading date of the stock record. |
| Open | Float | USD | Opening stock price. |
| High | Float | USD | Highest stock price during the trading day. |
| Low | Float | USD | Lowest stock price during the trading day. |
| Close | Float | USD | Closing stock price (Target Variable). |
| Adj Close | Float | USD | Adjusted closing price after dividends and stock splits. |
| Volume | Integer | Shares | Total number of shares traded during the day. |

**Notes**

| Item | Description |
|------|-------------|
| Currency | USD |
| Time Granularity | Daily |
| Target Variable | `Close` |
| Source | Kaggle – S&P 500 Historical Data |
| Dataset URL | https://www.kaggle.com/datasets/jacksaleeby/s-and-p500-historical-data |

---

## Tiếng việt

| **Cột** | **Kiểu dữ liệu** | **Đơn vị** | **Ý nghĩa** |
|---------|------------------|------------|-------------|
| Ticker | String | - | Mã chứng khoán của công ty thuộc chỉ số S&P 500. |
| Date | Date | YYYY-MM-DD | Ngày giao dịch của bản ghi chứng khoán. |
| Open | Float | USD | Giá mở cửa của cổ phiếu vào đầu phiên giao dịch. |
| High | Float | USD | Giá cao nhất mà cổ phiếu đạt được trong phiên giao dịch. |
| Low | Float | USD | Giá thấp nhất của cổ phiếu trong phiên giao dịch. |
| Close | Float | USD | Giá đóng cửa của cổ phiếu vào cuối phiên giao dịch (biến mục tiêu dự báo). |
| Adj Close | Float | USD | Giá đóng cửa đã được điều chỉnh sau khi chia cổ tức và tách cổ phiếu. |
| Volume | Integer | Cổ phiếu | Tổng số lượng cổ phiếu được giao dịch trong phiên. |

**Ghi chú**

| Mục | Ý nghĩa |
|-----|----------|
| Đơn vị tiền tệ | USD |
| Mức thời gian | Theo ngày |
| Biến mục tiêu | `Close` |
| Nguồn dữ liệu | Kaggle – S&P 500 Historical Data |
| Đường dẫn | https://www.kaggle.com/datasets/jacksaleeby/s-and-p500-historical-data |