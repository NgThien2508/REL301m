# Xấp Xỉ Phi Tuyến với Mạng Nơ-ron

## Tổng Quan
Mạng nơ-ron cung cấp phương pháp xấp Xỉ phi tuyến mạnh mẽ, cho phép học các đặc trưng phức tạp từ dữ liệu.

## Cấu Trúc Mạng

### Khởi Tạo
- Trọng số ngẫu nhiên
- Hàm kích hoạt phi tuyến
- Cấu trúc lớp ẩn

### Xử Lý Đầu Vào
- Chuẩn hóa dữ liệu
- Biến đổi đặc trưng
- Truyền tín hiệu

## Tạo Đặc Trưng

### Lớp Ẩn
- Học biểu diễn trung gian
- Kết hợp đặc trưng
- Tạo đặc trưng mới

### Hàm Kích Hoạt
- ReLU: $f(x) = max(0,x)$
- Sigmoid: $f(x) = \frac{1}{1+e^{-x}}$
- Tanh: $f(x) = \frac{e^x-e^{-x}}{e^x+e^{-x}}$

## So Sánh với Tile Coding

### Điểm Tương Đồng
- Đều tạo đặc trưng từ đầu vào
- Có thể biểu diễn hàm phức tạp
- Cần điều chỉnh tham số

### Điểm Khác Biệt
- Mạng nơ-ron: học đặc trưng tự động
- Tile Coding: đặc trưng cố định
- Mạng nơ-ron: linh hoạt hơn

## Biểu Diễn Trực Quan

### Vùng Thu Nhận
- Mỗi nơ-ron có vùng thu nhận riêng
- Các vùng có thể chồng lấp
- Tạo biểu diễn phân tán

### Ví Dụ Thực Tế
- Nhận dạng hình ảnh
- Xử lý ngôn ngữ tự nhiên
- Điều khiển robot

## Ưu Điểm và Hạn Chế

### Ưu Điểm
- Linh hoạt trong biểu diễn
- Tổng quát hóa tốt
- Học đặc trưng tự động

### Hạn Chế
- Cần nhiều dữ liệu
- Tốn kém tính toán
- Khó hiểu và giải thích

## Kết Luận
Mạng nơ-ron cung cấp phương pháp xấp xỉ phi tuyến mạnh mẽ, đặc biệt phù hợp cho các bài toán phức tạp cần học biểu diễn tự động.
