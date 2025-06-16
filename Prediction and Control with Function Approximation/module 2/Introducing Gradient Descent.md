# Giới Thiệu Gradient Descent

## Khái Niệm Cơ Bản
Gradient descent là một phương pháp tối ưu hóa quan trọng trong học máy, đặc biệt là trong học tăng cường. Phương pháp này giúp chúng ta tìm ra các tham số tối ưu bằng cách di chuyển theo hướng ngược với gradient của hàm mục tiêu.

## Nguyên Lý Hoạt Động

### Cập Nhật Tham Số
$$\theta_{t+1} = \theta_t - \alpha \nabla_\theta J(\theta_t)$$
Trong đó:
- $\theta_t$: vector tham số tại bước t
- $\alpha$: tốc độ học (learning rate)
- $\nabla_\theta J(\theta_t)$: gradient của hàm mục tiêu

### Đặc Điểm
- Di chuyển theo hướng giảm giá trị hàm mục tiêu
- Tốc độ học ảnh hưởng đến sự hội tụ
- Có thể bị mắc kẹt ở cực tiểu cục bộ

## Ứng Dụng Trong Học Tăng Cường

### Ước Lượng Giá Trị
- Cập nhật tham số để giảm sai số
- Sử dụng gradient của hàm mất mát
- Tối ưu hóa trực tuyến

### Tối Ưu Hóa Chính Sách
- Điều chỉnh tham số chính sách
- Tăng xác suất hành động tốt
- Giảm xác suất hành động xấu

## Các Biến Thể

### Batch Gradient Descent
- Cập nhật sau khi xem toàn bộ dữ liệu
- Hội tụ ổn định
- Tốn nhiều bộ nhớ

### Stochastic Gradient Descent
- Cập nhật sau mỗi mẫu
- Học nhanh hơn
- Dao động nhiều hơn

### Mini-batch Gradient Descent
- Kết hợp ưu điểm của cả hai
- Cân bằng giữa tốc độ và ổn định
- Phổ biến trong thực tế

## Kết Luận
Gradient descent là nền tảng cho nhiều thuật toán học tăng cường hiện đại, cho phép chúng ta tối ưu hóa các hàm phức tạp một cách hiệu quả.
