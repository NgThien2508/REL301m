# Gradient Descent cho Huấn Luyện Mạng Nơ-ron

## Tổng Quan
Thuật toán backpropagation dựa trên gradient descent để tối thiểu hóa hàm mất mát, cho phép huấn luyện mạng nơ-ron hiệu quả.

## Ký Hiệu và Cấu Trúc

### Thành Phần
- Đầu vào: $S$
- Đầu ra: $\hat{y}$
- Lớp ẩn: $x$
- Trọng số: $A$ và $B$

### Cấu Trúc Mạng
- Lớp đầu vào → Lớp ẩn → Lớp đầu ra
- Hàm kích hoạt phi tuyến
- Hàm mất mát

## Đạo Hàm Gradient

### Gradient cho Trọng Số B
$$\frac{\partial L}{\partial B} = \frac{\partial L}{\partial \hat{y}} \frac{\partial \hat{y}}{\partial B}$$
- $\frac{\partial L}{\partial \hat{y}}$: gradient của hàm mất mát
- $\frac{\partial \hat{y}}{\partial B}$: gradient của đầu ra

### Gradient cho Trọng Số A
$$\frac{\partial L}{\partial A} = \frac{\partial L}{\partial x} \frac{\partial x}{\partial A}$$
- $\frac{\partial L}{\partial x}$: gradient truyền ngược
- $\frac{\partial x}{\partial A}$: gradient của lớp ẩn

## Thuật Toán Backpropagation

### Quá Trình Truyền Xuôi
1. Tính đầu ra lớp ẩn
2. Tính đầu ra mạng
3. Tính hàm mất mát

### Quá Trình Truyền Ngược
1. Tính gradient đầu ra
2. Cập nhật trọng số B
3. Tính gradient lớp ẩn
4. Cập nhật trọng số A

### Cập Nhật Trọng Số
$$w_{t+1} = w_t - \alpha \nabla_w L$$
- $\alpha$: tốc độ học
- $\nabla_w L$: gradient của hàm mất mát

## Tối Ưu Hóa

### Hiệu Quả Tính Toán
- Tránh tính toán lặp lại
- Lưu trữ kết quả trung gian
- Tận dụng tính chất chuỗi

### Mạng Sâu
- Tính toán đệ quy
- Gradient cho nhiều lớp
- Vấn đề tiêu biến gradient

## Ví Dụ Cụ Thể

### ReLU Activation
- $f(x) = max(0,x)$
- $\frac{\partial f}{\partial x} = 1$ nếu $x > 0$
- $\frac{\partial f}{\partial x} = 0$ nếu $x \leq 0$

### Linear Output
- $\hat{y} = Bx$
- $\frac{\partial \hat{y}}{\partial B} = x$
- $\frac{\partial \hat{y}}{\partial x} = B$

## Kết Luận
Gradient descent và backpropagation cung cấp phương pháp hiệu quả để huấn luyện mạng nơ-ron, cho phép học các biểu diễn phức tạp từ dữ liệu.
