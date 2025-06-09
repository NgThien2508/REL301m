# Mô Hình Trong Học Tăng Cường Là Gì?

## 1. Tổng Quan
Mô hình (model) trong học tăng cường là một biểu diễn của môi trường, cho phép agent dự đoán kết quả của các hành động mà không cần thực hiện chúng trực tiếp. Mô hình giúp agent lập kế hoạch và tối ưu hóa quyết định.

## 2. Các Loại Mô Hình
### 2.1. Mô Hình Chuyển Trạng Thái
- Dự đoán trạng thái tiếp theo khi thực hiện một hành động
- Biểu diễn bởi hàm $P(s'|s,a)$: Xác suất chuyển từ trạng thái $s$ sang $s'$ khi thực hiện hành động $a$

### 2.2. Mô Hình Phần Thưởng
- Dự đoán phần thưởng nhận được khi thực hiện một hành động
- Biểu diễn bởi hàm $R(s,a)$: Phần thưởng kỳ vọng khi thực hiện hành động $a$ trong trạng thái $s$

## 3. Ví Dụ Minh Họa
### 3.1. Trò Chơi Đường Đi (Gridworld)
- Mô hình chuyển trạng thái: Dự đoán vị trí tiếp theo khi di chuyển
- Mô hình phần thưởng: Dự đoán phần thưởng khi đến một vị trí cụ thể

### 3.2. Robot Học Di Chuyển
- Mô hình chuyển trạng thái: Dự đoán vị trí và hướng tiếp theo khi thực hiện một hành động
- Mô hình phần thưởng: Dự đoán phần thưởng khi hoàn thành một nhiệm vụ

## 4. Ưu Điểm và Hạn Chế
### 4.1. Ưu Điểm
- Cho phép lập kế hoạch trước
- Giảm số lần tương tác thực tế với môi trường
- Tăng tốc độ học và hiệu quả

### 4.2. Hạn Chế
- Có thể không chính xác nếu môi trường phức tạp
- Yêu cầu nhiều tài nguyên tính toán
- Khó xây dựng cho môi trường lớn hoặc liên tục

## 5. Kết Luận
Mô hình là một công cụ quan trọng trong học tăng cường, giúp agent học hiệu quả hơn thông qua việc lập kế hoạch và dự đoán kết quả của các hành động.
