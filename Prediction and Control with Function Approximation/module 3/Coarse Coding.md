# Coarse Coding

## Tổng Quan
Coarse Coding là kỹ thuật biểu diễn đặc trưng linh hoạt trong học tăng cường, cho phép tổng quát hóa giữa các trạng thái tương tự.

## Nguyên Lý Hoạt Động

### Kích Hoạt Đặc Trưng
- Mỗi đặc trưng được kích hoạt bởi một vùng hình dạng cụ thể
- Trạng thái có thể kích hoạt nhiều đặc trưng cùng lúc
- Tạo ra biểu diễn phân tán (distributed representation)

### Vùng Thu Nhận (Receptive Fields)
- Mỗi đặc trưng có một vùng thu nhận riêng
- Các vùng có thể chồng lấp
- Cho phép phân biệt tinh tế giữa các trạng thái

## So Sánh với State Aggregation

### Điểm Khác Biệt
- State Aggregation: phân chia không gian trạng thái thành các vùng rời rạc
- Coarse Coding: cho phép chồng lấp và biểu diễn mềm dẻo hơn

### Ưu Điểm của Coarse Coding
- Tổng quát hóa tốt hơn
- Biểu diễn liên tục
- Phù hợp với không gian trạng thái lớn

## Ứng Dụng

### Không Gian Liên Tục
- Biểu diễn trạng thái liên tục
- Xấp xỉ hàm giá trị
- Học chính sách

### Không Gian Nhiều Chiều
- Mở rộng tự nhiên cho nhiều chiều
- Duy trì tính chất tổng quát hóa
- Hiệu quả tính toán

## Kết Luận
Coarse Coding cung cấp phương pháp biểu diễn đặc trưng hiệu quả, đặc biệt phù hợp với các bài toán có không gian trạng thái lớn và liên tục.