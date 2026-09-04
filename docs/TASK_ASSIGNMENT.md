# PHÂN CÔNG CÔNG VIỆC – FINAL PROJECT

**Đề tài:** SP500 Stock Price Analysis & Forecasting

## Nguyễn Hoàng Đức Anh – 1. Project Charter & README

**Chỉnh các file**

* `docs/Project_Charter.md`
* `README.md`
* `notebooks/BT1_ProjectCharter.ipynb`

**Công việc**

1. Xác định Business Question.
2. Xác định Target Variable (`Close`).
3. Viết Project Charter (mục tiêu, phạm vi, rủi ro, nguồn dữ liệu).
4. Viết README giới thiệu dự án.
5. Tạo notebook BT1 và trình bày nội dung Charter

**Hoàn thiện:** BT1 hoàn chỉnh + Project_Charter

---

## Nguyễn Thành An 2. – Data Collection & Data Dictionary

**Chỉnh các file**

* `notebooks/BT2_DataCollection.ipynb`
* `docs/Data_Dictionary.md`

**Công việc**

1. Đọc dữ liệu bằng Pandas.
2. Kiểm tra số dòng, số cột, kiểu dữ liệu.
3. Chuyển cột `Date` sang `datetime`.
4. Kiểm tra Missing Values.
5. Kiểm tra Duplicate.
6. Lập Data Dictionary cho toàn bộ 8 biến.
7. Lưu dữ liệu sạch vào `data/processed/`.

**Hoàn thiện:** BT2 + Data Dictionary.

---

## Nguyễn Hương Duyên 3. - EDA & Visualization

**Chỉnh file**

* `notebooks/BT3_EDA.ipynb`

**Công việc**

1. Xử lý Missing Values (nếu có) và giải thích phương pháp.
2. Phát hiện & xử lý Outliers (IQR hoặc Z-score).

**Thực hiện tối thiểu 8 biểu đồ:**

1. Phân bố Closing Price
2. Phân bố Volume
3. Boxplot giá cổ phiếu
4. Xu hướng giá theo thời gian
5. Top 10 cổ phiếu giao dịch nhiều nhất
6. Heatmap tương quan
7. Scatter Volume vs Close
8. Rolling Moving Average

Sau mỗi biểu đồ viết 2–3 câu insight - Viết 5–7 Business Insights sau EDA.

**Hoàn thiện:** Notebook BT3.

---

## Nguyễn Thị Mỹ Quyên - 4. Feature Engineering & Modeling

**Chỉnh file**

* `notebooks/BT4_Model.ipynb`

**Công việc**

1. Tạo Daily Return.
2. Tạo SMA5, SMA20.
3. Tạo Volatility.
4. Chia Train/Test.
5. Huấn luyện Linear Regression.
6. Huấn luyện Random Forest.

**Yêu cầu:** Hai mô hình hoạt động và giải thích quá trình thực hiện

---

## Hà Huy Dũng 5. - Model Evaluation & Business Insight

**Chỉnh file**

* `notebooks/BT4_Model.ipynb`
* `report/Final_Report.docx`

**Công việc**

1. Tính MAE, R², RMSE 
2. Vẽ Actual vs Predicted
3. Lập bảng so sánh hai mô hình.
4. Phân tích Feature Importance.
5. Lựa chọn mô hình tốt nhất và giải thích lý do (dựa trên MAE, RMSE, R²).
6. Viết phần Business Insight và Discussion trong report/Final_Report.docx.

**Yêu cầu:** Đánh giá mô hình trong BT4 - Viết phần đánh giá mô hình trong báo cáo.

---

## Kiều Trung Đạt – 6. Report & Presentation

**Chỉnh các file**

* `report/Final_Report.docx`
* `slides/Final_Slide.pptx`
* `docs/Peer_Review.md`

**Công việc**

1. Tổng hợp báo cáo từ các thành viên.
2. Chuẩn hóa hình ảnh và bảng biểu.
3. Thiết kế slide 10–12 trang.
4. Viết Peer Review (ghi nhận góp ý và điều chỉnh).
5. Kiểm tra toàn bộ notebook chạy không lỗi.

**Hoàn thiện:** Báo cáo hoàn chỉnh + Slide + Peer Review.
